def main():
 book_path = "books/frankenstein.txt"
 text = get_book_text(book_path)
 num_words = get_num_words(text)
 num_letters = get_num_char(text)
 num_letters.sort(key=sort, reverse=True)
 #print(num_letters, num_words)
 reports = report(num_letters)
 print(f"--- Begin report of {book_path} ---") 
 print(f"{num_words} found") 
 print(f"{reports} ---End of the report---")

def sort(e):
 return e["count"]
def get_num_words(text):
 words = text.split()

 return len(words)

def get_book_text(path):
 with open(path) as f:
  return f.read()

def get_num_char(text):
 char_count = {}
 report_list = []
 words_lowered = text.lower()
 for letters in words_lowered:
  if letters.isalpha():
   if letters in char_count:
     char_count[letters] += 1
   else:
     char_count[letters] = 1
 for key in char_count:
  small_dict = {}
  value = char_count[key]
  small_dict["letter"] = key
  small_dict["count"] = value
  report_list.append(small_dict)
 return report_list
 
def report(list_dict):
 s = ""
 for i in list_dict:
  s += (f"The {i['letter']} character was found {i['count']} times ")
 return s

main()
