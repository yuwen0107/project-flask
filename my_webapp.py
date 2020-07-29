from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app) #建立bootstrap物件

@app.route('/')
def show_resume():
    return render_template('resume.html')

@app.route('/index')
def my_index():
    return render_template('index.html')

@app.route('/index/new')
def new_data():
    return render_template('new.html')

@app.route('/index/new/third')
def third_job():
    return render_template('third.html')



@app.errorhandler(404)  #錯誤處理(找不到頁面)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500) #錯誤處理(系統內部錯誤)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()