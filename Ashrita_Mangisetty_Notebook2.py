#!/usr/bin/env python
# coding: utf-8

# In[10]:


def encode_rot(text,key): #this function take plain input and key and gives encoded text as the output
    encoded_text = "" 
    for char in text: #this particular loops runs for each character in the word and encodes it using the ascii values
        if char.isalpha():
            if char.islower(): #this runs if the char is lowercase
                encoded_char = chr(((ord(char) - ord('a')+ key) % 26)+ ord('a'))
            else:  #this runs for all the characters that are uppercase and finds the encoded output of the character
                encoded_char = chr(((ord(char) - ord('A')+ key) % 26)+ ord('A'))
        else: #if the character has number or special characters other than alphabet, it stores that vaulue as it is in the output
             encoded_char = char
        encoded_text += encoded_char #it sums up the output from loop to the encoded text
    return encoded_text
    


# In[11]:


l = "Machine CAN learn 2 !!!" #text input
k = 28 #key input 
print(encode_rot(l,k))  #function calling with input text and key


# In[12]:


def isenglish(word, dict_words): #this function takes words from input and coverts it into lowercase
    return word.lower() in dict_words

def decode_rot(cipher_text): #this command decodes the input text provided
    best_key = 0 
    best_wordcount = 0 
    best_decodedtext = ""

    with open("Dictionary.txt", "r") as file: #this opens the text file Dictionary in read mode
        dict_words = set(word.strip().lower() for word in file) # this statement removes all the white spaces, converts the words into lowercase and saves completely in the dict_word

    for i in range(26): #this loop runs from 0-25(i.e., as given) and iterates through possible key values for decoding
        decoded_text = ""
        for char in cipher_text: # it loops for each character in the given word and finds the character using ascii values 
            if char.isalpha():
                if char.islower():
                    decoded_char = chr(((ord(char) - ord('a') - i) % 26) + ord('a'))
                else: 
                    decoded_char = chr(((ord(char) - ord('A') - i) % 26) + ord('A'))
            else: #this stores the character if it is number or special characters in the decoded_char variable 
                decoded_char = char
            decoded_text += decoded_char

        words = decoded_text.split() 
        valid_wordcount = sum(1 for word in words if isenglish(word, dict_words)) #this loop increments the valid word count by 1, if the word is present in dictionary word

        if valid_wordcount > best_wordcount: # if statement is used in the loop to find the best key value by comparing the input word count & best word count value as it loops through
            best_wordcount = valid_wordcount
            best_key = i #for the coresponding value of word count, the key value is set
            best_decodedtext = decoded_text 

    return best_decodedtext, best_key #this function returns the decoded text and key



# In[13]:


cipher_text = "Tqjq yi byau fuefbu, ydjuhhewqju yj xqht udekwx qdt yj mybb jubb oek mxqjuluh oek mqdj je xuqh."
clear_text, key = decode_rot(cipher_text) #function call to find decoded char by giving text and the key
print("The clear text is:", clear_text)
print("The key is:", key)


# In[14]:


#encoding examples
#Example 1
l = "This is Machine Learning first assignment" #text input
k = 13 #key input 
print(encode_rot(l,k))  #function calling with input text and key

#Example 2
l = "The Machine Learning course is super interesting and you need to focus more. Have a happy learning!!" #text input
k = 13 #key input 
print(encode_rot(l,k))  #function calling with input text and key

#Example 3
l = "Machine CAN learn 2 !!! " 
k = 2  
print(encode_rot(l,k))  

#Example 4
l = "What's up? " 
k = 13 #key input 
print(encode_rot(l,k))  

#Example 5
l = "Security matters."
k = 10
print(encode_rot(l,k))


#Example 6
l = "Python is fun."
k = 13
print(encode_rot(l,k))







# In[15]:


#decoding examples
#Example 1
cipher_text = "Guvf vf Znpuvar Yrneavat svefg nffvtazrag."
clear_text, key = decode_rot(cipher_text)
print("The clear text is:", clear_text)
print("The key is:", key)

#Example 2
cipher_text = "V nz n tenqhngr fghqrag sebz ZFVG."
clear_text, key = decode_rot(cipher_text)
print("The clear text is:", clear_text)
print("The key is:", key)

#Example 3
cipher_text = "Uryyb thlf!! Rawbl lbhe ybat jrrxraq!!"
clear_text, key = decode_rot(cipher_text)
print("The clear text is:", clear_text)
print("The key is:", key)

#Example 4
cipher_text = "Jung'f hc?"
clear_text, key = decode_rot(cipher_text)
print("The clear text is:", clear_text)
print("The key is:", key)


# In[16]:


#Example 5 decoding
cipher_text = "Ocejkpg ECP ngctp 2 !!!"
clear_text, key = decode_rot(cipher_text)
print("The clear text is:", clear_text)
print("The key is:", key)


# In[17]:


#Example 6 decoding
cipher_text = "Comebsdi wkddobc."
clear_text, key = decode_rot(cipher_text)
print("The clear text is:", clear_text)
print("The key is:", key)



# In[ ]:




