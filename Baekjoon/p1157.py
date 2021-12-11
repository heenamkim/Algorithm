#1157 단어공부 브론즈1

word = input()
word = word.upper()

alp_list = []
alp_count = []

max_count = 0
result = 0

for upper_alp in range(65, 91):
    alp_list.append(chr(upper_alp))
    alp_count.append(0)

for word_alp in word:
    for alp_index, alp in enumerate(alp_list):
        if word_alp == alp:
            alp_count[alp_index] += 1

max_count = max(alp_count)


for count in alp_count:
    if count == max_count:
        result += 1

if result >= 2 :
    print('?')
else:
    print(alp_list[alp_count.index(max(alp_count))])

