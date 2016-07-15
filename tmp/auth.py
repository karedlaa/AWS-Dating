import os.path
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

class MainHandler(tornado.web.RequestHandler,
                  tornado.auth.FacebookGraphMixin):
    @tornado.web.authenticated
    @tornado.gen.coroutine
    def get(self):
        new_entry = yield self.facebook_request(
            "/me/feed",
            post_args={"message": "I am posting from my Tornado application!"},
            access_token=self.current_user["access_token"])

        if not new_entry:
            # Call failed; perhaps missing permission?
            yield self.authorize_redirect()
            return
        self.finish("Posted a message!")


if __name__ == "__main__":
    
    application = tornado.web.Application([
        (r"/", welcome),
        (r"/login", FacebookGraphLoginHandler),
        (r"/version", VersionHandler)
    ])
    main(application)