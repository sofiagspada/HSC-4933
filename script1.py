# Import the AnonyMate anonymizer function
from anonymate import anonymizer

# The 5 profiles
profiles = [
    {
        'job': 'Agricultural engineer',
        'company': 'Phillips-Johnson',
        'ssn': '055-51-3629',
        'residence': '1107 Brian Coves\nSouth Jessica, UT 66862',
        'current_location': ('-81.6575675', '111.794874'),
        'blood_group': 'B+',
        'website': ['https://hurley.com/', 'http://www.baker.info/',
                    'http://silva-jones.com/', 'https://www.mathews.com/'],
        'username': 'nnelson',
        'name': 'Oscar Newman',
        'sex': 'M',
        'address': '2574 Scott Manors\nPort Aprilfort, MI 13337',
        'mail': 'wgraham@hotmail.com',
        'birthdate': '1927-01-19'
    },
    {
        'job': 'Engineer, civil (consulting)',
        'company': 'Guzman Inc',
        'ssn': '457-09-3674',
        'residence': '8014 Lambert Ways Apt. 285\nSouth Briannaside, KS 13217',
        'current_location': ('61.686331', '-42.036583'),
        'blood_group': 'A-',
        'website': ['http://gregory-martin.org/', 'http://tanner.org/',
                    'https://www.carr.org/'],
        'username': 'lking',
        'name': 'Jeremy Wilson',
        'sex': 'M',
        'address': '9375 Thomas Alley Suite 536\nNorth Darren, AZ 22956',
        'mail': 'hdeleon@hotmail.com',
        'birthdate': '1996-10-12'
    },
    {
        'job': 'Information officer',
        'company': 'Green Inc',
        'ssn': '230-42-2169',
        'residence': 'Unit 6625 Box 0858\nDPO AE 52466',
        'current_location': ('-78.802646', '-47.996111'),
        'blood_group': 'A-',
        'website': ['https://www.watkins.com/', 'http://johnson.org/'],
        'username': 'timothycastro',
        'name': 'Kenneth Rhodes',
        'sex': 'M',
        'address': '7994 Pearson Square\nHannahmouth, FM 16699',
        'mail': 'sonya72@hotmail.com',
        'birthdate': '2003-06-15'
    },
    {
        'job': 'Contracting civil engineer',
        'company': 'Smith-Williamson',
        'ssn': '796-76-1297',
        'residence': '0041 Brittany Mountains\nNorth Harryshire, MN 69202',
        'current_location': ('66.422320', '107.124001'),
        'blood_group': 'AB+',
        'website': ['http://www.nolan.com/'],
        'username': 'debraphillips',
        'name': 'Nicole Richardson',
        'sex': 'F',
        'address': '303 Wong Trafficway Suite 883\nLake Kiara, MN 78039',
        'mail': 'andrew33@gmail.com',
        'birthdate': '2003-09-07'
    },
    {
        'job': 'Engineer, technical sales',
        'company': 'Moody-Meza',
        'ssn': '574-63-6422',
        'residence': '74438 Moore Fall\nSouth Andrew, GA 64257',
        'current_location': ('38.089195', '35.459581'),
        'blood_group': 'A+',
        'website': ['https://brooks-moore.com/'],
        'username': 'xlewis',
        'name': 'Gary Gamble',
        'sex': 'M',
        'address': '9929 Henderson Branch Suite 961\nLake Mary, AL 36478',
        'mail': 'ambercordova@yahoo.com',
        'birthdate': '1968-08-19'
    }
]


# Ask the user if they want to encrypt the profiles
encrypt_choice = input("Would you like to encrypt the data? (yes/no): ").lower()

if encrypt_choice == "yes":
    # Encrypt/anonymize the profiles using AnonyMate
    encrypted_profiles = anonymizer(profiles)

    print("\nData has been encrypted.")
else:
    encrypted_profiles = profiles
    print("\nData was not encrypted.")


# Allow the user to query the profiles
while True:

    print("\nWhat information would you like to search for?")
    print("1. Name")
    print("2. DoB")
    print("3. Sex")
    print("4. Blood Type")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Goodbye!")
        break

    if choice == "1":
        field = "name"
    elif choice == "2":
        field = "birthdate"
    elif choice == "3":
        field = "sex"
    elif choice == "4":
        field = "blood_group"
    else:
        print("Invalid choice. Please try again.")
        continue

    search_value = input("Enter the value you want to search for: ")

    found = False

    for profile in encrypted_profiles:
        if str(profile.get(field, "")).lower() == search_value.lower():
            print("\nProfile found:")
            print(profile)
            found = True

    if not found:
        print("\nNo matching profile was found.")
