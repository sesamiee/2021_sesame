from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)
LED_red = 4
LED_blue = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_red, GPIO.OUT)
GPIO.setup(LED_blue, GPIO.OUT)


@app.route("/")
def home() :
    return '''
    <p>Hello, Flask!</p>
    <a href="/led/red/on">RED LED ON</a> 
    <a href="/led/red/off">RED LED OFF</a>
    <a href="/led/blue/on">BLUE LED ON</a>
    <a href="/led/blue/off">BLUE LED OFF</a>
    '''

@app.route("/led/<color>/<op>")
def led_op(color,op) :
    if color == "red" and op == "on" :
        GPIO.output(LED_red, GPIO.HIGH)
        return '''
        <p>RED LED ON</p>
        <a href="/">Go Home</a>
        '''
    elif color == "red" and op == "off" :
        GPIO.output(LED_red, GPIO.LOW)
        return '''
        <p>LED OFF</p>
        <a href="/">Go Home</a>
        '''
    elif color == "blue" and op == "on" :
        GPIO.output(LED_blue, GPIO.HIGH)
        return '''
        <p>BLUE LED ON</p>
        <a href="/">Go Home</a>
        '''
    elif color == "blue" and op == "off" :
        GPIO.output(LED_blue, GPIO.LOW)
        return '''
        <p>BLUE LED OFF</p>
        <a href="/">Go Home</a>
        '''

if __name__ == "__main__" : #터미널에서 직접 실행한 경우
    try :
        app.run(host="0.0.0.0")
    finally :
        GPIO.cleanup()


