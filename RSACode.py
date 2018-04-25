e = ''
n = ''
d = '' 
message = ''
encrypted_message = ''


def EDE():
    print 'Would you like to encrypt, decrypt or quit?'
    EDE=raw_input()
    if EDE == 'encrypt':
        encrypt()
    if EDE == 'decrypt':
        decrypt()
    
def encrypt():
    encrypted_message = ''
    print 'Please input your n value'
    n=input()
    print 'Please input your e value'
    e=input()
    print 'please input your message'
    message=raw_input()
    
    for x in message:
        numerize = ord(x)
        encrypt = pow(numerize, e, n)
        denumerize = unichr(encrypt)
        encrypted_message += denumerize
    print encrypted_message
    
def decrypt():
    decrypted_message = ''
    print 'Please input your d value'
    d=input()
    for t in encrypted_message:
        numerize = ord(t)
        decrypt = pow(numerize, d, n) 
        denumerize = chr(decrypt)
        decrypted_message += denumerize
    print decrypted_message

