from statistics import mean

heart_rate_samples = {
"J. Alvarez": [72, 75, 78],
"M. Chen": [80, 82],
"R. Okafor": [65, 68, 70, 66],
"S. Patel": [90, 95, 92, 88, 91],
"T. Nguyen": [77, 79],
"L. Kowalski": [68, 70, 69],
"D. Osei": [98, 101, 95, 99],
"A. Whitfield": [74, 76, 75, 73],

}

def patient_name(patient_number):
    patients = list(heart_rate_samples.keys())
    return patients[patient_number]

# I am assigning a patient number to each patient name
# starting at 0

def patient_stats(patient_number, *args):
    name = patient_name(patient_number)
    heart_rates = heart_rate_samples[name]

    results = {}

    patients = list(heart_rate_samples.keys())

    print("Patient List:")

    for number in range(len(patients)):
        print(number, "-", patients[number])

    patient_number = int(input("\nEnter a patient number: "))

    name = patient_name(patient_number)

    print("\nPatient:", name)
    print("Heart Rate Values:", heart_rate_samples[name])

    choice = input("\nWould you like to calculate the mean? Enter yes or no: ").lower()

    if choice == "yes":
        result = patient_stats(patient_number, "mean")
        print("Mean Heart Rate:", result["mean"])

    else:
        print("Program ended.")