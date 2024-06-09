from func import get_data, sort_data, transform_date, mask_data, print_data

get_data = get_data()
sorted_data = sort_data(get_data)
for i in sorted_data[:5]:
    date = transform_date(i)
    from_ = mask_data(i.get('from'))
    to_ = mask_data(i.get('to'))
    print_data(i, date, from_, to_)
