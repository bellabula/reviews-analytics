# iput 留言資料
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        # if count % 10000 == 0:
        #     print(len(data))
print('檔案中總共有', len(data), '筆資料')

# 留言平均長度
sum_len = 0
for d in data:
    sum_len += len(d)
avg_len = sum_len/len(data)
print('所有留言的平均長度為', avg_len)

# 留言長度 < 100
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('總共有',len(new), '筆留言長度小於100')


# 含有good的留言
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('總共有',len(good), '筆留言提到"good"')
# list comprehension
good_c = [d for d in data if 'good' in d]
print(len(good_c))

# 留言中是否含有'bad', True Fales
bad = ['bad' in d for d in data]
print('總共有',sum(bad), '筆留言中包含"bad"')


# word count
word_count = {}

for d in data:
    words = d.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

for word in word_count:
    if word_count[word] > 1000000:
        print(word, word_count[word])

print(len(word_count))

while True:
    in_word = input('請輸入想查詢的文字: ')
    if in_word == 'q':
        print('感謝使用本查詢功能')
        break
    elif in_word in word_count:
        print(in_word, '出現了 ', word_count[in_word], '次')
    else:
        print('這個字沒有出現過')