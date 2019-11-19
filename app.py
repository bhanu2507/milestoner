import tornado.ioloop
import tornado.web
import tornado.autoreload
import json

class Hello(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

""" class User(tornado.web.RequestHandler):
    def get(self):
        form = """<form method="post">
        <input type="text" name="username"/>
        <input type="text" name="designation"/>
        <input type="submit"/>
        </form>"""
        self.write(form)

    def post(self):
        username = self.get_argument('username')
        designation = self.get_argument('designation')
        self.write("Wow " + username + " you're a " + designation) """

class post_project_template(tornado.web.RequestHandler):
    def post(self):
        print(json.loads(self.request.body))
        self.write('successfully posted')

application = tornado.web.Application([
    (r"/", Hello),
    """ (r"/user", User), """
    (r"/post_project_template", post_project_template)
], debug=True)

if __name__ == "__main__":
    """ app = make_app() """
    application.listen(8888)
    tornado.autoreload.start()
    tornado.ioloop.IOLoop.current().start()

