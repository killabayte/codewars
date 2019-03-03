def tickets(people):
    a = people.count(25)
    b = people.count(50)
    c = people.count(100)
    if (b-a <= 0) and ((a-b-min(b,a-b))/3 + min(b,a-b) >= c):
        return 'YES'
    else:
        return 'NO'