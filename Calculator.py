tries = 0 

while True:

          operator = input("Enter one of the following operators +-*/:  ")
          num1 = float(input("Enter the first number: "))
          num2 = float(input("Enter the second number: "))

          tries += 1

          if operator == "+":
              result = (num1 + num2)
              print(round(result,2))
          elif operator == "-":
              result = (num1 - num2)
              print(round(result,2))
          elif operator == "*":
              result = (num1 * num2)
              print(round(result,2))
          elif operator == "/":
              result = (num1 / num2)
              print(round(result,2))
          else:
              print("Invalid")

          print(f"You've done {tries} calculations so far")

          again = input("Do you want to calculate again? (yes/no): ").lower()
          if again != "yes":
              print(f"Goodbye! You made {tries} total")
              break