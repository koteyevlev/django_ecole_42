#!/usr/bin/env python3

def get_capital_city(state):
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
        return capital_cities[short_states]
    else:
        return False


def get_state(capital_city):
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
        return list(states.keys())[list(states.values()).index(short_states)]
    else:
        return False


def all_in(argv):
    if len(argv) == 2:
        input_list = argv[-1].split(",")
        for raw_element in input_list:
            element = raw_element.title().strip()
            if raw_element.isspace():
                continue
            city = get_capital_city(element)
            state = get_state(element)
            if city:
                print(city, "is the capital of", element)
            elif state:
                print(element, "is the capital of", state)
            else:
                print(raw_element.strip(), "is neither a capital city nor a state")


if __name__ == '__main__':
    import sys
    all_in(sys.argv)
