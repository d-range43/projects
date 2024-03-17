class EnglishMessage:
    """
    A Class used to represent an English Message.
    
    Attributes: 
        message (str): a message in english characters (a-z), numbers (1-9) 
            and spaces ' '.
        
    """
    def __init__(self, message):
        """
        Initialises MorseMessage instance.
        
        Args:
            message (str): a message in english characters (a-z), numbers (1-9) 
                and spaces ' '.
        
        """
        self.message = message
        self.letter_to_morse = {
            'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
            'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
            'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
            'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
            '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
            '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'
            }
    
    def encode(self):
        """
        Converts an english message into a morse message.

        """
        morse = []
        #loop over each english letter in message
        for letter in self.message:
            # make each letter lowercase
            letter = letter.lower()
            #append empty morse list
            morse.append(self.letter_to_morse[letter])
        
        #list to string and add spaces
        morse_message = " ".join(morse)
        return morse_message

class MorseMessage:
    """
    A Class used to represent a Morse Message.
    
    Attributes: 
        message (str): a message in characters dots '.', dashes '-' 
            and slashes "/".
        
    """    
    def __init__(self, message):
        """
        Initialises MorseMessage instance.
        
        Args:
            message (str): a message in characters dots '.', dashes '-' 
                and slashes "/".
        
        """
        self.message = message
        self.morse_to_letter = {}
        letter_to_morse = {
            'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
            'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
            'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
            'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
            '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
            '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'
            }
        # swaps keys and values for morse_to_letter
        for letter in letter_to_morse:
            morse = letter_to_morse[letter]
            self.morse_to_letter[morse] = letter
    def decode(self):
        """
        Converts a morse message into an english message.
        
        """
        english = []
        # string to list 
        morse_letters = self.message.split(" ")
        #loop over each morse letter in message
        for letter in morse_letters:
            #append empty english list
            english.append(self.morse_to_letter[letter])
    
        # rejoin, no need to add spaces
        english_message = "".join(english)
    
        return english_message