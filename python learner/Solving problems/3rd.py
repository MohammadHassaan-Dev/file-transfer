sentence = input("Enter: ").lower().replace(" ", "")

reversed = sentence[::-1]

if sentence == reversed:
    print("Palindrome")

else:
    print("Not Palindrome")