'''
Jenna Esposito
CS175L
Restaurant Program
'''
vegetarian=False
vegan=False
gluten_free=False
keep_going='yes'

while keep_going=='yes':
    response1=input('Is anyone is your party a vegetarian? ')
        
    response2=input('Is anyone in your party vegan? ')

    response3=input('Is anyone in your party gluten-free? ')

    print('Here are your restaurant choices: ')

    if response1=='Yes' or response1=='yes':
        print('Corner Cafe')
    if response2=='Yes' or response2=='yes':
        print('The Chef\'s Kitchen')
    if response3=='Yes' or response3=='yes':
        print('Main Street Pizza Company')
        print('Mama\'s Fine Italian')
    if (response1=='No' or response1=='no') and (response3=='No' or response3=='no'):
        print('Joe\'s Gourmet Burgers')
        print('Mama\'s Fine Italian')
        print('The Chef\'s Kitchen')
        print('Corner Cafe')
        print('Main Street Pizza Company')

    keep_going=input('Would you like to get more restaurant choices? ')

print('Goodbye!')
    



