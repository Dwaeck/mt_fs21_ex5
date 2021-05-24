from sacremoses import MosesTokenizer
import argparse

mt = MosesTokenizer
parser = argparse.ArgumentParser()

parser.add_argument('--file',type=str,required=False)
args = parser.parse_args()

x = open(args.file,'r',encoding="UTF-8")
y = open(args.file+'tokenized','w',encoding="UTF-8")

a = 0
for x in args.file:
    if a < 100000:
        y.write(mt.tokenize(x))
        a += 1
    else:
        break
