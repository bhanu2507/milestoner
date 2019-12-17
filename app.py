import tornado.ioloop
import tornado.web
import tornado.autoreload
import json
import os
import get_templ
import create_templ
import planproject


application = tornado.web.Application([
    # (r"/", get_templ.Hello),
    (r"/post_project_template", create_templ.post_project_template),
    (r"/get_template", get_templ.get_template),
    (r"/get_template_list", get_templ.get_template_list),
    (r"/get_project_plan", planproject.plan_project)
], debug=True)


if __name__ == "__main__":
    """ app = make_app() """
    application.listen(8888)
    tornado.autoreload.start()
    tornado.ioloop.IOLoop.current().start()

