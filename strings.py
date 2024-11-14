words = []
for i in range(10):
    word = input(f"Enter a word {i + 1}: ")
    words.append(word)
    
while True:
    length = input("Please enter a length or number: ")
    if length.isdigit():
        length = int(length)
        break
    else:
        print("Please enter a numeric value.")
        
matching_words = [word for word in words if len(word) >= length]
print("\nDone")
if matching_words:
    print("\nWords with the required length:", ', '.join(matching_words))
else:
    print("\nNo words are found with the required length.\n")