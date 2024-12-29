from os import system, name
import statistics

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
    print("6. Standard Deviation (sample)")
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
        case "5":
            get_numbers("average")
        case "6":
            get_numbers("stdev")
        case "q":
            active = False

    print("Goodbye!")

def add(number_list):
    sum = 0
    for num in number_list:
        sum += num
    print(sum)

def subtraction(number_list):
    value = number_list[0]
    for i in range(1,len(number_list)):
        value -= number_list[i]
    print(value)

def multiplication(number_list):
    value = 1
    for num in number_list:
        value *= num
    print(value)

def division(number_list):
    value = number_list[0]
    for i in range(1,len(number_list)):
        value /= number_list[i]
    print(value)

def average(number_list):
    sum = 0
    for num in number_list:
        sum += num
    print(sum/len(number_list))

def stdev(number_list):
    print(statistics.stdev(number_list))

def get_numbers(function):
    user_input = []
    active = True
    print("Enter numbers followed by a carraige return. Enter a # symbol when ready to perform the operation")
    while active:
        temp_input = input(">>>")
        try:
            user_input.append(float(temp_input))
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
        case "average":
            average(user_input)
        case "stdev":
            stdev(user_input)
main()