data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
'''
		count += 1
		if count % 10000 == 0:
			print(len(data))
'''
print('檔案中總共有', len(data), '筆資料')

sum_len = 0
for c in data:
	sum_len += len(c)

print('所有留言的平均長度為', sum_len/len(data))