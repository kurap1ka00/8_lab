def a4(*words):
    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)

    if len(words) < 2:
        return False

    first_word = words[0]
    for word in words[1:]:
        if not is_anagram(first_word, word):
            return False

    return True

if __name__=="__main__":

    result = a4("listen", "silent", "enlist")
    print(result)  