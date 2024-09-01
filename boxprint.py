def boxprint(symbol, width, height):
    if len(symbol)!=1:
        raise Exception('"Symbol" needs to be a string of length 1')
    if width < 2 or height < 2:
        raise Exception('"Width" and "Height" should be greater or equal to 2')
    print(symbol*width)
    for i in range(height-2):
        print(symbol+' ' *(width-2)+symbol)
    print(symbol * width)

#boxprint("**", 16, height=6)
boxprint(symbol="o",width=4,height=4)
######
