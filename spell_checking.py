

import re 
import collections
from functools import cmp_to_key 
from itertools import product 


class SpellChecker(object):

    def __init__(self, file_name):
        self.vowels = set('aeiouy')
        self.alphabet = set('abcdefghijklmnopqrstuvwxyz')
        self.language_model, self.real_words = self.get_language_model(file_name)
   
    def get_language_model(self, file_name):
        
        language_model = collections.defaultdict(lambda: 0) 

        with open(file_name) as file :
            txt = file.read()

        words =  re.findall('\w+', txt.lower()) 

        for word in words:
            language_model[word] += 1
        
        real_words = set(language_model) 
        return language_model, real_words 
    
    def add_word(self, word):
        self.real_words.add(word) 

    def variants1(self, word):
        """get all possible variants for a word"""
        splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes    = [a + b[1:] for a, b in splits if b]
        transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
        replaces   = [a + c + b[1:] for a, b in splits for c in self.alphabet if b]
        inserts    = [a + c + b for a, b in splits for c in self.alphabet]
        return set(deletes + transposes + replaces + inserts)

    def variants2(self, word):
        """get variants for the variants for a word"""
        return set(s for w in self.variants1(word) for s in self.variants1(w))

    def suggestions(self, word ) : 
        return self.variants1(word) & self.real_words or \
               self.variants2(word) & self.real_words or \
               {word} 

    def check(self, word) :
        if word in self.real_words :
            return True, word 
        
        return False, self.suggestions(word) 




if __name__ == "__main__":
    
    spell_checker = SpellChecker('data/big.txt') 
    
    test = ['hi', 'monster', 'gad', 'minster', 'try', 'gad'] 

    for word in test : 
        flag, suggestions = spell_checker.check(word) 
        if flag : 
            print("word {} is correct".format(word))
        else :
            print("word {} is not correct. suggestions are:{}".format(word, suggestions))
            spell_checker.add_word(word) 