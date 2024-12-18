#weather = ["sunny", "rainy", "cold"]
weather = input("What's the weather like today? (sunny/rainy/cold):").lower()

#Avdvise for a sunny day
if weather == "sunny":
  print("Wear a t-shirt and sunglasses.")

#Advise for a Rainy day
elif weather == "rainy":
  print("Don't forget your umbrella and a raincoat.")

# Advise for a cold day
elif weather == "cold" :
  print(" Make sure to wear a warm coat and a scarf.")

else:
  print("Sorry, I don't have recommendations for this weather.")  