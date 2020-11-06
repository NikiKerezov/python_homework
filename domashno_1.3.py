a = input('Enter a string: ')
b = ''
a = list(a)
a.sort()
print(a)
for i in range(len(a)):
    print(i)
    if str[i] != b:
        print(''', str[i], ''', 'appears', a.count(str[i]), 'times in this string')
    b = a[i]