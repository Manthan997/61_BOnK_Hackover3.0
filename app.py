import site
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') 
@app.route('/home')
def index():
    return render_template('landing.html')

@app.route('/services')
def service():
    return render_template('service.html')

@app.route('/about') 
def about():
    return render_template('about.html')



if __name__ == "__main__":
    app.run(debug=True)