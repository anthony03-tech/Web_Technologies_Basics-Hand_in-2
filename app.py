from flask import Flask, render_template, jsonify

app = Flask(__name__)

users = {
    1:  {"name": "Alex Martin",    "email": "alex.martin@email.com", "avatar": "A", "member": "Member since January 2024"},
    2: {"name": "Bob Nakamura",  "email": "bob@example.com", "avatar": "B", "member": "Member since March 2018"},
    3: {"name": "Clara Osei",    "email": "clara@example.com", "avatar": "C", "member": "Member since June 2025"},
}


@app.route("/")
def homePage():
    return render_template("FirstPage_To-do-list.html")


@app.route("/account")
def account():
    return render_template("SecondPage_account.html")


@app.route("/account/<int:user_id>")
def get_user(user_id):
    user = users.get(user_id)
    return jsonify({"id": user_id, **user})


@app.route("/settings")
def settings():
    return render_template("ThirdPage_Settings.html")


app.run(debug=True)
