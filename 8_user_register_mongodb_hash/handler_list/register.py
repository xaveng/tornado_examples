import tornado.web
import utils.cipher
from .base import BaseHandler

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("register.html")

    def post(self):
        
