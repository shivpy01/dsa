def anagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s = s.replace(' ', '').lower()
    t = t.replace(' ', '').lower()

    if (len(s) != len(t)):
        return False
    counter = {}
    for letter in s:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

    for letter in t:
        if letter in counter:
            counter[letter] -= 1
        else:
            return False

    for k in counter:
        if counter[k] != 0:
            return False

    return True

print(anagram("dog","god"))

