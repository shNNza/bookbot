def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def count_characters(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


with open("books/frankenstein.txt", "r") as file:
    text = file.read()
    result = count_characters(text)

def sort_on(dict):
    return dict["num"]

char_counts = count_characters(text)

char_list = []
for char, count in char_counts.items():
     if char.isalpha():
         char_list.append({"char": char, "num": count})
         
char_list.sort(reverse=True, key=sort_on)
word_count = get_num_words(text)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document")
print()
for item in char_list:
    print(f"The '{item['char']}' character was found {item['num']} times")
print("--- End report ---")

    
main()