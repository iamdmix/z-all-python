msg = input('>')
words = msg.split(' ')
emojis = {
    ":)":"😃",
    ":(":"😢",
    "-_-":"😑"
}
output=""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
