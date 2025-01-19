print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("How much % of tip would you like to give? 10, 12, or 15? "))
total_to_be_paid = percentage_tip * float(f"1.{percentage_tip}")

number_of_people = int(input("How many people to split the bill? "))


print(f"Each person should pay: ${round(total_to_be_paid / number_of_people, 2)}")
