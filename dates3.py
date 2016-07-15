import botocore
from boto3 import resource


class dates3():
    s3 = resource('s3', region_name='us-east-1')

    def new_bucket(self, mybucket):
        newb = self.s3.create_bucket(mybucket,
                                     ACL='public-read',
                                     CreateBucketConfiguration={
                                         'LocationConstraint': 'us-east-1' | 'us-west-2'
                                     }
                                     )
        return newb

    def look_bucket(self, mybucket):
        exists = True
        try:
            self.s3.meta.client.head_bucket(Bucket=mybucket)
        except botocore.exceptions.ClientError as e:
            error_code = int(e.response['Error']['Code'])
            if error_code == 404:
                exists = False
        return exists

    def set_content(self, bucketname, content):
        if not self.look_bucket(bucketname):
            bucket = self.new_bucket(bucketname)
        else:
            bucket = self.s3.Bucket(bucketname)
        key = bucket.Key('profile_image')
        key.set_contents_from_string(content)
        key.set_acl('public-read')

    def get_all_buckets(self):
        for bucket in self.s3.buckets.all():
            for key in bucket.objects.all():
                print(key.key)
        return

    def put_acl(self, bucket):
        bucket.Acl().put(ACL='public-read')

    def get_grantinfo(self, bucket):
        acl = bucket.Acl()
        for grant in acl.grants:
            print(grant['Grantee']['DisplayName'], grant['Permission'])

    def add_grantee(self, bucket, email):
        bucket.Acl.put(GrantRead='emailAddress=%s'.format(email))

    def key_metadata(self, key):
        key.put(Metadata={'meta1': 'This is my metadata value'})
        print(key.metadata['meta1'])
