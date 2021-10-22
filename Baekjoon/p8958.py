#8958 OX퀴즈 브론즈2

test_num = int(input())

for i in range(test_num):
    quiz_num = input()
    quiz = list(quiz_num)
    total = 0
    num = 1
    for j in quiz:
        if j == 'O':
            total += num
            num += 1
        else:
            num = 1
    print(total)
