#10809 알파벳 찾기 브론즈2

s = input()
for i in range(97, 123):
    print(s.find(chr(i)), end=' ')

