##fizzbuzz
def fizzbuzz (x):
    for i in range(1, x+1):
        if i%3==0 and i%5==0:
            print('fizz buzz')
        elif i %3== 0:
            print('fizz')
        elif i%5 ==0:
            print('buzz')
        else:
            print(i)
fizzbuzz(16)
