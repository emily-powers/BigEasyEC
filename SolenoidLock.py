// Source: https://iotdesignpro.com/projects/iot-based-solenoid-door-lock-using-raspberry-pi-4

from flask import Flask, render_template, request, redirect, url_for, make_response
import time
import RPi.GPIO as GPIO
relay = 18;

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)
GPIO.output(relay, 0)

app = Flask(__name__)
@app.route('/')

def index():
  return render_template('index.html')

@app.route('/<changepin>', methods=['POST'])

def reroute(changepin):
  changePin = int(changepin)
  if changePin == 1:
    print("ON")
    GPIO.output(relay, 1)
  elif changePin == 2:
    print("OFF")
    GPIO.output(relay, 0)
  response = make_response(redirect(url_for('index')))
  return response

app.run(debug=True, host='0.0.0.0', port=8000)
