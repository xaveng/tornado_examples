#!/usr/bin/env python

import tornado.ioloop
import tornado.options
import tornado.web
import tornado.escape
import os.path
import json
import datetime


from tornado.options import define, options

define("port", default=3000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
        ]
        settings = dict(
            debug=True,
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static")
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", messages=None)
    
    def post(self):
        now = datetime.datetime.now()
        now = now.ctime()
        data = tornado.escape.json_decode(self.request.body)
        response_to_send = dict(now = now)
        self.write(json.dumps(response_to_send))

def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
