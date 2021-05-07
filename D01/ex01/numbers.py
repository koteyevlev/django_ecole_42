#!/usr/bin/env python3

def numbers():
    with open("numbers.txt", "r") as num_file:
        number_list = num_file.read().split(',')
        for number in number_list:
            print(number.strip())


if __name__ == '__main__':
    numbers()
