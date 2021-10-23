# 브론즈1
# 단어공부
input_word = input().upper()

if 1000000 >= len(input_word) and 0 < len(input_word) :
    list_word = list(input_word)
    list_alphabet=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    cnt_word = {}
    for alphabet in list_alphabet:
        cnt_word[alphabet] = 0

    for word in list_word:
        chk = False
        for key in cnt_word.keys() :
            if key == word: 
                chk = True 
                break

        if chk: cnt_word[word] += 1

    print_word = ""
    max_word = 0
    for key in cnt_word.keys() :
        if max_word < cnt_word[key] and cnt_word[key] != 0:
            max_word = cnt_word[key]
            print_word = key
        elif max_word == cnt_word[key] and cnt_word[key] != 0: print_word = "?"

    print(print_word)

#2
word = input().upper()
list_alphabet=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
numlist=[]

for s in alphabet:
    numlist.append(word.count(s))

maxnum=max(numlist)
if(maxnum!=0):
    if(numlist.count(maxnum)>1):
        print('?')
    else:
        print(chr(numlist.index(maxnum) + 65))

