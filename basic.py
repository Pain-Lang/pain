from sys import *

tokens = []
temp = 0


def open_file(filename):
    data = open(filename).read()
    return data


def lex(filecontents):
    contains_start = False
    contains_end = False
    tok = ""
    state = 0
    string = ""

    filecontents = list(filecontents)

    for char in filecontents:
        tok += char
        if tok == "---whydidistart---":
            contains_start = True
            tok = ""
        elif tok == "---omgifinished---":
            contains_end = True
            tok = ""
        elif tok == " ":  # ignoring spaces and separating words after spaces
            if state == 0:
                tok = ""
            else:
                tok = " "
        elif tok == "\n":
            tok = ""

        if tok == "comeonsumalready":
            tokens.append("SUM")
            tok = ""
        elif state == 0 and tok == "[":
            state = 1
        elif state == 1 and tok == ")":
            tokens.append("NUM: " + string + ")")
            tok = ""
            state = 0
            string = ""

        if tok == "comeonprintalready":  # print go brr
            tokens.append("PRINT")
            tok = ""
        elif state == 0 and tok == "[\"":
            state = 1
        elif state == 1 and tok == "')":  # man this was so painful to figure out
            tokens.append("STRING:" + string + "')")
            tok = ""
            state = 0
            string = ""
        elif state == 1:
            if tok == "'":  # what am i doing with my life
                pass
            else:
                string += tok
                tok = ""

    if not contains_start:
        raise SyntaxError("Start statement not provided.")
    if not contains_end:
        raise SyntaxError("End statement not provided.")

    print(tokens)
    return tokens


def parse(toks):
    temp2 = 6
    temp3 = ""
    temp4 = ""
    i = 0
    while(i < len(toks)):
        try:
            if toks[i] + " " + toks[i+1][0:3] == "SUM NUM":
                while True:
                    try:
                        if toks[i+1][temp2] == ",":
                            break
                    except:
                        break
                    temp3 += toks[i+1][temp2]
                    temp2 += 1

                temp2 += 2

                while True:
                    try:
                        if toks[i+1][temp2] == ",":
                            break
                    except:
                        break
                    temp4 += toks[i+1][temp2]
                    temp2 += 1

                temp = float(temp3) + float(temp4[:-1])
                i += 2
        except:
            pass

        try:
            if toks[i] + " " + toks[i+1][0:6] == "PRINT STRING":
                print(toks[i+1][9:-2])
                i += 2
        except:
            pass


def run():
    data = open_file(argv[1])
    toks = lex(data)
    parse(toks)


run()
