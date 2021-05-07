#!/usr/bin/env python3

def get_valid_link(links):
    for i in range(len(links)):
        link = links[i].get('href')
        if link[0] == "#" or "/wiki/Help" in link or "/wiki/File" in link or "//upload.wikimedia" in link:
            continue
        else:
            return link
    return None


def valid_link(info_candidate):
    links = info_candidate.find_all('a')
    if get_valid_link(links):
        return True
    return False


def roads_to_philosophy():
    import sys, requests
    from bs4 import BeautifulSoup

    argv = sys.argv
    if len(argv) != 2:
        return
    link = "/wiki/" + argv[1]
    if argv[1] == "Philosophy":
        print(0, "roads from", argv[1], "to philosophy !")
    headers = []

    while True:
        req = requests.get("https://en.wikipedia.org" + link)
        if req.status_code != 200 or not req.text:
            print("Something wrong. Status code -", req.status_code)
            return
        parsed = BeautifulSoup(req.text, 'html.parser')
        header = parsed.body.find_all("h1", {"class": "firstHeading"})[0].text
        if header not in headers:
            headers.append(header)
        else:
            print("It leads to an infinite loop !")
            return
        info_all = parsed.body.find_all("div", {"class": "mw-parser-output"})[0].find_all("p", {"class": None})
        info = info_all[0]
        for info_candidate in info_all:
            try:
                if info_candidate.parent.attrs["class"][0] == "mw-parser-output":
                    if valid_link(info_candidate):
                        info = info_candidate
                        break
            except Exception as e:
                print("It leads to a dead end !")
                return
        links = info.find_all('a')
        if len(links) == 0:
            print("It leads to a dead end !")
            return
        new_link = get_valid_link(links)
        #print(new_link)
        link = new_link
        if header == "Philosophy":
            break
    for road in headers:
        print(road)
    print(len(headers), "roads from", argv[1], "to philosophy !")


if __name__ == '__main__':
    roads_to_philosophy()
