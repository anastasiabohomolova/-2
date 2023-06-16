base = [1, 5 ,6 ,34, 'hello', 678494, 434, 'Haluna', 34354]

menu = input('Виберіть одну дію: append, index, remove, insert: ')
choice_type = input('int or str: ')


if menu == 'append' and choice_type == 'str':
    ch_index = int(input('Виберіть index для елемента?: '))
    ch_el = input('Напишіть елемент: ')
    for el in base:
        if el == ch_el:
            print('Цей елемент вже є в списку')
            que = input('Продоовжуємо далі?: ')
    if  ch_el != el or que == 'так':
        base.append(ch_el)
        base.insert(ch_index, ch_el)
    
elif menu == 'append' and choice_type == 'int':
    ch_index = int(input('Виберіть index для елемента?: '))
    ch_el = int(input('Напишіть елемент: '))
    for el in base:
        if el == ch_el:
            print('Цей елемент вже є в списку: ')
            que = input('Продовжуємо далі?:')
    if  ch_el != el or que == 'так':
        base.append(int(ch_el))
        base.insert(ch_index, int(ch_el))
    
elif menu == 'insert' and choice_type == 'str':
    ch_index = int(input('Виберіть index для елемента?: '))
    ch_el = input('Напишить елемент: ')
    for el in base:
        if el == ch_el:
            print('Цей елемент вже є в списку: ')
            que = input('Продовжуємо далі?:')
    if ch_el != el or que == 'так':
        base.insert(ch_index, ch_el)
    
elif menu == 'insert' and choice_type == 'int':
    ch_index = int(input('Виберіть index для елемента?: '))
    ch_el = int(input('Напишіть елемент: '))
    for el in base:
        if el == ch_el:
            print('Цей елемент вже є в списку: ')
            que = input('Продовжуємо далі?:')
    if ch_el != el or que == 'так':
        base.insert(ch_index, int(ch_el))

elif menu == 'remove' and choice_type == 'int':
    ch_el = int(input('Напишіть елемент: '))
    base.remove(ch_el)

elif menu == 'remove' and choice_type == 'str':
    ch_el = input('Напишіть елемент: ')
    base.remove(ch_el)
 
elif menu == 'index' and choice_type == 'int':
    ch_index = int(input('Виберіть елемент: '))
    print(base.index(ch_index))
                     
elif menu == 'index' and choice_type == 'str':
    ch_index = input('Виберіть елемент: ')
    print(base.index(ch_index))
        
                               
print(base)


