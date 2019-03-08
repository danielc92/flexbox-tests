from flask import Flask, render_template, session, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('i.html')

if __name__ =='__main__':
	app.run(debug=True)
