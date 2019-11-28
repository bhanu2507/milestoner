import tornado.web

class Hello(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class get_template(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class get_template_list(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")