# ex1
def wordlist_count(dictionary):
    wordcount = {}
    for word in dictionary:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    for key in wordcount.keys():
        print( "{}:{}".format( key, wordcount[key] ) )
    
wordlist = ["apple","durian","banana","durian","apple","cherry",
"cherry","mango","apple","apple","cherry","durian","banana",
"apple","apple","apple","apple","banana","apple"]
wordlist_count(wordlist)    

#ex2
text = "apple,durian,banana,durian,apple,cherry,cherry,mango," + \
"apple,apple,cherry,durian,banana,apple,apple,apple," + \
"apple,banana,apple"

counts = {}
for word in text.split(","):
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

for key, value in counts.items():
    print(key, value)
# ex3
english_dutch = {
    "last":"laatst", "week":"week", "the":"de",
    "royal":"koninklijk", "festival":"feest", "hall":"hal", "saw":"zaag",
    "first":"eerst", "performance":"optreden", "of":"van",
    "a":"een", "new":"nieuw", "symphony":"symphonie", "by":"bij",
    "one":"een", "world":"wereld", "leading":"leidend", "modern":"modern",
    "composer":"componist", "composers":"componisten",
    "two":"twee", "shed":"schuur", "sheds":"schuren"
}

sentence = "Last week The Royal Festival Hall saw the first performance of a new symphony by one of the world's leading modern composers, Arthur \"Two-Sheds\" Jackson."

words = sentence.lower().split()
translated_words = [english_dutch.get(word, word) for word in words]

translated_sentence = " ".join(translated_words)

print(translated_sentence)
