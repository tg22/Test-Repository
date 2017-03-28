"""This function uses the textblob library to paraphrase, spellcheck, translate and write sentences into a plain text file. The function is not perfect but it does check that the root of two words
are not the same so as to avoid redundancy. overall 9/10 function would use again."""

# coding: utf-8


#
# hw6 problem 3
#

## Problem 3: Paraphrasing!
import nltk
from textblob import TextBlob
from textblob import Word



# A starter function that substitutes each word with it's top match
#   in word2vec.  Your task: improve this with POS tagging, lemmatizing, 
#   and/or at least three other ideas of your own (more details below)
#

import gensim
import gensim.models

def read_word2vec_model():  
    """ a function that reads a word2vec model from the file
        "word2vec_model.txt" and returns a model object that
        we will usually name m or model...
    """
    file_name = "word2vec_model.txt"
    from gensim.models.word2vec import Word2Vec
    m = gensim.models.KeyedVectors.load_word2vec_format(file_name, binary=False)
    print("The model built is", m)
    ## The above line should print
    ## Word2Vec(vocab=43981, size=300, alpha=0.025)
    ## which tells us that the model represents 43981 words with 300-dimensional vectors
    ## The "alpha" is a model-building parameter called the "learning rate."
    ##   Once the model is built, it can't be changed without rebuilding it; we'll leave it.  
    return m
#from nltk.stem.wordnet import WordNetLemmatizer

def paraphrase_sentence( sentence, m):
    """ paraphrase_sentence's docstring - be sure to include it!
    """
    response = input("suh, would you like to turn spellcheck on? (y/n)")
    response2 = input('would you like to translate your text (no/en/es/cn/fr')
    blob = TextBlob( sentence )
    if response=='y':
        blob = blob.correct()
    print("The sentence's words are")
    if response2 != 'no':
        blob = blob.translate(to=response2)
    LoW = blob.words
    print(LoW)
    
    NewLoW = []
    print (LoW)
    for w in LoW:
        t = False
        if w not in model:
            NewLoW += [w]
        else:
            w_alternatives = model.most_similar(positive=[w], topn=100)
            for n in range(len(w_alternatives)):
                if t == False:
                    # print("w_alternatives is", w_alternatives)
                    first_alternative, first_alternative_score = w_alternatives[n]
                    unlmt = Word(first_alternative)
                    lmt = unlmt.lemmatize()
                    unlmtw = Word(w)
                    lmtw = unlmtw.lemmatize()
                    if lmt != lmtw:
                        NewLoW += [first_alternative]
                        print("Added a new word!")
                        break
                    
                         
                    
                    
                    



    
    # you should change this so that it returns a new string (a new sentence),
    # NOT just print a list of words (that's what's provided in this starter code)
    para = ' '.join(NewLoW)
    return para  # this is a new low!


# 
# Once the above function is more sophisticated (it certainly does _not_ need to be
#   perfect -- that would be impossible...), then write a file-paraphrasing function:
#
def paraphrase_file(filename, m):
    """ paraphrase_file's docstring - be sure to include it!
    """
    # tokenize with textblob - first create a blob...
    k = open(filename, "r")
    orig_text = k.read()
    blob1 = TextBlob( orig_text )
    print(blob1)
    k.close()
    print("Tokenizing with textblob:")
    print("Words:")
    print( blob1.words )
    print("Sentences:")
    print( blob1.sentences )
    sent= blob1.sentences 
    text = ''
    #for x in range(len(sent)):
    text = paraphrase_sentence(blob1.string, m)
    
    name_of_file = 'test_paraphrased.txt'
    f= open(name_of_file, "w")
    f.write(text)
    f.close()
    return

"""examples
Original: There is a shark in the water
Not Successful: There was a sharpest where this water
Original: The car drove fast    
V Successful: The vehicle sped quick
Original: the mitochondria is the powerhouse of the cell
Paraphrased: 'this mitochondria was this poorhouse of this Cell'
Original: 'I was like baby, baby, baby ooooh'
Paraphrased (THIS IS HILARIOUS LMAO): 'myself is really newborn newborn newborn oooh'

        



#
# Results and commentary...
#


# (1) Try paraphrase_sentence as it stands (it's quite bad...)  E.g.,
#         Try:    paraphrase_sentence("Don't stop thinking about tomorrow!", m)
#         Result: ['Did', "n't", 'stopped', 'Thinking', 'just', 'tonight']

#     First, change this so that it returns (not prints) a string (the paraphrased sentence),
#         rather than the starter code it currently has (it prints a list) Thus, after the change:

#         Try:    paraphrase_sentence("Don't stop thinking about tomorrow!", m)
#         Result: "Did n't stopped Thinking just tonight"  (as a return value)

#     But paraphrase_sentence is bad, in part, because words are close to variants of themselves, e.g.,
#         + stop is close to stopped
#         + thinking is close to thinking
"""
            
    
"""


# (2) Your task is to add at least three things that improve this performance (though it
#     will necessarily still be far from perfect!) Choose at least one of these two ideas to implement:

#     #1:  Use lemmatize to check if two words have the same stem/root - and _don't_ use that one!
#             + Instead, go _further_ into the similarity list (past the initial entry!)
#     #2:  Use part-of-speech tagging to ensure that two words can be the same part of speech

#     Then, choose two more ideas that use NLTK, TextBlob, or Python strings -- either to guard against
#     bad substitutions OR to create specific substitutions you'd like, e.g., just some ideas:
#        + the replacement word can't have the same first letter as the original
#        + the replacement word is as long as possible (up to some score cutoff)
#        + the replacement word is as _short_ as possible (again, up to some score cutoff...)
#        + replace things with their antonyms some or all of the time
#        + use the spelling correction or translation capabilities of TextBlob in some cool way
#        + use as many words as possible with the letter 'z' in them!
#        + don't use the letter 'e' at all...
#     Or any others you might like!





# (3) Share at least 4 examples of input/output sentence pairs that your paraphraser creates
#        + include at least one "very successful" one and at least one "very unsuccessful" ones






# (4) Create a function paraphrase_file that opens a plain-text file, reads its contents,
#     tokenizes it into sentences, paraphrases all of the sentences, and writes out a new file
#     containing the full, paraphrased contents with the word paraphrased in its name, e.g.,
#        + paraphrase_file( "test.txt", model )
#             should write out a file names "test_paraphrased.txt"  with paraphrased contents...
#        + include an example file, both its input and output -- and make a comment on what you
#             chose and how it did! 











# (Optional EC) For extra-credit (up to +5 pts or more)
#        + [+2] write a function that takes in a sentence, converts it (by calling the function above) and
#          then compares the sentiment score (the polarity and/or subjectivity) before and after
#          the paraphrasing
#        + [+3 or more beyond this] create another function that tries to create the most-positive or
#          most-negative or most-subjective or least-subjective -- be sure to describe what your
#          function does and share a couple of examples of its input/output...






