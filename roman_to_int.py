def romanToInt(s):
    map = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    summ = 0
    i = 0
    n = len(s)

    while i < n:
        if i < n - 1 and map[s[i]] < map[s[i + 1]]:
            summ += map[s[i + 1]] - map[s[i]]
            i += 2
        else:
            summ += map[s[i]]
            i += 1
    return summ


# Test cases
# Test 1: Roman numeral "III" = 3
print(romanToInt("III"))  # Expected output: 3

# Test 2: Roman numeral "IV" = 4 (I before V indicates subtraction)
print(romanToInt("IV"))  # Expected output: 4

# Test 3: Roman numeral "IX" = 9 (I before X indicates subtraction)
print(romanToInt("IX"))  # Expected output: 9

# Test 4: Roman numeral "LVIII" = 58 (L = 50, V = 5, III = 3)
print(romanToInt("LVIII"))  # Expected output: 58

# Test 5: Roman numeral "MCMXCIV" = 1994 (M = 1000, CM = 900, XC = 90, IV = 4)
print(romanToInt("MCMXCIV"))  # Expected output: 1994
