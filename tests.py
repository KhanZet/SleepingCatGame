

def frameMsg(msg, firstSymbol, secondSymbol):
    lineMsg = (firstSymbol + secondSymbol) * int(len(msg) / 1.5)
    if list(lineMsg)[-1] == secondSymbol:
        lineMsg += firstSymbol
    spaceLen = (len(lineMsg) - len(msg) - 2) // 2
    outputMessage = firstSymbol + ' ' * spaceLen + msg + spaceLen * ' '
    if len(outputMessage) % 2 == 1:
        outputMessage += ' ' + firstSymbol
    else:
        outputMessage += firstSymbol
    print(lineMsg)
    print(outputMessage)
    print(lineMsg)

# Пример использования функции с новыми символам

frameMsg('Привет мама, я тебя очень люблю!', '+', '^')
