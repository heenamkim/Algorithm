#4344 평균은 넘겠지 브론즈1

student = int(input())

for i in range(student):
    score = list(map(int, input().split()))
    total = 0
    ave = (sum(score[1:]))/score[0]
    print(ave)
    people = 0
    for k in score:
        if ave < k:
            people += 1
        else:
            continue
        
    print("%.3f%%"%((people/score[0])*100))
 
