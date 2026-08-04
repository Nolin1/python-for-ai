def greet(name):
    print(f"Hello this is {name}")
    pass

greet(name="Nolin")

def check_weather(temp):
    if temp < 0 :
        print("it's too cold.")
    elif temp < 25:
        print("It's great weather.")
    else:
        print("It's hot.")


check_weather(temp = float(input("Enter temp: ")))

#function return

numbers = [2,4,6,7,3,1]

def first_and_last_number(list):
    first = list[0]
    last = list[-1]
    return first, last

first_number , last_number = first_and_last_number(numbers)
print(first_number)
print(last_number)