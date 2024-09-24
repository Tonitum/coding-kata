def merge_alternate(word1: str, word2: str) -> str:
    return_word = ""
    if len(word1) > len(word2):
        for i in range(len(word2)):
            return_word = return_word + word1[i] + word2[i]
        return_word = return_word + word1[len(word2):]
    else:
        for i in range(len(word1)):
            return_word = return_word + word1[i] + word2[i]
        if len(word2) > len(word1):
                return_word = return_word + word2[len(word1):]

    return return_word


