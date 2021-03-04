from flask import Flask, render_template
from replit import db


app = Flask(__name__)

@app.route('/')
def index():
  print(db['foo'])
  # matches = db.prefix("prefix")print(db['foo'])
  # db['foo'] = 10
  return render_template('index.html')

app.run(host='0.0.0.0', port=8080)