'''
Jenna Esposito
CS175L
Average From Input File
'''
'''
def main():

    total=0.0
    count=0
    for line in openFile:
        number=float(line)
        total=total+number
        print(f'Current number is: {number:.2f}','Total is: ',total)    
      
    avg=total/3
    print('Average: ',avg)
'''
'''
def main():
    total=0.0
    get_val(total)
    
    calc_avg(total,avg)
    print_avg(avg)
def get_val(total):
    try:
        openFile=open('numbers.txt','r')
        total=0.0
        for line in openFile:
            number=float(line)
            total=total+number
    except IOError:
        print('An error ocurred while running.')
    return total
def calc_avg(total,avg):
    avg=total/3
    return avg
def print_avg(avg):
    print('Average: ',avg)
'''
def main():
     try:
        openFile=open('numbers.txt','r')
        total=0.0
        for line in openFile:
            number=float(line)
            total=total+number
        avg=total/3
        print('Average: ',avg)
     except IOError:
        print('An error ocurred while running.')
if __name__=='__main__':
    main()
