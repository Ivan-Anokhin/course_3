from func import get_data, sort_data, transform_date, mask_data

get_data = get_data()
sorted_data = sort_data(get_data)
for i in sorted_data[:5]: # цикл задает количество последних операций для вывода
    date = transform_date(i)
    from_ = mask_data(i.get('from'))
    to_ = mask_data(i.get('to'))
    print(f"{date} {i.get('description')}\n"
            f"{from_} => {to_}\n"
            f"{i.get('operationAmount')['amount']} "
            f"{i.get('operationAmount')['currency']['name']}\n")