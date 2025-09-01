
def encode1(letter):
  code = ""
  num = ord(letter)
  num = (int(num) % 33) + 33
  code = chr(num)
  return code

def encode2(letter):
  code = ""
  num = ord(letter)
  num = (int(num) % 33) + 66
  code = chr(num)
  return code

def encode3(letter):
  code = ""
  num = ord(letter)
  num = (int(num) % 33) + 94
  code = chr(num)
  return code

def encode(password, pass1, pass2, pass3):
  encoded_password = ""
  number = (pass1 * pass2 + pass3) % 9

  for letter in password:
    # This loop allows the letter to be converted into ASCII, the code is carefully crafted for each ASCII int being beetwen 33 - 126

    # If number is = 0 6 or 3
    if number % 3 == 0 :
      encoded_password += encode1(letter)

    # If number is = 2 4 or 8 
    elif (number % 2 == 0 and number % 3 != 0):
      encoded_password += encode2(letter)  

    # If number is = 1 3 or 7 
    else:
      encoded_password += encode3(letter)

    number += ((pass1 * pass2) + (pass2 * pass3) + (pass3 * pass1))
    number = number % 9

  return encoded_password

