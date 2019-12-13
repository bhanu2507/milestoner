import tornado.web


class get_template(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class get_template_list(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message"))