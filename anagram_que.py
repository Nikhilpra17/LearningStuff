# https://www.programiz.com/python-programming/examples/anagram

word1="Race"
word2="care"
# length of word1 == length of word2
# check CHARACTERS of word1 exists in word2


def check_anagram(word_1,word_2):
    conclusion=True
    if len(word1) == len(word2):
        for char in word1:
            if char not in word2:
                conclusion=False
    else:
        conclusion=False            
    print(f' Word1 and Word2 are anagram: {conclusion}')       
check_anagram(word1,word2)
        

