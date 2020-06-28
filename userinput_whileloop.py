# input() function

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# multiline prompt

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

message = input(prompt)
print(message)

# Using int() to Accept Numerical Input

age = input("How old are you ? : ")
age = int(age) #Will give error if not converted to string as input returns the value in the form of string

print(age >= 18)

# While Loop

current_no = 1
while(current_no < 6) :
    print(current_no)
    current_no += 1

# Letting the User Choose When to Quit

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# Using break to Exit a Loop

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

message = ''
while True :
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(message)

# Using continue in a Loop

current_no = 0
while current_no <= 10:
    current_no += 1
    if current_no % 2 == 0:
        continue

    print(current_no)

# Filling a Dictionary with User Input

responses = {}
polling = True

while polling:
    name = input("Enter your name : ")
    response = input("Which mountain would you like to climb : ")

    responses[name] = response

    repeat = input("Would you like  to continue[yes / no] : ")
    if repeat == 'no':
        polling = False

print(responses)