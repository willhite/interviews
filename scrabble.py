import urllib.request
words = urllib.request.urlopen("https://d2i1pl9gz4hwa7.cloudfront.net/7HvykrqVNLAyrVQATa9iBA").read().decode("utf-8").split()

def check_word(w, words):
    if w not in words:
        return None
    if len(w) == 2:
        res = []
    else:
        res = check_word(w[1:], words) or check_word(w[:-1], words)
    if res is not None:
        return [w] + res
    return None

def get_longest_words(words):
    swords = set(words)
    lwords = []
    llen = 0
    for w in words:
        if len(w) < llen:
            continue
        path = check_word(w, swords)
        if path:
            print("new longest:", w)
            if len(w) == llen:
                lwords.append(path)
            else:
                llen = len(w)
                lwords = [path]
    return lwords


# res = check_word('abactinally', swords)
# print("res:", res)
for i, w in enumerate(get_longest_words(words)):
    print(f"{i}: {w}")

