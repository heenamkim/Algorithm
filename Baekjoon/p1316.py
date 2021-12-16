#1316 그룹단어 체커 실버5

number = int(input())
count = 0
alp = []

for i in range(97, 123):
    alp.append(chr(i))
print(alp)

for i in range(number):
    word = input()
    alp_list = []
    for alp in word:
        alp_list.append(i)
    
                
        
        
