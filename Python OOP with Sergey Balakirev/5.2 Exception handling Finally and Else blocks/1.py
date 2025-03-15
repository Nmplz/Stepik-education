lst_in = input().split()

try:
    result = sum(int(x) for x in lst_in)
except:
    try:
        result = sum(float(x) for x in lst_in)
    except:
        result = "".join(lst_in)
finally:
    print(result)
