def main():
 book_path = "books/frankenstein.txt"
 text = get_book_text(book_path)
 num_words = get_num_words(text)
 num_letters = get_num_char(text)
 sorted_report = sort_on(num_letters)
 print(sorted_report)
 
 

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
  small_dict[key] = value
  report_list.append(small_dict)
 return report_list
#refine list of dict as letter: a, occurence: 74065213

def sort_on(report):
 return 
 
 report.sort(key=sort_on, reverse=True)
 return report
 


main()
