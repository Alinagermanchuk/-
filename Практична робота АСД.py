A = int(input("Введіть перший множник "))
B = int(input("Введіть другий множник "))

# Змінна для накопичення залишків

accumulation = 0
def multi(A,B):
    if A%2 == 0:
        global a,b
        a = int(A/2)
        b = B * 2
        print(a,b)
        if a == 1:
            global accumulation
            print("Сума залишків =", accumulation)
            print("Результат множення по-російськи =",accumulation+b)
        else:
            multi(int(A/(2)),int(B*2))
    elif A==1:
        print("Сума залишків =", accumulation)
        print("Результат множення по-російськи =",accumulation+b)
    elif A%2 == 1:
        accumulation += B
        a = int((A-1)/2)
        b = B * 2
        print(a,b)
        multi(int((A-1) / 2), int(B * 2))

multi(A,B)

