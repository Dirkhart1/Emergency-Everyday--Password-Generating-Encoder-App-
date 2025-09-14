def flip(T):
  if len(T) >= 2:
    T = T[::-1]
    li = int(len(T)/2)
    t1 = T[:li]
    t2 = T[li:]
    newT = t2 + t1
    return newT
  else:
    return T

def load_key():
          with open('storage/filekey.key', 'rb') as key_file:
              return key_file.read()

# Thes definitions are the ciphering method used to encode the password text
def encoding(lex, num):
  code = ""
  a = ord(lex)
  # This allows the letter to be converted into ASCII, the code is carefully crafted for each ASCII interger being beetwen 33 - 126
  # If number is = 0 6 or 3
  if num % 3 == 0 :
    a = (int(a) % 33) + 33
    code = chr(a)
    return code
  # If number is = 2 4 or 8 
  elif (num % 2 == 0 and num % 3 != 0):
    a = (int(a) % 33) + 66
    code = chr(a)
    return code
# If number is = 1 3 or 7 
  else:
    a = (int(a) % 33) + 94
    code = chr(a)
    return code

def encode(p, n1, n2, n3):
  encodeP = ""
  num = ((n1+1) * (n2+1) + n3) % 9
  newP = flip(p)

  for letter in newP:
    encodeP += encoding(letter, num)
    num += ((n1 * n2)+1) + (n2 * n3) + (n3 * n1)
    num = num % 9

  return encodeP