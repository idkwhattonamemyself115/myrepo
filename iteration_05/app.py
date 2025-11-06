from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    phone_number = 13000000000
    is_student=False
    email = "khu27@nmhschool.org"
    return render_template("contact.html", email=email, is_student=is_student, phone_number=phone_number)
@app.route("/tools_used")
def tool_used():
    tools = ["Flask", "Jinja2", "Python"]
    return render_template("tools_used.html", tools=tools)

@app.route("/about")
def about():
    work_in_tech=True
    techonological_companies= ["Google", "Apple", "Microsoft", "Amazon", "Facebook"]
    return render_template("about.html", author=" ",techonological_companies=techonological_companies, work_in_tech=work_in_tech, is_student=True)

app.run(debug=True)