def decode_message(number, key):
    substrings = []
    t = 0
    for i in str(key):
        v = int(i)
        substrings.append(number[t:t+v])
        t += v

    decoded_message = ''
    for substring in substrings:
        if substring.isdigit():
            number = int(substring)
            if 1 <= number <= 26:
                char = chr(ord('a') + number - 1)
                decoded_message += char
            else:
                decoded_message += '?'
        else:
            decoded_message += '?'
    return decoded_message


while True:
    number = input("Enter the number to decode (type 'exit' to quit): ")
    
    if number.lower() == 'exit':
        break

    key = input("Enter the key: ")

    decoded_message = decode_message(number, key)
    print("Decoded message:", decoded_message)