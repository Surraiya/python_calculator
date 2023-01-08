def add(first_number,next_number):
    return first_number + next_number

def minus(first_number,next_number):
    return first_number - next_number

def multiply(first_number,next_number):
    return first_number * next_number

def division(first_number,next_number):
    if next_number == 0:
        return "Undefined"
    else: 
        return first_number / next_number

calculations = {
    "+": add,
    "-": minus,
    "*": multiply,
    "/": division
}

def calculator():
    from art import logo
    print(logo)
    recalculate = True
    first_number = int(input("What's the first number?\n"))
    while recalculate:
        for operators in calculations:
            print(operators)
        incorrect_operator = True
        while incorrect_operator:
            operator = input("Choose an operator: \n")
            if operator in calculations:
                incorrect_operator = False
        next_number = int(input("What's the next number? \n"))
        result = calculations[operator](first_number,next_number)
        print(f"{first_number} {operator} {next_number} = {result}")

        if input("Do you want to continue calculating? Type 'yes' or 'no'\n") == "yes":
          first_number = result
        else: 
            recalculate = False
            print("\033c")
            calculator()
        
        
calculator()