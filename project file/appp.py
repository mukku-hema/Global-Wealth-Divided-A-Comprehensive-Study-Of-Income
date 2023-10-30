from flask import Flask, render_template, request


Global = Flask(__name__) # initializng the flask app


@Global.route('/')
def helloworld():
    return render_template("index.html")

if __name__ == '__main__':
    Global.run(debug = False, port = 5000)
    