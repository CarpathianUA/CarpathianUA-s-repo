#-*-coding:utf8;-*-
#qpy:2
#qpy:console

fruits = ['apples', 'bananas', 'tofu', 'cats']

def PlusEnd(some_list):
    sentence = ""
    for f in some_list[:-1]:
        sentence += f + ','
    sentence = sentence + ' and ' + fruits[-1]
    return sentence

print PlusEnd(fruits)
