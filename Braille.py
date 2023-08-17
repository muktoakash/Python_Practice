def Braille(s):
    # Converts text to braille
    alphabet = dict()
    string = "The quick brown fox jumps over the lazy dog"
    braille = "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
    index = 6;
    for letter in string:
        alphabet[letter] = braille[index:index+6]
        index += 6
    
    ret = ""
    
    for c in s:
        if c.isupper():
            ret += braille[0:6] # Marker for capitalization
        
        ret += alphabet[c.lower()]
    
    return ret

def main():
    #Tests
    assert Braille("The quick brown fox jumps over the lazy dog") == "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
    assert Braille("Braille") == 000001110000111010100000010100111000111000100010
    assert Braille("code") == "100100101010100110100010"

if __name__ == __main__:
    main()
