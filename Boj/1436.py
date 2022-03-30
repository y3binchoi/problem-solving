N = int(input())
num_of_death = 665
count = 0
while count < N:  # count==N, 즉 N번째 종말의 숫자를 찾으면 멈춤
    num_of_death += 1
    if str(num_of_death).find('666') != -1:  # '666'이 포함된 숫자=종말의 숫자
        count += 1
print(num_of_death)
