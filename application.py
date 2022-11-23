from flask import Flask, render_template
from data_model import website_metadata, user_data

application = Flask(__name__)


@application.route("/")
def index():
    return render_template("resume.html", website_metadata=website_metadata, user_data=user_data)


if __name__ == "__main__":
    application.run(debug=True, port=5001)
