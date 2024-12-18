#Prompt for first number
num1 = int(input("Enter the first number:"))

#Prompt for the second number
num2 = int(input("Enter the second number:"))

operator = input("Choose the operation (+,-,*, /)") 

#Performing of operations using the match case
match operator:
  case "+":
    result = num1 + num2 
  case "-":
    result = num1 - num2
  case "*"  :
    result = num1 * num2
  case "/"  :
    if num2 != 0:
      result= num1 / num2
    else:
      print("Cannot divide by zero.")
      exit()
 # case _:
  #  result = "Invalid Operator"

print(f"The result is {result}")    
