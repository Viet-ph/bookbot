def count_letters(data):
    mydict = {}
    for letter in data:
        letter = letter.lower()
        if letter in mydict:
            mydict[letter] += 1
        else:
            mydict[letter] = 1 
    
    return mydict

def sort_on(dict):
    return dict['num']

def dict_to_list(data):
    return [{'name': key, 'num': data[key]} for key in data]

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        words = file_contents.split()
        list_of_dicts = dict_to_list(count_letters(file_contents))
        sorted_list = sorted(list_of_dicts, key=sort_on, reverse=True)
        for item in sorted_list:
            if item['name'].isalpha():
                print(f'the \'{item['name']}\' was found {item['num']} times')

main()
