'''
Jenna Esposito
CS175L
Average and Grade Assignment
'''
def calc_average(grade1,grade2,grade3,grade4,grade5):
    grade1=int(input('Please enter the first test score: '))
    grade2=int(input('Please enter the second test score: '))
    grade3=int(input('Please enter the third test score: '))
    grade4=int(input('Please enter the fourth test score: '))
    grade5=int(input('Please enter the fifth test score: '))
    return(grade1,grade2,grade3,grade4,grade5)
    determine_grade(g1,g2,g3,g4,g5)

def determine_grade(g1,g2,g3,g4,g5):
#grade 1
    if g1<101 and g1>89:
        g1='A'
    if g1<90 and g1>79:
        g1='B'
    if g1<80 and g1>69:
        g1='C'
    if g1<70 and g1>59:
        g1='D'
    if g1<60 and g1>0:
        g1='F'
    return g1
    #grade 2
    if g2<101 and g2>89:
        g2='A'
    if g2<90 and g2>79:
        g2='B'
    if g2<80 and g2>69:
        g2='C'
    if g2<70 and g2>59:
        g2='D'
    if g2<60 and g2>0:
        g2='F'
    return g2
    #grade 3
    if g3<101 and g3>89:
        g3='A'
    if g3<90 and g3>79:
        g3='B'
    if g3<80 and g3>69:
        g3='C'
    if g3<70 and g3>59:
        g3='D'
    if g3<60 and g3>0:
        g3='F'
    return g3
    #grade 4
    if g4<101 and g4>89:
        g4='A'
    if g4<90 and g4>79:
        g4='B'
    if g4<80 and g4>69:
        g4='C'
    if g4<70 and g4>59:
        g4='D'
    if g4<60 and g4>0:
        g4='F'
    return g4
    #grade 5
    if g5<101 and g5>89:
        g5='A'
    if g5<90 and g5>79:
        g5='B'
    if g5<80 and g5>69:
        g5='C'
    if g5<70 and g5>59:
        g5='D'
    if g5<60 and g5>0:
        g5='F'
    return g5
    average=(grade1+grade2+grade3+grade4+grade5)/5
    if (average<101) and (average>89):
        average='A'
    if (average<90) and (average>79):
        average='B'
    if (average<80) and (average>69):
        average='C'
    if (average<70) and (average>59):
        average='D'
    if (average<60) and (average>0):
        average='F'
    average_score=(grade1+grade2+grade3+grade4+grade5)/5
    return(g1,g2,g3,g4,g5)
    
def main():
    calc_average(grade1,grade2,grade3,grade4,grade5)
    determine_grade(g1,g2,g3,g4,g5)
    print('Score\t\tNumeric Grade\tLetter Grade')
    print('-------------------------------------------')
    print('Score 1: ',g1,grade1)
    print('Score 2: ',g2,grade2)
    print('Score 3: ',g3,grade3)
    print('Score 4: ',g4,grade4)
    print('Score 5: ',g5,grade5)
    print('Average score: ',average_score,average)

main()

