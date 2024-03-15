from morsewc import EnglishMessage, MorseMessage

message_string = "hello everyone"
message = EnglishMessage(message_string)

code_string = message.encode()
code = MorseMessage(code_string)
decoded = code.decode()

print(decoded == message_string)