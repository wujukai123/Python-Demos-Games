print('Only integer calculations are supported')
while True:
    x=input('Please enter an operation symbol:')
    if x==+:
        a=input('Please input a number:')
        a=int(a)
        b=input('Please input a number:')
        b=int(b)
        print('The final answer is:'+a+b)
    if x==-:
        a=input('Please input a number:')
        a=int(a)
        b=input('Please input a number:')
        b=int(b)
        print('The final answer is:'+a-b)
    if x==*:
        a=input('Please input a number:')
        a=int(a)
        b=input('Please input a number:')
        b=int(b)
        print('The final answer is:'+a*b)
    if x==/:
        a=input('Please input a number:')
        a=int(a)
        b=input('Please input a number:')
        b=int(b)
        print('The final answer is:'+a/b)
