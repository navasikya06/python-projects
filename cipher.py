alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
import random
random.seed()
import math

def file_to_string(filename):
    with open(filename, "r") as f:
        x = f.read()
    return x

def string_to_file(filename, s):
    with open(filename, "w") as f:
        f.write(s)

#############################################################
# A working Caesar cipher
#############################################################

def simplify_string(s):
    simple_string = ""
    s = str.upper(s)
    for i in s:
        x = i in alpha
        if x == True:
            simple_string = simple_string + i
    return simple_string

def num_to_let(x):
    if x > 25:
        x = x - 26 #to return to the beginning of the alphabet list if the number is greater than 25
    return alpha[x]

def let_to_num(a):
    return alpha.index(a)
    
def shift_char(char, shift):
    char = let_to_num(char)
    char_shift = num_to_let(char + shift)
    return char_shift

def caesar_enc(plain, key):
    plain = simplify_string(plain)
    key = let_to_num(key)
    cipher = ""
    for i in plain:
        cipher += shift_char(i, key)
    return cipher

def caesar_dec(cipher, key):
    cipher = simplify_string(cipher)
    cipher_dec = ""
    key = let_to_num(key)
    for i in cipher:
        cipher_dec += shift_char(i,-key)
    return cipher_dec

#############################################################
# Breaking the Caesar cipher
#############################################################

def letter_counts(s):   
    counts = {}
    i = 0 
    while i < len(alpha): #to create a dictionary of all letters in the alphabets with their number of counts in the given string s
        a = alpha[i] #set the letter to be a certain one in the alphabet
        count = 0
        k = 0
        while k < len(s): #count up if we find the same letter in the string
            if s[k] == a:
                count += 1
            k += 1
        counts[a] = count
        i += 1
    return counts

def normalize(counts):
    total = 0
    for i in counts:
        total += counts[i] #take the sum of all the counts
    for i in counts:    
        counts[i] = counts[i]/total #divide each count by the total to normalize
    return counts 

def distance(observed, expected):
    distance = 0
    for i in observed: #using the given formula to calculate difference of the counts to the standard counts
        distance += (observed[i] - expected[i])**2/expected[i]
    return distance

def caesar_break(cipher, frequencies):
    key = 0 #set first trial key to index 0 of alpha
    output = 0 #the final chosen key
    cipher_dec = caesar_dec(cipher, alpha[key])
    dist = distance(normalize(letter_counts(cipher_dec)), frequencies) #decipher with the set key and calculate distance
    while key <= 25:
        if distance(normalize(letter_counts(caesar_dec(cipher, alpha[key]))), frequencies) < dist:
            output = key
            dist = distance(normalize(letter_counts(caesar_dec(cipher, alpha[key]))), frequencies)
            cipher_dec = caesar_dec(cipher,alpha[key])
        key += 1 #if the incremented key results is lower distance, output gets replaced with the new key, the distance is reset to the new one, and the text is replaced
    output = num_to_let(output)
    return [output, cipher_dec]

#############################################################
# A working Vigenere cipher
#############################################################

def vigenere_enc(plain, key):
    plain = simplify_string(plain)
    keynum = []
    for i in range(len(key)): #turn key into a list of numbers
        keynum.append(let_to_num(key[i]))
    cipher = ""
    for i in range(len(plain)): #from plain text, shift every letter by the index of the letter in the original key, given in the keynum list. 
        index = i % len(key) #this turns the normal index i in the text into the corresponding letter in the key, which is calculated as the remainder of dividing it with len(key)
        cipher += shift_char(plain[i], keynum[index])
    return cipher

def vigenere_dec(cipher, key):
    cipher = simplify_string(cipher)
    keynum = []
    for i in range(len(key)):
        keynum.append(let_to_num(key[i]))
    cipher_dec = ""
    for i in range(len(cipher)):
        index = i % len(key)
        cipher_dec += shift_char(cipher[i], -keynum[index])
    return cipher_dec

#############################################################
# Breaking the Vigenere cipher
#############################################################

def split_string(s, parts):
    s = simplify_string(s)
    newstring = []
    for i in range(parts): #for every remainder of an index with the number of parts, find the corresponding letters and string them together
        index = i % parts
        a = s[i]
        for k in range(len(s)):
            if k % parts == index and k != i: #to avoid duplication
                a += s[k]
        newstring.append(a) #put them into a list of strings, each string corresponding to the letters encoded by one letter in the key
    return newstring

