import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

#Ex https://team-katil:hay_246skdabcdefgh@github.com/team-katil/ShiviXMusic
os.system("git clone https://username:token@github.com/username/reponame ok && cd ok && pip3 install -U -r requirements.txt && nohup python3 main.py &")
