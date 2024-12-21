from flask import Flask, jsonify, request

app = Flask(__name__) 

@app.route('/', methods=['GET','POST'])
def function1():
    return 'This is function 1. Is this really function 1. Test again'

@app.route('/function2', methods=['GET','POST'])
def function2():
    var = "This is function2"
    print(var)
    return var

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)