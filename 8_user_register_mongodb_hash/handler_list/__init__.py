import tornado.web

from handler_list.main  import *
from handler_list.base  import *

get_handler_list = [
    tornado.web.url(r'/', MainHandler, name="main"),
    tornado.web.url(r'/login', LoginHandler, name="login"),
    tornado.web.url(r'/logout', LogoutHandler, name="logout"),
    tornado.web.url(r'/register', RegisterHandler, name="register"),
]
