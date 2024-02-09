alp = ' abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'

f = open("secret.txt")
text = f.read()

lines = text.split("\n")
for line in lines:
    cnt = 0
    for j in line:
        if j in vowels:
            cnt += 1
    print(alp[cnt], end="")






