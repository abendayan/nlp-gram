from collections import defaultdict
import random

"""
Adele Bendayan 336141056
"""

class PCFG(object):
    def __init__(self):
        self._rules = defaultdict(list)
        self._sums = defaultdict(float)

    def add_rule(self, lhs, rhs, weight):
        assert(isinstance(lhs, str))
        assert(isinstance(rhs, list))
        self._rules[lhs].append((rhs, weight))
        self._sums[lhs] += weight

    @classmethod
    def from_file(cls, filename):
        grammar = PCFG()
        with open(filename) as fh:
            for line in fh:
                line = line.split("#")[0].strip()
                if not line: continue
                w,l,r = line.split(None, 2)
                r = r.split()
                w = float(w)
                grammar.add_rule(l,r,w)
        return grammar

    def is_terminal(self, symbol): return symbol not in self._rules

    def gen(self, symbol, tree):
        if self.is_terminal(symbol):
            if tree:
                start = " "
            else:
                start = ""
            return start + symbol
        else:
            expansion = self.random_expansion(symbol)
            if tree:
                start = "(" + symbol + " "
                end = ")"
            else:
                start = ""
                end = ""
            return start + " ".join(self.gen(s, tree) for s in expansion) + end

    def random_sent(self, number_phrases, tree):
        list_phrases = []
        # generate multiple phrases if ask for
        for i in range(number_phrases):
            list_phrases.append(self.gen("ROOT", tree))
        return list_phrases

    def random_expansion(self, symbol):
        """
        Generates a random RHS for symbol, in proportion to the weights.
        """
        p = random.random() * self._sums[symbol]
        for r,w in self._rules[symbol]:
            p = p - w
            if p < 0: return r
        return r


if __name__ == '__main__':

    import sys
    pcfg = PCFG.from_file(sys.argv[1])
    number_phrases = 1
    if "-n" in sys.argv:
        index_n = sys.argv.index("-n")
        number_phrases = int(sys.argv[int(index_n) + 1])
    tree = "-t" in sys.argv
    list_phrases = pcfg.random_sent(number_phrases, tree)
    for phrase in list_phrases:
        print phrase
