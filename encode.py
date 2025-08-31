

#Entry = ""
#encoded_password = ""
#password = input("Enter Password to encode: ")
##pass1 = int(input("Enter num: "))
#pass2 = int(input("Enter num: "))
#pass3 = int(input("Enter num: "))
# i = 0


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
  number = (pass1 * pass2 + pass3) % 10

  for letter in password:
    # be between 33-126

    # This prints a special chracter
    if number % 3 == 0 and number % 2 == 0:
      encoded_password += encode1(letter)

    # This prints a Upper case
    elif (number % 2 == 0 and number % 3 != 0):
      encoded_password += encode2(letter)  

    #This prints a lowercase
    else:
      encoded_password += encode3(letter)

    number += ((pass1 * pass2) + (pass2 * pass3) + (pass3 * pass1))
    number = number % 10

  return encoded_password

