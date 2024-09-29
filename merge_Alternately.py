def mergeAlternately(word1,word2):
    output = ""
    for i in range (min(len(word1),len(word2))):
        output += word1[i]
        output += word2[i]
    if len(word2) > len(word1):
        output += word2[len(word1)-len(word2):]
    elif len(word2) < len(word1):
        output += word1[len(word2)-len(word1):]
    return output

print(mergeAlternately("abc", "defg"))  # Output: "adbcefg"