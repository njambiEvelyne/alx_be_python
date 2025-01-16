try:
  num = int(input("Enter a number: "))
  result = 100/num
  print(result)

except ValueError:
  print("Invlid input >>please enter a number")
except ZeroDivisionError:
  print("Cannot divide by zero")
else:
  print("Division successful")