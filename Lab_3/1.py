# TODO Напишите функцию для поиска индекса товара

def id_tovara(sd, x):
    df = None
    for i in range(len(sd)):
        if sd[i] == x:
            df = i
            break
    return(df)




items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = id_tovara(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
