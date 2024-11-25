def main():
 book_path = "books/frankenstein.txt"
 text = get_book_text(book_path)
 num_words = get_num_words(text)
 num_letters = get_num_char(text)
 print(f"{num_words} words found in the document")
 print(f"{num_letters} letters found in the document")
 
 

def get_num_words(text):
 words = text.split()

 return len(words)


def get_book_text(path):
 with open(path) as f:
  return f.read()

def get_num_char(text):
 char_count = {}
 words_lowered = text.lower()
 for letters in words_lowered:
  if letters in char_count:
    char_count[letters] += 1
  else:
    char_count[letters] = 1

 
 return char_count
   #need to individualize count for every letter





 
 return len(words)
 


 
 
 

main()
