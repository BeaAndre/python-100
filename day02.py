print("Welcome to the tip calculator!\nWhat was the total bill?")
total = float(input("$"))

print("How much tip (in percentage) would you like to give?")
percentage = int(input("%"))

print("How many people are splitting the bill?")
people = int(input())

with_tip = total + (total*(percentage/100))
result = round(with_tip/people, 2)

print(f"Each person should pay: ${result}.")