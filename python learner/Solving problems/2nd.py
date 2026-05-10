sentence = "Hello world".lower().replace(" ","")

vowels = "aeiou"
dict = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}

for vowel in vowels:
    for word in sentence:
        if word == vowel:
            dict[vowel] += 1

        else:
            dict[vowel] += 0

print(dict)

