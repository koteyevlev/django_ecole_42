#!/usr/bin/env python3

def request_wiki():
    import sys, json, requests
    from dewiki import parser
    argv = sys.argv
    if len(argv) != 2:
        return
    req = requests.get("https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&meta=&continue=&titles=" +
                       argv[1] + "&rvprop=content")
    if req.status_code != 200 or not req.text:
        print("Something wrong")
        return
    pars = parser.Parser()
    try:
        output = json.loads(req.text)
        key = list(output["query"]["pages"].keys())[0]
        content = (output["query"]["pages"][key]["revisions"][0]["*"])
        output_file = open(argv[1] + ".wiki", "w")
        output_file.write(pars.parse_string(content).strip())
        output_file.close()
    except Exception as e:
        print("some problem with answer", e)


if __name__ == '__main__':
    request_wiki()
