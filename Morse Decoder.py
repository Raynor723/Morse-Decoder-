MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code):
    code1 = code.split(' ')
    decryption = []
    string = ''
    repetition = 0
    for word in range(len(code1)):
        if code1[word] == '':
            decryption.append(' ')
            repetition += 1
            if repetition == 2:
                decryption.pop()
                repetition = 0
        for x, y in MORSE.items():
            if code1[word] == x:
                decryption.append(y)
    for x in decryption:
        string += x
    print(string.capitalize())
    return string.capitalize()


if __name__ == "__main__":
    assert (morse_decoder("... --- ..."))
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
