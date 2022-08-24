from date_master import date_master


date = [31, 12, 2022]
order = ['DD','MM','YYYY']
format = ['int','str','int']
split_by = ['|']


params = {
    'date':date,
    'order':order,
    'format':format,
    'split_by':split_by
}

result = date_master(params)
print(result)
