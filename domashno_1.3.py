a = input('Enter a string: ')
b = ''
a = list(a)
a.sort()
print(a)
for i in range(len(a)):
    print(i)
    if str[i] != str[i-1]:
        print(''', str[i], ''', 'appears', str.count(str[i]), 'times in this string')
    