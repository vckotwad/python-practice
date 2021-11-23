#program to find each vowel present inside a word
word=input('please enter a word')
lv=['a','e','i','o','u']
l=[x for x in lv if (x in word )]
print("vowel present inside the words are ",l)