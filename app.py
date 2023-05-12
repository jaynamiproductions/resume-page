from flask import Flask
app = Flask(__name__)

@app.route('/')
def func():
    return 'hello'

# app.run(host='0.0.0.0',port=5000)