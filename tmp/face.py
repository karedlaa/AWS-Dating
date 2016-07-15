from datetime import date
import os.path
import tornado.escape
import tornado.ioloop
import tornado.template as template

import tornado.web
 
class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        response = { 'version': '3.5.1',
                     'last_build':  date.today().isoformat() }
        self.write(response)
 
class GetGameByIdHandler(tornado.web.RequestHandler):
    def get(self, id):
        response = { 'id': int(id),
                     'name': 'Crazy Game',
                     'release_date': date.today().isoformat() }
        self.write(response)

class login(tornado.web.RequestHandler):
    def get(self):
        myvalue = 9
        t = template.Template("<html>{{ myvalue }}</html>")
        print t.generate(myvalue="XXX")
        
class welcome(tornado.web.RequestHandler):
    def get(self):
        
        self.write("Hi Ravi Welcome")
 #(r"/login/([0-9]+)", GetGameByIdHandler),
application = tornado.web.Application([
    (r"/", welcome),
    (r"/login", login),
    (r"/version", VersionHandler)
])
 
settings = dict(
    template_paths = os.path.join(os.path.dirname(__file__), "templates"),
    static_paths = os.path.join(os.path.dirname(__file__), "static"),
    debug=True
)

if __name__ == "__main__":
    application.listen(8082)
    tornado.ioloop.IOLoop.instance().start()