#2941 크로아티아 알파벳 실버5

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
result = 0

for i in range(len(word)):
    for alp in word:
        cro_alp = ''
        cro_alp += alp
        print(cro_alp[0])
        if cro_alp[0] == 'c' or 'd' or 'l' or 'n' or 's' or 'z':
            for j in cro:
                if cro_alp == cro:
                    result += 1
                    cro_alp = ''
                else:
                    pass
        else:
            result += 1
            cro_alp = ''
        

print(result)




