#!/usr/bin/env python3

def capital_city(argv):
    if len(argv) == 2:
        state = argv[1]
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
        if state in states:
            short_states = states[state]
            print(capital_cities[short_states])
        else:
            print("Unknown state")


if __name__ == '__main__':
    import sys
    capital_city(sys.argv)

