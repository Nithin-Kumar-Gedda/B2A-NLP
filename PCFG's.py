import nltk
from nltk.corpus import treebank
from nltk import Nonterminal

productions = []

for t in treebank.fileids()[:2]:
    for x in treebank.parsed_sents(t):
        productions += x.productions()

print(productions)

s = Nonterminal('S')

grammer = nltk.induce_pcfg(s,productions)
print(grammer)

productions = []
for t in treebank.fileids()[:2]:
    for x in treebank.parsed_sents(t):
        x.collapse_unary(collapsePOS = False)
        x.chomsky_normal_form(horzMarkov = 2)
        productions += x.productions()
grammer = nltk.induce_pcfg(s, productions)
print(grammer)

parser = nltk.pchart.InsideChartParser(grammer)
parser.trace(3)
sent = treebank.parsed_sents('wsj_0001.mrg')[0].leaves()

for parse in parser.parse(sent):
    print(parse)