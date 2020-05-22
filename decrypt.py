
print('''Instructions: To decrypt enter 'dec' and 
to Encrypt enter 'enc' ''')

#Initializing circular Alphabet

alpha_list = ['a','b','c','d','e','f','g','h','i','j',
'k','l','m','n','o','p','q','r','s','t','u','v',
'w','x','y','z','a','b','c','d','e',
'f','g','h','i','j','k','l','m','n',
'o','p','q','r','s','t','u','v','w','x',
'y']

#Getting Inputs
input_text = input("Input Text: ")
key = int(input("Key: "))
operation = input("Enter OPeration 'enc/dec' ")

#Defining Lists to Store Data
text_list=[]
decrypt=[]
last_list=[]
character=0

#Storing Input Text to a list as Single characters
for letters in input_text:
    text_list.append(letters)
    


#Iterating through  circular alphabet and user input list
for char in text_list:
    for letter in alpha_list:
        #matching Charcaters
        if char == letter:
            character=(alpha_list.index(char)+1)
            #matching Operation
            if operation == "enc":
                decrypt.append(alpha_list[character-1+(key)])
            else:
                decrypt.append(alpha_list[character-1-(key)])

#Converting List in to a string
dec_string=''.join (map(str,decrypt))

#Fixing double character Error
for dec in range (0,len(dec_string),2):
    last_list.append(dec_string[dec])

if operation == "enc":
    print("Encrypted Value: ",''.join(map(str,last_list)))
else:
    print("Decrypted Value: ",''.join(map(str,last_list)))
