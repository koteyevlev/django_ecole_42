#!/usr/bin/env python3
from settings import *


def replace_variable(input_file):
    """
    replace on global variable in html
    :param input_file: file
    :return: string
    """
    input_html = input_file.read()
    input_file.close()
    return input_html.format_map(globals())


def render():
    """
    render html from template
    :return:
    """
    import sys
    argv = sys.argv
    if len(argv) != 2:
        return
    input_file = open(argv[1], "r")

    content = replace_variable(input_file)

    output_file = open(argv[1][:-9] + ".html", "w")
    output_file.write(content)
    output_file.close()


if __name__ == '__main__':
    render()
