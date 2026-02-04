#ceaser cipher
#assigning variable

alphabets = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

direction = input("type 'encode' to encode,type 'decode' to decode:\n").lower()
orignal = input("type your text:\n").lower()
shifted = int(input("type the shift number:\n"))



def cipher(orignal_text,shifted_text,encode_or_decode):
    cipher=""
    if encode_or_decode=="decode":
        shifted_text*=-1
    for letter in orignal_text:
        if letter in alphabets:
            position = alphabets.index(letter) +shifted_text
            cipher+=alphabets[position % 26]
    print(f"Here is your {encode_or_decode}d cipher :{cipher}")

cipher(orignal_text=orignal,shifted_text=shifted,encode_or_decode=direction)

should_continues = True
while should_continues:
    direction = input("type 'encode' to encode,type 'decode' to decode:\n").lower()
    orignal = input("type your text:\n").lower()
    shifted = int(input("type the shift number:\n"))
    cipher(orignal_text=orignal,shifted_text=shifted,encode_or_decode=direction)

    restart=input("type 'y' to restart.otherwise 'no' \n").lower()
    should_continues =False
    print("----------goodbye---------")