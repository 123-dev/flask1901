from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')

def index():
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
    return render_template('index.html',name=name,movies=movies)

# #动态路由
# @app.route('/index/<name>')
# def home(name):
#     return "<h1>Hello,flask, %s</h1>"%name