def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "Lastname": "García"}

    super_list = [
        {"firstname": "Facundo", "Lastname": "García"},
        {"firstname": "Miguel", "Lastname": "Torres"},
        {"firstname": "Pepe", "Lastname": "Rodelo"},
        {"firstname": "Susana", "Lastname": "Martínez"},
        {"firstname": "José", "Lastname": "García"},
    ]

    super_dict = {
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2, 0, 1, 2],
        "floating_nums":[1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for elemento in super_list:
        print(elemento)



if __name__ == '__main__':
    run()