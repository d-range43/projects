## Find And Replace function:
    
def findAndReplace(text, oldText, newText):
    """
    Searches through text and replaces any instances of oldText with newText.
    
    Args:
        text (string) 
        oldText (substring)
        newText (substring)
    
    Returns:
        string: text with replaced substrings
            
    """
    replacedText = ""
    i = 0
    while i < len(text):
        if text[i:i+len(oldText)] != oldText:
            replacedText += text[i:i+1]
            i += 1
        else:
            replacedText += newText 
            i += len(oldText)
            
    return replacedText  
    
        