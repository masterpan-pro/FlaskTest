# encoding: utf-8

from flask import Flask, url_for, redirect, render_template
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    # return 'Hello World!'
    return redirect(url_for('index', is_login=1))


@app.route('/login')
def login():
    return u'This is Login Page'


# URL传参测试
@app.route('/article/<id>')
def article(id):
    return u'您请求的参数为：%s' % id


# URL反转测试
@app.route('/reversal')
def reversal():
    url1 = url_for('hello_world')
    url2 = url_for('article', id=100)
    print(url1, url2)
    return u'hello_world()->%s, article(100)->%s' % (url1, url2)


# 页面跳转和重定向
@app.route('/redirect/<is_login>')
def redirect_test(is_login):
    if is_login == '1':
        return u'没有登录'
    else:
        return redirect(url_for('login'))


# 模板渲染和参数传递
@app.route('/index/<is_login>')
def index(is_login):
    # return render_template('index.html', username=u'MasterPan')
    # return render_template('index.html', username=u'MasterPan', age=u'24')
    if is_login == '1':
        user = {
            'username': u'MasterPan',
            'age': 24
        }
        # For循环
        for k, v in user.items():
            print(k, v)

        users = [
            {
                'username': u'MasterPan',
                'age': 18
            },
            {
                'username': u'ZhangSan',
                'age': 19
            },
            {
                'username': u'LiSi',
                'age': 20
            }
        ]
        for item in users:
            for k, v in item.items():
                print(k, v)
    else:
        user = None
    return render_template('index/index.html', user=user)


if __name__ == '__main__':
    app.run()
