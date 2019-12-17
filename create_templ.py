import tornado.web
import json
import os

def create_template(tjson, tname):
    try:
        with open(os.path.join("templates", tname + ".txt"), 'w') as outfile:
            json.dump(tjson, outfile)
        return 1
    except:
        return 0        

class post_project_template(tornado.web.RequestHandler):
    def post(self):
        try:
            if create_template(json.loads(self.request.body), self.get_argument("tname")) == 1:
                self.write("Created")
            else:
                self.write("Failed to create the template")    
        except:
            self.write('failed')