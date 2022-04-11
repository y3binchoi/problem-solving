def d(_n):  # 생성자 n
    return _n + sum(map(int, str(_n)))


self_nums = [1 for _ in range(10000)]  # self num 이면 1 아니면 0
for n in range(10000):
    x_self = d(n)  # self num 가 아님
    if x_self < 10000 and self_nums[x_self - 1]:
        self_nums[x_self - 1] = 0
for n in range(10000):
    if self_nums[n]:
        print(n + 1)
