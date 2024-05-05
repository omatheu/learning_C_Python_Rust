numbers = [1,2,3,4,5,6]
double = lambda x: x*2

# print(double(5))

double = map(lambda x: x*2, numbers)
print(double) # Return: <map object at 0x7f7c1818b400>
print(list(double))

# ------------------------------------------------------------ #
# Another step for learning used lambda functions
# ------------------------------------------------------------ #

pairs = filter(lambda pair: pair % 2 == 0, numbers)
# pairs = lambda pair: pair % 2 == 0

print(list(pairs))

# ------------------------------------------------------------ #
# Another step for learning used lambda functions
# ------------------------------------------------------------ #

words = ['banana', 'uva', 'maçã', 'goiaba', 'melancia', 'mamão', 'abacaxi']

#sorted_words = sorted(words) # ordered all words in alphabetical order

sorted_words = sorted(words, key=lambda x: len(x))

print(sorted_words)