from num2words import num2words
print(num2words(42))
print(num2words(42, to='ordinal'))
print(num2words(42, lang='fr')) 
from transliterate import translit
print('78', translit(num2words(78), 'ru'), sep=" - ",)
print('78', num2words(78), sep=" - ")
print('15', num2words(15), sep=" - ")
print('3', num2words(3), sep=" - ")
print('40', num2words(40), sep=" - ")
print('8', num2words(8), sep=" - ")

