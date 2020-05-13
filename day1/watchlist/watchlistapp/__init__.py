import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

WIN = sys.platform.startswith('win')
if WIN:
    #widows的路径
    prefix = 'sqlite:///'   
else:
    #linux里的路径
    prefix = 'sqlite:////'  


app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path),'data.db')    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #关闭了对模型修改的监控 
app.config['SECRET_KEY'] = 'watchlist_dev'

db = SQLAlchemy(app)    #初始化扩展，传入程序实例app
 
from watchlistapp.models import User

login_manager = LoginManager(app)    #实例化登录扩展类
@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    return user
login_manager.login_view = 'login'

# 模板上下文处理函数
@app.context_processor
def common_user():
    user = User.query.first()
    return dict(user=user)

from watchlistapp import views,errors,commands
