from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])

# default: route answers to GET requests
# therefore, the result would be GET_login()
def login():
    if request.method == 'POST':
        return POST_login()
    else:
        return GET_login()

def POST_login():
    return 'POST method is used'

def GET_login():
    return 'GET method is used'

if __name__ == '__main__':
   app.run(debug=True)
