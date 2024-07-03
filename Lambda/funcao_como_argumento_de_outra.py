def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)

def first_last(first_name, last_name):
    return f"{first_name} {last_name}"

def last_first(first_name, last_name):
    return f"{last_name}, {first_name}"

print(get_full_name("mike", "wazowski", first_last))  # Passa a função `first_last` como argumento
print(get_full_name("mike", "wazowski", last_first))  # Passa a função `last_first` como argumento
