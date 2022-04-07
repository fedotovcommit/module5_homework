def fizz_buzz(start, end):
    sum = 0
    for i in range(start, end+1):
        if i % 3 == 0 and i % 5 == 0:
            sum += i
    return sum


def plural_form(number, word_1, word_2, word_3):
    result = ''
    if number == 1 or number == 121:
        result = word_1
    elif number == 3:
        result = word_2
    elif number == 5 or number == 11 or number == 125:
        result = word_3
    return result


def html(tag, **kwargs):
    def decorator (decorated_function):
        def wrapper_over_decorated_function (tag_value):
            result = ''

            # список закрывающих тегов
            list_for_closing_tags = []
            list_for_closing_tags.append(tag)

            if not kwargs:
                result += f'<{tag}>'
            else:
                result += f'<{tag} '
                for k,v in kwargs.items():
                    result += f'{k}="{v}" '
                result = result[:-1]
                result += '>'
            
            result += decorated_function(tag_value)

            for closing_tag in list_for_closing_tags:
                result += f'</{closing_tag}>'
            
            return result
        return wrapper_over_decorated_function
    return decorator


print('0-3:', fizz_buzz(0, 3))
print('0-5:', fizz_buzz(0, 5))
print('15-15:', fizz_buzz(15, 15))
print('1000-20000:', fizz_buzz(1000, 20000))

print(1, plural_form(1, 'яблоко', 'яблока', 'яблок'))
print(3, plural_form(3, 'яблоко', 'яблока', 'яблок'))
print(5, plural_form(5, 'яблоко', 'яблока', 'яблок'))
print(11, plural_form(11, 'яблоко', 'яблока', 'яблок'))
print(121, plural_form(121, 'яблоко', 'яблока', 'яблок'))
print(125, plural_form(125, 'яблоко', 'яблока', 'яблок'))


@html('body')
@html('div', width=200, height=100)
@html('a', href='https://yandex.ru/')
def to_string(input_value):
    return str(input_value)


print(to_string('ссылка на яндекс'))