def word_count(sentence, N=3):
  
    sentence = sentence.lower()
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for p in punctuation:
        sentence = sentence.replace(p, "")
    words = sentence.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:N]
