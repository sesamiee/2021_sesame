from flask import Flask

app = Flask(__name__)



@app.route("/")
def hello() :
    return '''
    <p>Hello, Flask</p>
    <a href="/first">Go first</a> 
    <a href="/second">Go second</a> 
    '''

@app.route("/first")
def first() :
    return '''
    <p>First page</p>
    <a href="/">Go Home</a>
    '''

@app.route("/second")
def second() :
    return '''
    <p>second page</p>
    <a href="/">Go Home</a>
    '''

if __name__ == "__main__" : #터미널에서 직접 실행한 경우
    app.run(host="0.0.0.0")