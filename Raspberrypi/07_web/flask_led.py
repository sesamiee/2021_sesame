from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)
LED_red = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_red, GPIO.OUT)


@app.route("/")
def hello() :
    return '''
    <p>Hello, Flask</p>
    <a href="/led/on">LED ON</a> 
    <a href="/led/off">LED OFF</a> 
    '''

@app.route("/led/<op>")
def led_op(op) :
    if op == "on" :
        GPIO.output(LED_red, GPIO.HIGH)
        return '''
        <p>LED ON</p>
        <a href="/">Go Home</a>
        '''
    elif op == "off" :
        GPIO.output(LED_red, GPIO.LOW)
        return '''
        <p>LED OFF</p>
        <a href="/">Go Home</a>
        '''

@app.route("/sesami/<op>")
def wasans(op):
    return "<p> sesami is " + op + "</p>"



if __name__ == "__main__" : #터미널에서 직접 실행한 경우
    try :
        GPIO.cleanup()
    finally :
        app.run(host="0.0.0.0")

