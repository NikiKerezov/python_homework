string = ["my", 1, "turtle", "explain", 3.14]
a = len(string)
i = 0
while i < a:
    if type(string[i]) == int or type(string[i]) == float:
        del string[i]
        i -= 1
        a -= 1
    i += 1
    
print(string)

