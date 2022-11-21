from flask import Flask, render_template

application = Flask(__name__)

# variables
email = "orezek@seznam.cz"
be_number = "+320 497 127 267"
cz_number = "+420 608 840 502"
age = 38
name = "Oldrich Rezek"
greeting = "Hey, I'm"
languages = ["English", "Czech"]

skills = {"AWS Cloud": 80, "Windows Server": 82, "Networking": 75, "Python": 50, "HTML": 55, "Linux": 45,
          "Problem Solving": 90, "VM Ware": 70, "Veeam": 60}

interests = ["Technology",
             "Blockchain",
             "Finance",
             "Sport",
             "Photography",
             "History",
             "Philosophy",
             "Travelling",
             "Exploring"]


@application.route("/")
def index():
    return render_template("resume.html", email=email, be_number=be_number,
                           cz_number=cz_number, name=name, greeting=greeting, interests=interests)


if __name__ == "__main__":
    application.run(debug=True, port=5001)
