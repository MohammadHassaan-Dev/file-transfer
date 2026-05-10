# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

a = input("Enter your hindi word: ")

d = {
    "Kursi":"Chair",
    "Darwaza":"Door",
    "Satrangi":"Orange"
}

print(f"The english word of {a} is: {d[a]}")