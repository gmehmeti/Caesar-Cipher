class Ceaser():
    def __init__(self, shift_key):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.shiftKey = shift_key

    def EncryptMessage(self, message: str):
        message = message.strip()
        result = ""
        if self.shiftKey < 0 or self.shiftKey > 26:
            raise Exception("Shift Key is not valid!")

        if len(message) == 0:
            raise Exception("Message should not be empty!")

        alphabet_len = len(self.alphabet)-1

        for n in message:
            if n.lower() in self.alphabet:
                current_index = self.alphabet.index(n.lower())
                shift_index = current_index + self.shiftKey
                shift_index = shift_index % 26
                # if shift_index > alphabet_len:
                #     shift_index = shift_index - alphabet_len - 1

                # print(f"Index {current_index}, shiftindex {shift_index} ")
                letter = self.alphabet[shift_index]
                if n.islower():
                    result += letter.lower()
                else:
                    result += letter.upper()
            else:
                result += n

        return result

    def DecryptMessage(self, message: str):
        message = message.strip()
        result = ""
        if self.shiftKey < 0 or self.shiftKey > 26:
            raise Exception("Shift Key is not valid!")

        if len(message) == 0:
            raise Exception("Message should not be empty!")

        alphabet_len = len(self.alphabet)-1
        for char in message:
            if char.lower() in self.alphabet:
                current_index = self.alphabet.index(char.lower())
                shift_index = current_index - self.shiftKey
                shift_index = shift_index % 26
                # if shift_index < 0:
                #     shift_index = alphabet_len + shift_index + 1

                # print(f"Index {current_index}, shiftindex {shift_index} ")
                if(shift_index < 0):
                    shift_index *= -1

                letter = self.alphabet[shift_index]
                if char.islower():
                    result += letter.lower()
                else:
                    result += letter.upper()
            else:
                result += char

        return result
