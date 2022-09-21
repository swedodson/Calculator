#Calculator program with functions to add, subtract, multiply, and divide floating point numbers.

#Add function
def add (n1, n2):
  return n1 + n2

#Subtract function
def subtract(n1, n2):
  return n1 - n2

#Multiply function
def multiply(n1, n2):
  return n1 * n2

#Divide function
def divide(n1, n2):
  return n1 / n2

#Dictionary to hold operation functions
operations = {
  "+":add, 
  "-":subtract, 
  "*":multiply, 
  "/":divide
}

def calculator():
  #User input for first number
  num1 = float(input("What's the first number? "))
  
  #Print options for operators for user to choose
  for symbol in operations:
    print(symbol)
  
  #Set Flag for continuing calculations
  should_continue = True
  
  while should_continue:
  #Take user input for operator
    operation_symbol = input("Pick an operation: ")
  
  #User input for second number
    num2 = float(input("What's the next number? "))
  
  #Create variables to hold operator and user inputs for calculating
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
  
  #Print result of operation
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == "y":
      num1 = answer
    #Use recursion to continue calling calculator function
    else:
      should_continue = False
      calculator()

calculator()
