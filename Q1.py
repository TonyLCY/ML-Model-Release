import sys

if len(sys.argv) < 2:
    print('Not enougn arguement')

filename = sys.argv[1]
input = open(filename, 'r')
line = input.readline()
words = line.split()

id = 0
id_word = {}
word_cnt = {}
for word in words:
    if word in word_cnt:
        word_cnt[word] += 1
    else:
        id_word[id] = word
        id += 1
        word_cnt[word] = 1

total = id
output = open('./Q1.txt', 'w')
for id in range(total):
    word = id_word[id]
    line = word + ' ' + str(id) + ' ' + str(word_cnt[word]) + '\n'
    output.write(line)
