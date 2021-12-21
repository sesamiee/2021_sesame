from flask import Flask, render_template
import RPi.GPIO as GPIO

LED_PIN = 4
LED_PIN_BLUE = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN_BLUE, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template("led2.html")

@app.route("/led/<color>/<op>")
def red_led_op(color, op):
  if color == "red":
    if op == "on":
      GPIO.output(LED_PIN, 1)
    elif op == "off":
      GPIO.output(LED_PIN, 0)
  elif color == "blue":
    if op == "on":
      GPIO.output(LED_PIN_BLUE, 1)

    elif op == "off":
      GPIO.output(LED_PIN_BLUE, 0)


if __name__ == "__main__":
  app.run(host="0.0.0.0")