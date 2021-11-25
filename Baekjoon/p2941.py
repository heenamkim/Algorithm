#2941 크로아티아 알파벳 실버5

alp = input()
ea = 0

for i in alp:
    if i == 'c':
        if [i+1] == '=':
            ea += 1
        elif [i+1] == '-':
            ea += 1
    elif i == 'd':
        if [i+1] == 'z':
            if [i+2] == '=':
                ea += 1
        elif [i+1] == '-':
            ea += 1
    elif i == 'l':
        if [i+1] == 'j':
            ea += 1
    elif i == 'n':
        if [i+1] == 'j':
            ea += 1
    elif i == 's':
        if  [i+1] == '=':
            ea += 1
    elif i == 'z':
        if [i+1] == '=':
            ea += 1
    else:
        ea += 1
            


print(ea)
