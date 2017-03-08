#-*- coding:utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import os.path
import motor
import pprint

from tornado import gen
from tornado.options import define, options

define("port", default=3000, help="run on the given port", type=int)
db = motor.MotorClient('localhost').testdb

@gen.coroutine
def getdata():
    data = yield db.userinfo.find_one()
    return data

class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        data = yield db.userinfo.find_one()
        pprint.pprint(data)
        self.write("Hello, World%s" %data)

class Application(tornado.web.Application):
    def __init__(self):
        base_dir = os.path.dirname(__file__)
        handlers = [
           tornado.web.url(r"/", MainHandler, name="main"),
        ]
        settings = {
            'template_path' : os.path.join(base_dir, 'templates'),
            'static_path' : os.path.join(base_dir, 'static'),
            'debug' : True,
        }
        tornado.web.Application.__init__(self, handlers=handlers, **settings)

def main():
    tornado.options.parse_command_line()
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    print("Oen http://127.0.0.1:{}".format(options.port))
    main() 
