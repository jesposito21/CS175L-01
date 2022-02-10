#Jenna Esposito
#CS175
#Weather Station
station_name=input('Weather Station Name: ')
current_temp=float(input('What is the current temperature(Fahrenheit)? '))
wind_speed=float(input('What is the wind speed? '))
wind_direction=input('What is the wind direction? ')

TITLE=' Weather Station\n'
TEMP_F='Temperature (Fahrenheit):'
TEMP_C='Temperature(Celsius):'
WIND_MPH='Wind speed(mph):'
WIND_DIR='Wind direction:'
tempinc=(current_temp-32)*5/9

print('\n','\t',station_name +TITLE)
print(TEMP_F,current_temp)
print('   ',TEMP_C,f'{tempinc:.1f}')
print('        ',WIND_MPH,wind_speed)
print('        ',WIND_DIR,wind_direction)



      

      
