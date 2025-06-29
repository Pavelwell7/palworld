from transliterate import translit


print(translit("Lorem ipsum dolor sit amet", 'hy'))  # Выведет Լօրեմ իպսում դօլօր սիտ ամետ
print(translit("Lorem ipsum dolor sit amet", 'el'))  # Выведет Λορεμ ιψυμ δολορ σιτ αμετ
print(translit("Lorem ipsum dolor sit amet", 'uk'))  # Выведет Лорем іпсум долор сіт амет