import tornado.web

from utils.cipher import *
from .base import BaseHandler

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("register.html")

    def post(self):
        getusername = self.get_argument('username')
        getpassword = self.get_argument('password')
        self.write("%s,%s" %(getusername, getpassword))
        

