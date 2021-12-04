#1152 단어의 개수 브론즈2


word = input()

word_num = 0

word = word.split()

for i in word:
    word_num += 1

print(word_num)
