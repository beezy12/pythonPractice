

def divide_by(num):
    try:
        return 42 / num
    except ZeroDivisionError:
        print('invalid')

print(divide_by(13))
print(divide_by(0))
print(divide_by(67))
