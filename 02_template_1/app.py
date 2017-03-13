#-*- coding:utf-8 -*-

import tornado.web
import tornado.httpserver
import tornado.ioloop
import os.path

from tornado.options import define, options
define("port", default=3000, help="run on the given port", type=int)

def add(x,y):
    return x+y

class Application(tornado.web.Application):
    def __init__(self):
        base_dir = os.path.dirname(__file__)
        settings = {
            "template_path":os.path.join(base_dir, "templates"),
            "static_path":os.path.join(base_dir, "static"),
            "debug":True,
        }
        tornado.web.Application.__init__(self, [
            tornado.web.url(r"/", MainHandler, name="main"),
        ], **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        value_test = "normal_value_1"
        list_test = ["list_value_1","list_value_2","list_value_3"]
        dict_test = dict(a="dict_value_1", b="dict_value_2")
        list_dict_test = [dict(number=1),dict(number=2), dict(number=3)]
        self.render("index.html", value_test = value_test,
                                  list_test = list_test,
                                  dict_test = dict_test,
                                  list_dict_test = list_dict_test,
                                  add = add)
def main():
    tornado.options.parse_command_line()
    Application().listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    print ("Open http://127.0.0.1:{}".format(options.port))
    main()

