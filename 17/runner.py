#/usr/bin/python

from num2words import num2words

count = 0

for i in range(1, 1001):
    holder = num2words(i, lang='en_GB')
    holder = holder.replace(" ", "")
    holder = holder.replace("-", "")
    count += len(list(holder))

print count
