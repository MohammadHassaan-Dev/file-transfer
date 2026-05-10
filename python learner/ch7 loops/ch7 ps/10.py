""" 
Problem Statement: Read the paragraph from confusion.txt and display the count of each word occuring in the confusion.txt

input: let's say this is let's say is paragraph say
output:
{
    "let's": 2,
    "say": 3,
    "this": 1,
    "is": 2,
    "paragraph": 1
}
"""

# def demo():
#     with open("confusion.txt")as f:
#         data = f.read()
#     for i in range(1,len(data)):
#         a = data[i]
#         print(a.count(a))

    
# demo()

def count_words():
    with open("confusion.txt")as f:
        data = f.read()
    dictionary = {}
    words = data.lower().split()

for word in words:
    if word in dictionary:
        word[dictionary] = word[dictionary]+1
    
    else:
        word[dictionary]