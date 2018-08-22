# Xhanti Singatha
# Morse Code

def code_letter(letter):

    morse = {'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..'}
    
    return morse[letter.lower()]

def transmit_letter(letter):
    
    item = code_letter(letter)
    string = ''
    index = len(item)
    
    for i in range(0,index-1):
        if item[i] == '-' or item[i] =='.':
            string += item[i]+'^'
            
    return string+item[index-1]


def transmit_word(word):
    
    length = len(word)
    element = ''
    for i in range(0,length-1):
        element += transmit_letter(word[i])+'|'
        
        
    print(element+transmit_letter(word[length-1]))

def word_pause():
    print('||')