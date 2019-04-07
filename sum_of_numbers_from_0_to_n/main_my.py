def show_sequence(n):
    my_list = []
    if n > 0:
        for num in range(0, n+1):
            my_list.append(str(num))
        my_str = '+'.join(my_list)
        return f"{my_str} = {sum(range(0,n+1))}"
    elif n == 0:
        return f"{n}=0"
    else:
        return f"{n}<0"
