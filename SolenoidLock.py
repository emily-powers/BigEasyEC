from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html')
changePin = int(change in) #cast changepin to an int
if changePin == 1:
  print "ON"
  GPIO.output( relay , 1)             
elif changePin == 2:
  print "OFF"
  GPIO.output(relay, 0)
