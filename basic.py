from sys import * 

tokens = []

def open_file(filename):
    data = open(filename, "r").read()
    return data

def lex(filecontents):
    tok = ""
    state = 0
    string = ""

    filecontents = list(filecontents)

    for char in filecontents:
        tok += char
        if tok == " ": # ignoring spaces and separating words after spaces
            if state == 0:
                tok = ""
            else:
                tok = " "
        elif tok == "\n":
            tok = ""
        elif tok == "comeonprintalready": # print go brr 
            tokens.append("PRINT")
            tok = ""
        elif state == 0 and tok == "[\"":
            state = 1
        elif state == 1 and tok == "')": # man this was so painful to figure out
            tokens.append("STRING:" + string + "')")
            tok = ""
            state = 0
            string = ""
        elif state == 1: 
            if tok == "'": # what am i doing with my life 
                pass
            else:
                string += tok
                tok = ""
    # print(tokens)
    return tokens

def parse(toks):
    i = 0
    while(i < len(toks)):
        if toks[i] + " " + toks[i+1][0:6] == "PRINT STRING":
            print(toks[i+1][9:-2])
            i += 2

def run():
    data = open_file(argv[1])
    toks = lex(data)
    parse(toks)

run()