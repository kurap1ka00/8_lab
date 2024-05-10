def a3(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic_numeral = 0
    prev_value = 0

    for numeral in roman_numeral:
        value = roman_dict[numeral]
        if value > prev_value:
            arabic_numeral += value - 2 * prev_value
        else:
            arabic_numeral += value
        prev_value = value

    return arabic_numeral
if __name__=="__main__":

    arabic_result = a3("IV")
    print(arabic_result)

    arabic_result = a3("III")
    print(arabic_result)  