import re

class MorphologicalAnalyzer:
    def __init__(self):
        
        self.suffix_rules = [
            (r'(.*)(ing)$', 'VBG'),
            (r'(.*)(ed)$', 'VBD'),
            (r'(.*)(S)$', 'NNS'),
            (r'(.*)(ly)$', 'RB'),
            (r'(.*)(able| ible)$', 'JJ'),
            (r'(.*)(ness)$', 'NN'),
            (r'(.*)(ment)$', 'NN'),
            (r'(.*)(er| or)$', 'NN'),
            (r'(.*)(ion)$', 'NN'),
            (r'(.*)(al|ial)$', 'JJ'),
            (r'(.*)(y)$', 'JJ'),
            (r'(.*)(ive)$', 'JJ'),
        ]
        self.preffix_rule = [
            (r'(un)(.*)', 'JJ'),
            (r'(re)(.*)', 'VB'),
            (r'(dis)(.*)', 'VB'),
            (r'(in|im|il|ir)(.*)', 'JJ'),
        ]

    def analyze(self, word):
        analyze = {'word': word, 'root': word, 'affix': None, 'pos': None}

        for pattern, pos in self.suffix_rules:
            match = re.match(pattern, word)
            if match:
                analyze['root'] = match.group(1)
                analyze['affix'] = match.group(2)
                analyze['pos'] = pos
                return analyze
            
        for pattern, pos in self.preffix_rule:
            match = re.match(pattern, word)
            if match:
                analyze['root'] = match.group(2)
                analyze['affix'] = match.group(1)
                analyze['pos'] = pos
                return analyze
            
        return analyze
    
analyzer = MorphologicalAnalyzer()

words = ['rewind', 'disapprove', 'cats', 'readable']

for word in words:
    result = analyzer.analyze(word)
    print(result)