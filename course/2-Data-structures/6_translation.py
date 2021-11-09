from get_filename import get_filename
dictionary_url = get_filename('dictionary')


def get_input():
    return input('give a string: ')


def get_key_val(line):
    return line.replace('\n', '').split('=')


def merge_key_val(key, val):
    return key + '=' + val + '\n'


def get_dictionary():
    with open(dictionary_url, 'r') as dic:
        return {get_key_val(line)[0]: get_key_val(line)[1] for line in dic}


def append_new_trans(key, val):
    with open(dictionary_url, 'a') as dic:
        dic.write(merge_key_val(key, val))


def prog():
    while True:
        print('\n--------------- WELCOME TO DICTIONARY 1.1.1 --------------------\n')
        dic = get_dictionary()
        inp = get_input()
        if inp in dic.keys():
            print('\n' + merge_key_val(inp, dic[inp]))
        else:
            print('\nno translation found, give one: ')
            trans = get_input()
            append_new_trans(inp, trans)
        print('\nDo you want to continue? [yes, no]:')
        yes_or_no = input()
        if yes_or_no == 'no':
            print('\nBYE')
            break


prog()
