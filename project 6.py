# input a number
number = int(input("Enter a number: "))

# check if the number is even and greater than 10
if number % 2 == 0 and number > 10:
  print(f"the number {number} is even and greater than 10.")
else:
  print(f"the number {number} is not even or greater than 10.")
