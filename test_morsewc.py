from morsewc import EnglishMessage, MorseMessage

# Create string to be tested
message_string = "hello everyone"

# Initialise message instance
message = EnglishMessage(message_string)

# Encodes message to morse
code_string = message.encode()

# Initalise code instance
code = MorseMessage(code_string)

# Decodes code to english
decoded = code.decode()

# Check if orginal message == decoded message,
#if True then morsewc works as intended.
print(decoded == message_string)