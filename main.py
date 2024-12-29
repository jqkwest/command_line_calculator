from os import system, name

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
def main():
    clear()
    print("Welcome to the command line calculator")
    print("Please select the operation you would like to run from the list below")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiplication")
    print("4. Division")
    print("5. Average")
    print("6. Standard Deviation")
    print("q: Quit")
    repl()

def repl():
    active = True
    while active:
      user_input = input(">>> ")
      match user_input:
        case "1":
            get_numbers("addition")
        case "2":
            get_numbers("subtraction")
        case "3":
            get_numbers("multiplication")
        case "4":
            get_numbers("division")
        case "q":
            active = False

    print("Goodbye!")

def add(number_list):
    sum = 0
    for num in number_list:
        sum += float(num)
    print(sum)

def subtraction(number_list):
    value = float(number_list[0])
    for i in range(1,len(number_list)):
        value -= float(number_list[i])
    print(value)

def multiplication(number_list):
    value = 1
    for num in number_list:
        value *= float(num)
    print(value)

def division(number_list):
    value = float(number_list[0])
    for i in range(1,len(number_list)):
        value /= float(number_list[i])
    print(value)

def get_numbers(function):
    user_input = []
    active = True
    print("Enter numbers followed by a carraige return. Enter a # symbol when ready to perform the operation")
    while active:
        temp_input = input(">>>")
        try:
            float(temp_input)
            user_input.append(temp_input)
        except ValueError:
            if temp_input =="#":
                active = False
            else:
                 print("Please only enter numbers")
        if temp_input == "#":
            active = False
        
    match function:
        case "addition":
            add(user_input)
        case "subtraction":
            subtraction(user_input)
        case "multiplication":
            multiplication(user_input)
        case "division":
            division(user_input)
main()