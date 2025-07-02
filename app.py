from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-very-secret-key'


@app.route('/')
def home():
    return render_template("home.html", title="Home", name="Priyanshu Gupta")

@app.route('/about')
def about():
    return render_template("about.html", title="About")

@app.route('/projects')
def projects():
    return render_template("projects.html", title="Projects")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        flash('Thank you for reaching out! I will get back to you soon.')
        return redirect(url_for('contact'))
    return render_template("contact.html", title="Contact")

if __name__ == "__main__":
    app.run(debug=True)
