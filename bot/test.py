class Swear:
    swear_words = str(open('swear_words.txt', 'r').read())
    swear_words = swear_words.split(''',
''')
    swear_words.pop()
print(Swear.swear_words)

x = input()

for i in range(len(Swear.swear_words)):
    if Swear.swear_words[i] in x:
        print("success")
    else:
        print("nope")
