myimg = open('minion.jpg', mode ='rb')
myimgdata = myimg.read()
dupimg = open('duplicateminion.jpg', mode = 'wb')
dupminion = dupimg.write(myimgdata)
