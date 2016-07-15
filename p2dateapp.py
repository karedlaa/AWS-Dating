from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from run import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(8080)
IOLoop.instance().start()