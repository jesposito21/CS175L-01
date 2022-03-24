'''
Jenna Esposito
CS175L
Average From Input File
'''
def main():
    openFile=open('numbers.txt','r')

    #openFile.close

    total=0.0
    count=0
    for line in openFile:
        number=float(line)
        total=total+number
        print(f'Current number is: {number:.2f}','Total is: ',total)    
      
    avg=total/3
    print('Average: ',avg)


if __name__=='__main__':
    main()
