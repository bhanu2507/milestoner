import tornado.web
import json
import os
from os import listdir
from os.path import isfile, join

class get_template(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "text/plain")
        try:
            with open("templates/"+self.get_argument("tname")+".txt", "rb") as f:
                byte = f.read()   
            self.write(json.loads(byte))
        except:
            self.write("Cannot open the file or no file exists")


class get_template_list(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "text/plain")
        try:
            onlyfiles = [f for f in listdir('templates') if isfile(join('templates', f))]
            self.write(json.dumps(onlyfiles))
        except:
            self.write("cannot get list of templates")    

        