#Quiz
name=str(input('What is your name?  '))
questions=(('1.What is the largest continent'), ('2.How many oceans do we have?'),('3.What is 0!'),('4.What is the capital of China?'),('5.How many questions were asked' ))
answers=((('A.Africa'),('B.Australia'),('C.N. America'),('D.Asia')),
         (('A.2 '),('B.4'),('C.5'),('D.7')),
         (('A.1'),('B.0'),('C.Undefined'),('D.Nothingness')),
         (('A. Hong Kong'),('B.Beijing'),('C.Seoul'),('D. Tokyo')),
         (('A.4'),('B.3'),('C.Subjective'),('D.2')))
q_num=0
c_ans=['D','C','A','B','A']
score=0


for x in questions:
    print(x)
    for y in answers[q_num]:
        print(y)


    guess=input('What option is your pick? '+name+' :').upper()
    print()

    if c_ans[q_num]==guess:
        print('Correct!')
        score=score+1
    else:
        print('Incorrect!')
    q_num=q_num+1
    print('---------------------------------------------------------')

print('At the end of the day, you amassed a total score of '+str(score)+ ' mark(s)')
perc=(score/q_num)*100
print('This results to '+str(perc)+'%')
if perc>70:
    print('Good job!'+name)
elif perc>90:
    print('Excellent job done'+name)
else:
    print('Let us try harder next time'+name)
