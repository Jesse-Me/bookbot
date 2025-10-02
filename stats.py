def get_word_count(book):
    words = book.split()
    word_count = len(words)

    return word_count

def get_char_count(file_contents): 
    
    results = {} 
    file_contents = file_contents.lower()
    
    for character in file_contents:
       results[character] = results.get(character, 0) + 1
    
    return results
 
def get_sorted_char_count(char_count):
    
    sorted_list = []
    char_count = char_count.isalpha()
    for key, value in char_count.items():
        
        sorted_list.append({"char":key, "num": value})
        
    
    

    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    
    return sorted_list
    