#!/usr/bin/env python3

def my_program():
    from path import Path
    pwd_path = Path("./NewDir")
    if not pwd_path.isdir():
        pwd_path.mkdir()
    pwd_path = pwd_path / "file.txt"
    if not pwd_path.isfile():
        pwd_path.touch()
    pwd_path.write_text("Writing some_line")
    for line in pwd_path.lines():
        print(line)

if __name__ == '__main__':
    my_program()
