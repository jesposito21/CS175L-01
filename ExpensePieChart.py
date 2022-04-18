import matplotlib.pyplot as mpl


def main():
    file= open('expenses.txt','r')
    labels=[]
    values=[]
    for line in file.readlines():
        line=line.replace('Payment', '')
        labels.append(str(line.split()[0]))
        values.append(int(line.split()[1]))
    mpl.pie(values, labels=labels, colors=('c','y','b','r','m','g'))
    mpl.show()


main()
