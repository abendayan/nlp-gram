import nltk
from nltk import parse
import sys

def is_terminal(token):
 return token not in left_parts

"""prepare grammar input for nltk grammar format."""


f = open(sys.argv[1], "r")
lines = f.readlines()
f2 = open("grammar.cfg", "w")

lines = [line.split("#")[0].strip() for line in lines]
lines = [line for line in lines if line]
left_parts = [line.split(None, 2)[1] for line in lines]

for line in lines:

        w,l,r = line.split(None, 2)
	r_elements = r.split(None)
        right_side = ""
	for r in r_elements:
		if is_terminal(r):
			right_side+="'"+r+"' "
		else:
			right_side+=" "+r

		right_side  = right_side.strip()
	line =  l + " -> "+right_side
	f2.write(line+"\n")
f2.close()
f.close()



"""testing """


g = nltk.data.load("grammar.cfg")

parser = nltk.ChartParser(g)

lines = open(sys.argv[2]).readlines()
sentences = [line.split("#")[0].strip() for line in lines]

for s in sentences:
 if not s: continue
 tokens = s.split()
 tree = list(parser.parse(tokens))
 if tree: print "parsed sentence", s  #print tree[0]
 else: print "Cannot parse sentence",s

