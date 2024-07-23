# Write a Python program to count the occurrences of each word in a given sentance



sentence = "To change the overall look of your document. To change the look available in the gallery"
words = sentence.lower().split()

word_count = {}

for word in words:
    
    word = word.strip(".,")
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


for word, count in word_count.items():
    print(f"{word}: {count}")


    print("<---------------------------------------------------------------------------->")

# Write a Python program to remove a newline in Python
# String = "\nBest \nDeeptech \nPython \nTraining\n
    
string = "\nBest \nDeeptech \nPython \nTraining\n"


string_without_newlines = string.replace('\n', ' ')

print(string_without_newlines)


print("<---------------------------------------------------------------------------->")
# Write a Python program to reverse words in a string
# String = “Deeptech Python Training”

string = "Deeptech Python Training"


words = string.split()


reversed_words = words[::-1]


reversed_string = ' '.join(reversed_words)

print(reversed_string)

print("<---------------------------------------------------------------------------->")
# Write a Python program to count and display the vowels of a given
# text
# String=”Welcome to python Training”





string = "Welcome to python Training"


vowels = "aeiouAEIOU"


vowel_count = {vowel: 0 for vowel in vowels}

for char in string:
    if char in vowels:
        vowel_count[char] += 1


for vowel, count in vowel_count.items():
    if count > 0:
        print(f"{vowel}: {count}")
