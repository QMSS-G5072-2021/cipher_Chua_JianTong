def cipher(text, shift, encrypt=True):
	'''
	Takes a string and encrypts (or decrypts) it using the Caesae cipher. 
	
	Takes 3 arguments:
	text - the text to be encrypted or decrypted
	shift - the number of alphabets to shift each character in the string by
	encrypt - True by default, for decryption use False
	
	For example,
	cipher("Hello",1) returns Ifmmp
	This can be reversed to get back "Hello" using cipher("Ifmmp",1,encrypt=False)
	'''
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text