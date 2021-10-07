from flask import Flask
app = Flask(__name__)  # Flask 객체를 app에 할당

@app.route('/') # app 객체를 이용해 라우팅 경로 설정 (해당 웹페이지에 대한 경로를 만들어 줌)
# 해당 라우팅 경로로 요청이 올 때 실행할 함수를 바로 밑에 작성해야함
def index():
    return "Welcome to CS492"

@app.route('/hello')
def hello():
    return "<h1>hello, world</h1>"

@app.route('/guest/<guest>')  # <variable>: 입력되는 값을 variable 값으로 지정/할당
def hello_guest(guest):
    return "Hello, %s! WElCOME!!" % guest

if __name__ == '__main__':
   app.run()
