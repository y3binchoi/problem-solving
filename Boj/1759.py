# 1759. 암호 만들기
from itertools import combinations
from sys import stdin


input = stdin.readline
L, C = map(int, input().split())
letters = list(input().split())
letters.sort()
# print(letters)
passwords = list(combinations(letters, L))
# print(*passwords,sep='\n')
vowels = ('a', 'e', 'i', 'o', 'u')
for pwd in passwords:
    vowel_count = 0
    for i in pwd:
        if i in vowels:
            vowel_count += 1
    if 1 <= vowel_count <= L-2:
        print(''.join(pwd))
    
