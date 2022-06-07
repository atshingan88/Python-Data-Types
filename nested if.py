model = input('enter mobile model you wish')
RAM= (input('enter ram in gb'))
if model is "Nokia" :
    if RAM is 4 :
      print('cost is Rs. 8000')
    elif RAM is 6 :
        print('cost is Rs. 9000')
    elif RAM is 8 :
        print('cost is Rs. 10000')
else:
    print('Sorry we cant help u')
