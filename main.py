print ('Type EDE() to start') 

def EDE():
    
    choice = ''
    while choice != 'exit':
      choice = input('Would you like to encrypt, decrypt, or exit?')
      if choice == 'encrypt':
        print ('Please input your n value')
        n=int(input())
        print ('Please input your e value')
        e=int(input())
        encrypt(e,n)
      elif choice == 'decrypt':
        print ('Please input your d value')
        d=int(input())
        print ('PLease input your n value')
        n=int(input())
        decrypt(d,n)
    
def encrypt(e,n):
    encrypted_message = ''
    encrypt = ''
    numerize = ''
    message = ''
    print ('please input your message')
    message=input()
    
    for x in message:
        numerize = ord(x)
        encrypt = pow(numerize, e, n)
        denumerize = chr(encrypt)
        encrypted_message += denumerize
    print (encrypted_message)

    
def decrypt(d,n):
    decrypted_message = ''
    denumerize = ''
    print ('Please input your encrypted message')
    encrypted_message=input() 
   
    for t in encrypted_message:
        numerize = ord(t)
        decrypt = pow(numerize, d, n) 
        denumerize = chr(decrypt)
        decrypted_message += denumerize
    print (decrypted_message)


  

