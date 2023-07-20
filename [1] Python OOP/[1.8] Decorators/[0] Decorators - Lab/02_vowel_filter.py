def vowel_filter(function):
    vowels = "AOUEIYaoueiy"

    def wrapper():
        letters = function()
        return [x for x in letters if x in vowels]

    return wrapper

# Different solution:

# def vowel_filter(function):
#     VOWELS = "aeiou"
#
#     def wrapper():
#         return [l for l in function() if l in VOWELS]
#
#     return wrapper
#
#
# @vowel_filter
# def get_letters():
#     return ["a", "b", "c", "d", "e"]
#
#
# print(get_letters())
