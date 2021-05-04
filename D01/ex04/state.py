#!/usr/bin/env python3

def state(argv):
    if len(argv) == 2:
        capital_city = argv[1]
        states = {
            "Oregon": "OR", "Alabama": "AL",
            "New Jersey": "NJ",
            "Colorado": "CO"
        }
        capital_cities = {
            "OR": "Salem",
            "AL": "Montgomery",
            "NJ": "Trenton",
            "CO": "Denver"
        }
        if capital_city in capital_cities.values():
            short_states = list(capital_cities.keys())[list(capital_cities.values()).index(capital_city)]
            print(list(states.keys())[list(states.values()).index(short_states)])
        else:
            print("Unknown capital city")


if __name__ == '__main__':
    import sys
    state(sys.argv)
