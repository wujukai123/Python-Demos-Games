import random
import string
adjectives=['sleepy','slow','smelly','wet','fat','thin','fast','red','orange','yellow','green','blue','purple','fluffy','white','black','proud','brave','yummy','quickly']
nouns=['apple','banana','dinosaur','ball','table tennis','toaster','goat','sheep','cow','tiger','lion','elephant','ant','fly','water','dragon','hammer','duck','panda','feet','hand','hair']
verbs=['run','walk','jump','play','plant','water','geton','getoff','move','drive','ride','sit','backward','sing','shoot','say','shout','put','point','knock','cry']
places=['inthe river','inthespace','intheTV','onthetable','onthechair','onthebus','onthedrive','underthefloor','nexttotheclassroom']
print('Welcome to Password Picker!')
while True:
    adjective=random.choice(adjectives)
    noun=random.choice(nouns)
    verb=random.choice(verbs)
    place=random.choice(places)
    number=random.randrange(0,1000)
    special_char=random.choice(string.punctuation)
    password=adjective+noun+verb+place+str(number)+special_char
    print('Your new password is:%s'%password)
    response=input('Would you like another password?Type y or n:')
    if response=='n':
        break
