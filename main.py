from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('form.html')

@app.route('/action_page/', methods=['GET'])
def action_page():
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    return '''
        <p>{}</p>
        <p>{}</p>
    '''.format(fname,lname)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3542, debug=True)