#!/usr/bin/python

def get_number():
    while True:
        try:
            num = int(input("Number: "))
            return num
        except:
            print("Please enter a number!\n")

def is_odd_check(num):
    is_odd = num % 2
    return is_odd

def print_message(num, odd):
    if odd == 0:
        print(f'{num} is even!\n')
    if odd == 1:
        print(f'{num} is odd!\n')

if __name__ == '__main__':
    print("Enter a number to see if it is even or odd! Enter 0 to quit.")
    while True:
        num = get_number()
        if num == 0:
            print("Goodbye!")
            break
        else:
            is_odd = is_odd_check(num)
            print_message(num, is_odd)
