from flask import Flask, render_template
from data_model import website_headers, interests, skills, profile_summary_data_prod, job_titles

application = Flask(__name__)

# variables
email = "orezek@seznam.cz"
be_number = "+320 497 127 267"
cz_number = "+420 608 840 502"
age = 38
name = "Oldrich Rezek"
greeting = "Hey, I'm"
languages = ["English", "Czech"]


@application.route("/")
def index():
    return render_template("resume.html", email=email, be_number=be_number,
                           cz_number=cz_number, name=name, greeting=greeting,
                           interests=interests, website_headers=website_headers,
                           profile_summary_data_prod=profile_summary_data_prod, job_titles=job_titles)


if __name__ == "__main__":
    application.run(debug=True, port=5001)
