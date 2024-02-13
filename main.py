def get_vowels(String):
    return [each for each in String if each in "aeiou"]
get_vowels("animal") # [r, g]
get_vowels("sky") # []
get_vowels("football") # [o, o]
print(get_vowels)
