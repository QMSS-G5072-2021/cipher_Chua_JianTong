def cipher(text, shift, encrypt=True):
    '''Takes a string and encrypts (or decrypts) it using the Caesar cipher. 
	
    Parameters
    ----------
	text :  String
        string to be encrypted or decrypted
	shift : Integer
        the number of alphabets to shift each character in the string by        
	encrypt : Boolean
        True by default, for decryption use False
	
    Returns
    -------
    string
        The encrypted/decrypted string

    Examples
    --------
	>>> from cipher_jc5492 import cipher
    >>> cipher("hello",1)
    ifmmp
    >>> cipher("ifmmp",1,encrypt=False)
    hello
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