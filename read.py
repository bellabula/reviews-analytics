# iput 留言資料
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 10000 == 0:
            print(len(data))
print('檔案中總共有', len(data), '筆資料')

# 留言平均長度
sum_len = 0
for c in data:
    sum_len += len(c)
avg_len = sum_len/len(data)
print('所有留言的平均長度為', avg_len)

# 留言長度 < 100
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('總共有',len(new), '筆留言長度小於100')