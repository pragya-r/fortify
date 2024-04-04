from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route("/submit", methods=["POST"])
def submit():
   return render_template('results.html', sector = request.form['industry_sector'], size = request.form['size'], data = request.form['data'], security = request.form['security_level'])


if __name__ == '__main__':
   app.run()