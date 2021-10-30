def zero_args_test(func):
    def testing(_, *args):
        if len(args) > 0:
            return func(_, *args)
        else:
            return('Нет аргументов, вызов {} невозможен'.format(func.__name__))   
        
    return testing


@zero_args_test
def field(items, *args):
    request = list()
    if len(args) == 1:
        for each_dict in items:
            if args[0] in each_dict:
                request.append(each_dict[args[0]])
    else:   
        for each_dict in items:
            temp_dict = {}
            for key in each_dict:
                if (key in args):
                    temp_dict[key]=each_dict[key]
            request.append(temp_dict)
    return request


def main():

    goods = [
        {'title': 'Ковер',   'price': 2000,  'color': 'Зеленый'},
        {'title': 'Диван',   'price': 5300,  'color': 'Желтый'},
        {'title': 'Кресло',  'price': 1000,  'color': 'Красное', 'used': True},
        {'title': 'Лампа',   'price': 500,   'power':'50w'},
        {'title': 'Зеркало', 'price': 800,   'used': True},
        {'title': 'Чайник',  'price': 200,   'power':'50w',      'used': False},
    ]

    
    print(field(goods), '\n\n')
    print(field(goods, 'title'), '\n\n')
    print(field(goods, 'title', 'price'), '\n\n')
    print(field(goods, 'title', 'used'), '\n\n')



if __name__ == "__main__":
    main()



