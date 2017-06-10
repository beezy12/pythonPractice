
def spam():
    global eggs
    eggs = 'spam'
    eggs = 'global'
    spam()
    print(eggs)

# couldnt get this to work
