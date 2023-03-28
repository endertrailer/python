sentence = input("enter a sentence: ")
sentence2 = input("enter another sentence: ")
error = 0
sentence_1 = sentence.split()
sentence_2 = sentence2.split()
try:
    if len(sentence_1) > len(sentence_2):
        for i in range(len(sentence_1)):
            if sentence_1[i] != sentence_2[i]:
                error = error + 1
    else:
        for i in range(len(sentence_2)):
            if sentence_1[i] != sentence_2[i]:
                error = error + 1
    print(f"there are {error} errors")
except IndexError:
    print("the sentences have to be the same length")
