n = int(input())
m = 1000 - n
#print(m)
count =0

list = [500,100,50,10,5,1]
for coin in list:
    count += m // coin
    m %= coin

print(count)