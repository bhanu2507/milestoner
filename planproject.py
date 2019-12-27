import tornado.web
import json
from datetime import datetime  
from datetime import timedelta 

class plan_project(tornado.web.RequestHandler):
    def post(self):
        planDict = {'final_plan': {'duration': 'none', 'completion_date': 'none', 'plan': 'none'}}
        self.set_header("Content-Type", "text/plain")
        try:
            with open("templates/"+self.get_argument("tname")+".txt", "rb") as f:
                jloop = json.loads(f.read())
                duration = 0  
            for plan in jloop['project_template']:
                duration = duration + plan['duration']
                plan['task_completion_date'] = 'test'
            # print(duration)
            # print(datetime.strptime(self.get_argument('sdate'), "%m/%d/%Y") + timedelta(duration))
            planDict['final_plan']['duration'] = duration
            planDict['final_plan']['completion_date'] = json.dumps(datetime.strptime(self.get_argument('sdate'), "%m/%d/%Y") + timedelta(duration), default=str)
            planDict['final_plan']['plan'] = jloop['project_template']
            self.write(planDict) 
        except:
            self.write("Cannot open the file or no file exists")