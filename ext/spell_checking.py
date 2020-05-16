

import re 
import collections
from functools import cmp_to_key 
from itertools import product 


def get_language_model(file_name):
    
    language_model = collections.defaultdict(lambda: 0) 

    with open(file_name) as file :
        txt = file.read()

    words =  re.findall('\w+', txt.lower()) 

    for word in words:
        language_model[word] += 1
    
    real_words = set(language_model) 
    return language_model, real_words 
    

def suggestions(word, real_words ) : 
    





if __name__ == "__main__":
    language_model, real_words = get_language_model('data/small.txt')

    print("language_model:", language_model)
    print("real_words:", real_words,'\n')  

    suggestions('the', real_words) 