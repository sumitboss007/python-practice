#Say hello to user
print("Hello \"friend\"")

#Ask user for there name
name = input("what's your name? ").strip().title()

#split user's name into first name and last name
first, last = name.split(" ")

#Say hello to user
print(f"hello  {name}")#this is called "f" string method
print(f"hello  {first}")#this is called "f" string method
print(f"hello  {last}")#this is called "f" string method