from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/form/', methods=['POST'])
def form():
    id, date = request.args.to_dict().values()
    print(f'ID: {id}, Date: {date}')
    name, email, lastname = request.form.values()
    print(f'Name: {name}, lastname: {lastname}, Email: {email}')
    return {"status": "success"}

@app.route('/index')
def index():
    response = make_response({"response": "success"})
    return response