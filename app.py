import tornado.ioloop
import tornado.web
import tornado.autoreload
import json
import os
import get_templ


class post_project_template(tornado.web.RequestHandler):
    def post(self):
        """ print(self.request.body) """
        print(json.loads(self.request.body))
        create_template(json.loads(self.request.body))
        self.write('successfully posted')

application = tornado.web.Application([
    (r"/", get_templ.Hello),
    (r"/post_project_template", post_project_template),
    (r"/get_template", get_templ.get_template),
    (r"/get_template_list", get_templ.get_template_list)
], debug=True)


def create_template(tjson):
    with open(os.path.join("templates","templatetext.txt"), 'w') as outfile:
        json.dump(tjson, outfile)

if __name__ == "__main__":
    """ app = make_app() """
    application.listen(8888)
    tornado.autoreload.start()
    tornado.ioloop.IOLoop.current().start()

