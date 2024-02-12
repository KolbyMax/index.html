def get_vowels(String):
    return [each for each in String if each in "aeiou"]
get_vowels("animal") # [r, g, b]
get_vowels("sky") # []
get_vowels("football") # [o, o, a]
print(get_vowels)
