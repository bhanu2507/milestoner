import tornado.web
import json
import os

def create_template(tjson, tname):
    with open(os.path.join("templates", tname + ".txt"), 'w') as outfile:
        json.dump(tjson, outfile)

class post_project_template(tornado.web.RequestHandler):
    def post(self):
        """ print(self.request.body) """
        print(json.loads(self.request.body))
        create_template(json.loads(self.request.body), self.get_argument("tname") )
        self.write('successfully posted')