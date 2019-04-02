alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 'Z',]

def alphabet_position(letter):
    

    me = letter.upper()

    return alphabet.index(me)


def rotate_character(rot, char):

    encrypted = ''
    if char.isalpha():
        for letter in char:
            if char == " ":
                encrypted = encrypted + " " 
            else:
                rotation = alphabet_position(letter) + rot

                if rotation < 26: 
                   encrypted = encrypted + alphabet[rotation]
                else:
                    encrypted = encrypted + alphabet[rotation % 26]
            
        return encrypted
    
    else: 
        return char


def encrypt(text, rot):
    empty = ''
    for char in text:
        
        if char.isupper() == True:
            upper_rotate = rotate_character(rot, char)
            empty += upper_rotate
        else:
            lower_rotate = rotate_character(rot, char)
            
            empty += lower_rotate.lower()
        
    return empty


def main():

    char_input = str(input("What is your message: "))
    rot_input = int(input("How far should we rotate the message: "))

    
    # empty = ''
    # for char in char_input:
        
    #     if char.isupper() == True:
    #         upper_rotate = rotate_character(rot_input, char)
    #         empty += upper_rotate
    #     else:
    #         lower_rotate = rotate_character(rot_input, char)
            
    #         empty += lower_rotate.lower()
        
    solution = encrypt(char_input, rot_input)
    
    print(solution)
    
           
        
            
    
    
    

if __name__ == "__main__":
    main()


    






#def rotate_character(rot, char):

    
    



#create fucntion to just index cap letters

#create function to take index and rotate it 
    #if it isn't uppercase - return lower case 

    #if upper case - return normal


