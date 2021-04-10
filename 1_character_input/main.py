#!/usr/bin/env

def get_name_age():
    name = input("Enter your name: ")
    if name == 'quit':
        return False
    age = int(input("Enter your age: "))
    return (name, age)

def years_to_100(age):
    years = 100 - age
    return years

def send_message(name_age):
    print(f'Hello, {name_age[0]}')
    print(f'You will turn 100 in {years_to_100(name_age[1])} years!\n')

if __name__ == '__main__':
    while True:
        name_age = get_name_age()
        if name_age:
            send_message(name_age)
        else:
            print("Goodbye!")
            break
