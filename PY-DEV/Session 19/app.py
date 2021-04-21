from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return "Hello World"

@app.route("/home")
def home():
    # return '{"data":"Welcome to Home."}'
    # return open("response.json").read()
    return "<html>\
                <head><title>My home</title></head>\
                <body>Welcome to home\n</body>\
            </html>"

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)