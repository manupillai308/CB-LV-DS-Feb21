from flask import Flask, render_template, request, jsonify, redirect


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    elif request.method == "POST":
        # value = request.form.get("fname")
        value = request.json.get("fname")
        if value is not None:
            return jsonify({"data": value})
        
        return redirect("/")


@app.route("/user/<username>/<int:count>")
def user(username, count):
    # return jsonify({"status": "OK", "user":username})
    return render_template("user.html", username=username, count=count)

# @app.route("/get_args", methods=["GET", "POST"])
# def get_args():
#     if request.method == "GET":
#         value = request.args.get("fname")
#     elif request.method == "POST":
#         value = request.form.get("fname")

#     if value is None:
#         return redirect("/")

#     return jsonify({"value": value})


if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)