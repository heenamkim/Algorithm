'''
keypad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ['*', 0, '#']]


def solution(numbers, hand):
    
    answer = ''
    for num in numbers:
        if num == 1 or 4 or 7:
            answer += L
        elif num == 3 or 6 or 9:
            answer += R
            
    return answer


'''
a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print('*', end='')
    print()
