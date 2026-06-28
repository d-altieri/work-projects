### Omnibus maintenance template ###

number_of_sites = int(input('How many hub sites? '))

output = []
nest_output = []

while number_of_sites > 0:
    hubs = input('Enter Hub ID: ').upper()
    sectors = input('Enter affected sectors: ').split(' ')
    output.append(f'{hubs}')
    nest_output.append(f'{hubs}')
    for sector in sectors:
        output.append(f'{hubs}_{sector}1LAB - 2100 | 1900 | LAA')
        nest_output.append(f'{hubs}_{sector}1LAB')
        continue
    output.append('')
    number_of_sites -= 1


print("Alarms:\n\n")
print("Sites put into NEST:")
print(*nest_output, sep='\n')
print("\n\nFollowing sectors and frequencies have been locked:\n")
print(*output, sep='\n')
