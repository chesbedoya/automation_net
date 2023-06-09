from flask import Flask

app = Flask(__name__)

from mod_automation_services_net.controller import mod_netsuite as automation_selenium
app.register_blueprint(automation_selenium)
