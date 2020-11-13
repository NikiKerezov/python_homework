check = ["a", "e", "o", "u", "i", "A", "E", "O", "U", "I"]
string = input()
string = list(string)
count = 0
for i in check:
    for j in string:
        if i == j:
            count += 1

print(count)
