import tornado.web
import json
from datetime import datetime  
from datetime import timedelta 

class plan_project(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Content-Type", "text/plain")
        try:
            with open("templates/"+self.get_argument("tname")+".txt", "rb") as f:
                # pplan = json.load(f.read())
                # print(pplan['project_template'][0])
                jloop = json.loads(f.read())
                duration = 0  
            for plan in jloop['project_template']:
                duration = duration + plan['duration']
            print(duration)
            print(datetime.strptime(self.get_argument('sdate'), "%m/%d/%Y") + timedelta(duration))
            self.write(jloop['project_template'][0])    
        except:
            self.write("Cannot open the file or no file exists")