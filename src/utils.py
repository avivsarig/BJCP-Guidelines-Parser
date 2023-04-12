def pretty_print(dictionary):
    for key, value in dictionary.items():
        print(f"{key}:")
        if(type(value) == dict or type(value) == list):
            pretty_print(value)
        else:
            print(value)
        print()