with open('recipes.txt', 'w', encoding='utf-8') as f:
    f.write('''Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г

Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт''')
    f.close()

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        quantity_ingredient = int(file.readline())
        ingredients = []
        for ingredient in range(quantity_ingredient):
            name, quantity, measure = file.readline().strip().split('|')
            ingredients.append({
                'ingredient_name': name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish.strip()] = ingredients

def get_shop_list_by_dishes(dishes, person_count):
    ingrediend_to_cooking = {}
    dish = []
    for i in dishes:
        dish.append(cook_book[i])
    for j in dish:
        for i in j:
            if i['ingredient_name'] not in ingrediend_to_cooking:
                ingrediend_to_cooking[i['ingredient_name']] = {'measure': (i['measure']), 'quantity': (int(i['quantity']) * person_count)}
            else:
                q = int(i['quantity']) * person_count
                ingrediend_to_cooking[i['ingredient_name']] = {'measure': (i['measure']),
                                                               'quantity': (q + int(i['quantity']) * person_count)}
    return ingrediend_to_cooking

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

    