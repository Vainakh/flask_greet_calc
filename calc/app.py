# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_sum():
  """ adding a and b (two integers) """
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  sum = add(a,b)
  return str(sum) 

@app.route("/sub")
def subtract_two():
  """ subtracting a and b (two integers) """
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  subtwo = sub(a,b)
  return str(subtwo) 

@app.route("/mult")
def multiply_two():
  """multipying a and b (two integers)"""
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  multtwo = mult(a,b)
  return str(multtwo) 

@app.route("/div")
def divide_two():
  """dividing a by b (two integers)"""
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  divtwo = div(a,b)
  return str(divtwo) 

