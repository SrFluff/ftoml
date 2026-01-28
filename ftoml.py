import os
import sys

def read(file="example.toml"):

    stream = []
    f = open(file,"r")
    for i in f:
        stream.append(i.strip().replace(" = ","=").replace(" =","=").replace("= ","="))

    out = []
    outMap = []

    scope = "[general]"

    for i in stream:
        if len(i) == 0:
            continue
        if i[0] == "[" and i[len(i)-1] == "]":
            scope = i
        if not scope in outMap:
            outMap.append(scope)
            out.append([])
        if "=" in i:
            j = i
            k = i
            while k[0] != "=":
                k = k[1:]
            k = k[1:]
            if k[0] == '"' or k[0] == "'":
                k = k[1:-1]
            elif k == "true" or k == "false":
                if k == "true":
                    k = True
                else:
                    k = False
            elif not "'" in k or not '"' in k:
                if not k == "true" or not k == "false":
                    if "." in k:
                        k = float(k)
                    else:
                        k = int(k)
            while j[len(j)-1] != "=":
                j = j[0:-1]
            j = j[0:-1]
            out[outMap.index(scope)].append([j,k])

    return (outMap,out)
