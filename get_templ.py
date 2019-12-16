import tornado.web
import json
import os
from os import listdir
from os.path import isfile, join

class get_template(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "text/plain")
        # fd = os.open("templates/"+self.get_argument("tname")+".txt",os.O_RDWR)
        # readBytes = os.read(fd, 50)
        # os.close(fd)
        with open("templates/"+self.get_argument("tname")+".txt", "rb") as f:
            byte = f.read()   
        self.write(json.loads(byte))

class get_template_list(tornado.web.RequestHandler):
    def get(self):
        onlyfiles = [f for f in listdir('templates') if isfile(join('templates', f))]
        self.set_header("Content-Type", "text/plain")
        self.write(json.dumps(onlyfiles))