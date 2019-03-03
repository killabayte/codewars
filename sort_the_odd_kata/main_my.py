def sort_array(source_array):
    even_state = []
    new_source_array = []
    for one, two in enumerate(source_array):
        if two % 2 == 0:
            even_state.append((one,two))
        else:
            new_source_array.append(two)
    new_source_array.sort()
    for new_even in even_state:
        new_source_array.insert(new_even[0], new_even[1])
    return new_source_array