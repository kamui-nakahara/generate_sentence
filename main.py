from janome.tokenizer import Tokenizer
from random import choice
import json
import sys
def load():
    f=open("words.json",mode="rt",encoding="utf-8")
    return json.load(f)
def write():
    f=open("words.json",mode="wt",encoding="utf-8")
    json.dump(data,f,ensure_ascii=False,indent=2)
    f.close()
def learn(sentence):
    global data
    tokens=[str(token) for token in t.tokenize(sentence)]
    if "start" in data["words"]:
        data["words"]["start"].append(tokens[0])
    else:
        data["words"]["start"]=[tokens[0]]
    for i,token in enumerate(tokens):
        if token in data["words"]:
            if i==len(tokens)-1:
                if not "end" in data["words"][token]:
                    data["words"][token].append("end")
            else:
                if not tokens[i+1] in data["words"][token]:
                    data["words"][token].append(tokens[i+1])
        else:
            if i==len(tokens)-1:
                data["words"][token]=["end"]
            else:
                data["words"][token]=[tokens[i+1]]
def generate():
    sentence=""
    token=choice(data["words"]["start"])
    sentence+=token.split("\t")[0]
    while True:
        token=choice(data["words"][token])
        if token=="end":
            break
        sentence+=token.split("\t")[0]
    return sentence
data=load()
t=Tokenizer()
if len(sys.argv)==1:
    while True:
        sentence=input(">")
        if not sentence:
            break
        learn(sentence)
        sentence=generate()
        print(sentence)
elif len(sys.argv)==2:
    if sys.argv[1]=="l":
        while True:
            sentence=input(">")
            if not sentence:
                break
            learn(sentence)
    elif sys.argv[1]=="g":
        times=input("出力回数>")
        for i in range(int(times)):
            sentence=generate()
            print(sentence)
write()
