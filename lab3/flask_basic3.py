from flask import Flask,render_template, redirect, url_for

app = Flask(__name__)

@app.route('/admin')

def index():
    return render_template("index.html", message="hello flask", contacts=['c1','c2','c3','c4','c5']); 

# render_template(): render web page tempalte via jinja2 (template engine)
# designate html file to render and the variables to send

if __name__ == '__main__':
    app.run(debug=True)