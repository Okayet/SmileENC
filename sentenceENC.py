#Creator Okayet/Deserved
#Give republishing the code with modifications
#smile it looks good on u :)
def convert_words_to_numbers(string):
    result = []
    combined_result = ""
    words = string.split()
    for word in words:
        converted_word = ' '.join(str(ord(c.lower()) - 96) for c in word if c.isalpha())
        result.append(converted_word)
        combined_result += converted_word
        combined_result += " "
    return ' '.join(result), ''.join(result).replace(" ", ""), combined_result.replace(" ", "")


def count_digits_in_numbers(string):
    result = []
    numbers = string.split()
    for number in numbers:
        count = str(len(number))
        result.append(count)
    return ''.join(result)


while True:
    input_string = input("Enter a sentence (type 'exit' to quit): ")

    if input_string.lower() == 'exit':
        break

    converted_numbers, combined_numbers, combined_numbers_alt = convert_words_to_numbers(input_string)
    print("converted numbers:", converted_numbers)
    print("combined numbers:", combined_numbers)
    print("combined numbers (Alternative):", combined_numbers_alt)
    digit_counts = count_digits_in_numbers(converted_numbers)
    print("key without key u suck hehe:", digit_counts)