def vig_break_for_length(cipher, klen, frequencies):
    cipher = split_string(cipher, klen) #create a list of letters from the cipher with the same key letter
    cipher_break = []
    for i in cipher:
        cipher_break.append(caesar_break(i, frequencies)) #caesar break each string from the list, and add the list [key, deciphered string] to a new list called cipher_break
    for i in range(len(cipher_break)): # for each string in the list that is not as long as the others, add one spacing (since cipher length is not always divisble by the key length)
        stand = len(cipher_break[0][1])
        if len(cipher_break[i][1]) < stand:
            cipher_break[i][1] += " "
    key = ""
    for m in cipher_break: #the list cipher_break consists of lists, each with two elements, key and the deciphered string
        key += m[0] #string together the key, which is the 0 element of each element list in cipher_break
    cipher_real = ""
    for k in range(len(cipher_break[i][1])): #for each string in cipher break, which is the 1 element of each element list in cipher_break, string together the k element in them
        for i in range(len(cipher_break)):
            cipher_real += cipher_break[i][1][k] #take the k element in string 1, add k element in string 2, and so on, then increment k to go through all the letters in the string
    cipher_real = simplify_string(cipher_real) #to remove the spacings
    return [key, cipher_real]

def vig_break(c, maxlen, frequencies): 
    k = 1
    cipher_real = vig_break_for_length(c, k, frequencies)[1] #break for a certain key length, and call the string cipher_real
    dist = distance(normalize(letter_counts(vig_break_for_length(c, k, frequencies)[1])), frequencies)
    while k <= maxlen: #compare the original distance with all the distances generated from other key lengths smaller than the given max length
        if distance(normalize(letter_counts(vig_break_for_length(c, k, frequencies)[1])), frequencies) < dist:
            dist = distance(normalize(letter_counts(vig_break_for_length(c, k, frequencies)[1])), frequencies)
            cipher_real = vig_break_for_length(c, k, frequencies)[1]
            answer = vig_break_for_length(c, k, frequencies) #change the distance, the deciphered cipher, and the [key, text] combination everytime the distance is smaller
        k += 1
    return answer

#############################################################
# A working substitution cipher
#############################################################

def sub_gen_key():
    return ''.join(random.sample(alpha, len(alpha))) 

def sub_enc(s, k):
    s = simplify_string(s)
    dic = {}
    cipher = ""
    for i in alpha:
        dic[i] = k[alpha.index(i)] #create a dictionary with each letter in the alphabet and its corresponding replacement
    for m in s:
        cipher += dic[m] #turn each letter in s into the corresponding replacement and string them together
    return cipher

def sub_dec(s, k):
    dic = {}
    plain = ""
    for i in k:
        dic[i] = alpha[k.index(i)]
    for m in s:
        plain += dic[m]
    return plain

#############################################################
# Breaking the substitution cipher
#############################################################

def count_trigrams(s):
    dic = {}
    for i in range(len(s)-2): #to not get out of index range
        a = s[i]+s[i+1]+s[i+2] #create a string of three
        if a not in dic: 
            dic[a] = 1 #add this string of three to a dictionary and the count 1
        else:
            dic[a] += 1 #increment 1 if the string is already there
    return dic

english_trigrams = count_trigrams(simplify_string(file_to_string("twocities_full.txt")))
normalize(english_trigrams)

def map_log(d):
    dictlog = {}
    for i in d:
        dictlog[i] = math.log(d[i]) #turn the count into its ln
    return dictlog

english_trigrams = map_log(english_trigrams)

def trigram_score(s, english_trigrams):
    s = count_trigrams(s) #make a list of trigrams for the string
    score = 0
    for i in s: #for each trigram in the string, see if it's in the english_trigrams, and add the corresponding log frequency 
        if i not in english_trigrams:
            score -= 15
        else:
            score += english_trigrams[i]
    return score

def sub_break(cipher, english_trigrams):
    key = sub_gen_key()
    plain = sub_dec(cipher, key)
    score = trigram_score(plain, english_trigrams) #set up the key, the test decipherd text, and its score
    count = 1
    while count <= 1000: #while the number of fails hasn't reached 1000, keep trying to find the better key
        a = random.choice(key) #choose random letters a and b in the key, and take its index
        b = random.choice(key)
        c = key.index(a)
        d = key.index(b)
        if c < d:
            k = key[:c]+b+key[c+1:d]+a+key[d+1::] #string the key back together with the letters swapped
        elif c > d:
            k = key[:d]+a+key[d+1:c]+b+key[c+1::]
        elif c == d:
            k = key
        if trigram_score(sub_dec(cipher, k), english_trigrams) > score: #replace key, text, score everytime a better score is found
            key = k
            plain = sub_dec(cipher, key)
            score = trigram_score(sub_dec(cipher, k), english_trigrams)
            count = 1 #to reset unless it has failed 1000 times
        count += 1
    return [key, plain]


a = caesar_enc("The pharmacy. The elderly tree. Seven to five.", "B")
print(a)
b = caesar_dec(a, "B")
print(b)
