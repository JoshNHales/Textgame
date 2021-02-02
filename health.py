health = 10
hp = 10 
def health(num) :
    global hp
    hp -= num
    print(hp)

health(3)
health(4)