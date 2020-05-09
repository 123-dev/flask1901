import os
import sys

from flask import Flask,render_template
import click
from flask_sqlalchemy import SQLAlchemy

WIN = sys.platform.startswith('win')

if WIN:
    #widows的路径
    prefix = 'sqlite:///'   
else:
    #linux里的路径
    prefix = 'sqlite:////'  

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path,'data.db')    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #关闭了对模型修改的监控 

db = SQLAlchemy(app)    #初始化扩展，传入程序实例app

#models
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))
#view
@app.route('/')

def index():
    
    user = User.query.first()
    movies = Movie.query.all()

    return render_template('index.html',user=user,movies=movies)


#自定义命令
# 新建data.db的数据库初始化命令
@app.cli.command()   #装饰器，注册命令
@click.option('--drop',is_flag=True,help='删除之后再创建')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("初始化数据库完成")

# 向data.db中写入数据的命令
@app.cli.command()
def forge():
    name = "Bruce"
    movies = [
        {"title":"大赢家","year":"2020"},
        {"title":"囧妈","year":"2020"},
        {"title":"战狼 ","year":"2020"},
        {"title":"西华路放","year":"2020"},
        {"title":"速度与激情8","year":"2020"},
        {"title":"我和我的祖国","year":"2020"},
        {"title":"大赢家","year":"2020"},
        {"title":"囧妈","year":"2020"},
        {"title":"战狼 ","year":"2020"},
        {"title":"西华路放","year":"2020"},
        {"title":"速度与激情8","year":"2020"},
        {"title":"我和我的祖国","year":"2020"},
        {"title":"大赢家","year":"2020"},
        {"title":"囧妈","year":"2020"},
        {"title":"战狼 ","year":"2020"},
        {"title":"西华路放","year":"2020"},
        {"title":"速度与激情8","year":"2020"},
        {"title":"我和我的祖国","year":"2020"},
    ]
    
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo("插入数据完成")