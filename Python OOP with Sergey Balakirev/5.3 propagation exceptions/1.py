def input_int_numbers(s):
    return tuple(map(int, s))


while True:
    try:
        m = input_int_numbers(input().split())
    except:
        pass

    else:
        print(*m)
        break
