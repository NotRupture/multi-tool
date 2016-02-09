import urllib2

print('..:: Ruptures Social Network Tool ::..')
print('Here are your options:')
print()
print('1) Skype Resolver')
print('2) CloudFlare Resolver')
print('3) IP GEO-Lookup')
print('4) IP2Skype')
print('5) Skype DB Lookup')
print('6) Exit')

choice = input('Please choose a option: ')
loop = 1

while loop == 1:
        choice = int(choice)
        msg = 'Please wait... fetching the output now.'
        
        if choice == 1:
                ALIAS = raw_input('Please enter skype username: ')
                print(msg)
                response = urllib2.urlopen('http://APIOnly.com/skype.php?username=' + ALIAS)
                page = response.read()
                print page
        elif choice == 2:
                CF = raw_input('Please enter without http://: ')
                print(msg)
                response = urllib2.urlopen('http://APIOnly.com/cfresolver.php?domain=' + CF)
                page = response.read()
                print page
        elif choice == 3:
                GEO = raw_input('Please enter your targets IP address: ')
                print(msg)
                response = urllib2.urlopen('http://APIOnly.com/geolocator.php?ip=' + GEO)
                page = response.read()
                print page
        elif choice == 4:
                IPSK = raw_input('Please enter IP to match skypes: ')
                print(msg)
                response = urllib2.urlopen('hhttp://api.predator.wtf/lookup/?arguments=' + IPSK)
                page = response.read()
                print page
        elif choice == 5:
                GEO = raw_input('Please enter IP: ')
                print(msg)
                response = urllib2.urlopen('http://api.predator.wtf/lookup/?arguments=' + GEO)
                page = response.read()
                print page
        elif choice == 6:
                loop = 0
        else:
            print('Incorrect Input')
