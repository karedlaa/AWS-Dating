#!flask/bin/python
import os

from flask import Flask, render_template, redirect, url_for, request

from awslib.dates3 import dates3
from awslib.datesns import datesns
from awslib.datesqs import datesqs
from awslib.dynamodb_date import dynamodb_date

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif', 'JPG', 'PNG', 'JPEG', 'GIF'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/home/updateprofile', methods=['GET', 'POST'])
def updateprofile():
    if request.method == 'POST':
        print request.form['name'] == ""
        if (request.form['name'] == "" or request.form['password'] == "" or
                    request.form['emailid'] == "" or request.form['phone'] == "" or
                    request.form['dob'] == "" or request.form['addrline1'] == "" or
                    request.form['addrline2'] == "" or request.form['city'] == "" or
                    request.form['state'] == "" or request.form['country'] == "" or
                    request.form['Gender'] == "" or request.form['Interested'] == ""):
            msg = 'All fields should be filled to complete sign up.'
            print msg
        else:
            db = dynamodb_date()
            db.insert_user(name=request.form['name'], pwd=request.form['password'], email=request.form['emailid'],
                           phone=request.form['phone'], dob=request.form['dob'], addrline1=request.form['addrline1'],
                           addrline2=request.form['addrline2'], addrCity=request.form['city'],
                           addrState=request.form['state'],
                           addrCountry=request.form['country'], gender=request.form['Gender'],
                           interestedIn=request.form['Interested'])
            msg = "Successfully updated"
    return redirect(url_for('.home', username=request.form['name']), code=302)


@app.route('/home/editprofile', methods=['GET', 'POST'])
def editprofile():
    error = None
    if request.method == 'POST':
        username = request.form["myname"]
        print username
        db = dynamodb_date()
        user_data = db.get_user(username)
        print user_data.get("address")

        return render_template('edit.html', user=user_data, error=error)
    return render_template('edit.html', error=error)


@app.route('/home/subscribe', methods=['GET', 'POST'])
def subscribe():
    uname = ""
    if request.method == 'POST':
        uname = request.form["mysub"]
        db = dynamodb_date()
        user_data = db.get_user(uname)
        notification = datesns()
        notification.subscribe1(user_data["email"])
    return redirect(url_for('.home', username=uname), code=302)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == "" or request.form['password'] == "":
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('.auth'), code=307)
    return render_template('login.html', error=error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        render_template('signup.html', error=error)
    return render_template('signup.html', error=error)


def upload(bucket, filename):
    file = 'uploads/' + filename
    s3 = dates3()
    s3.set_content(bucket, file)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    msg = ""
    if request.method == 'POST':
        if (request.form['name'] == "" or request.form['password'] == "" or
                    request.form['emailid'] == "" or request.form['phone'] == "" or
                    request.form['dob'] == "" or request.form['addrline1'] == "" or
                    request.form['addrline2'] == "" or request.form['city'] == "" or
                    request.form['state'] == "" or request.form['country'] == "" or
                    request.form['Gender'] == "" or request.form['Interested'] == ""):
            msg = 'All fields should be filled to complete sign up.'
            print msg
        else:
            db = dynamodb_date()
            db.insert_user(name=request.form['name'], pwd=request.form['password'], email=request.form['emailid'],
                           phone=request.form['phone'], dob=request.form['dob'], addrline1=request.form['addrline1'],
                           addrline2=request.form['addrline2'], addrCity=request.form['city'], addrState=request.form['state'],
                           addrCountry=request.form['country'], gender=request.form['Gender'],
                           interestedIn=request.form['Interested'])
            file = request.files['file']
            if file and allowed_file(file.filename):
                file.save(os.path.join("uploads", file.filename))

                upload(request.form['name'], file.filename)

            msg = "Successfully Registered"
    return render_template('signup.html', message=msg)


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    err = ""
    if request.method == 'POST':
        db = dynamodb_date()
        user = db.get_user(request.form['username'])
        if user["password"] == request.form['password']:
            return redirect(url_for('.home', username=request.form['username']), code=302)
        else:
            err = "Invalid Credentials! Try again"
    return render_template('login.html', error=err)


@app.route('/home/<username>', methods=['GET', 'POST'])
def home(username=None):
    if request.method == 'POST':
        # url: "{{ url_for('home', username=user_data.uname) }}",
        # print username
        # print request.data
        # print request.args
        # print request.values
        # print request.form
        sender = request.form["myusername"]
        receiver = request.form["liked_user"]
        msg = request.form["msg"]
        sqs = datesqs()
        sqs.send_mes(sender, receiver, msg)

    db = dynamodb_date()
    user = db.get_user(username)
    interested_users = db.get_intereseted(user["uname"], user["gender"], user["interestedIn"])
    chnl = ''.join(sorted(user["uname"] + interested_users[0]["uname"]))
    return render_template("home.html", user_data=user, interested_users=interested_users, channel= chnl)


if __name__ == "__main__":
    app.run(debug=True)
