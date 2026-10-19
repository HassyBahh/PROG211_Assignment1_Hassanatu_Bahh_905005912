
# PATIENT RECORD MANAGEMENT SYSTEM
# Object-Oriented Programming 1 Assignment
# CLASS 1: PATIENT

class Patient:
    system_name = "Patient Record Management System"

    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age

    # Instance method
    def display_info(self):
        print("\n--- Patient Information ---")
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)

    # Instance method
    def update_age(self, new_age):
        self.age = new_age
        print("Patient age updated successfully.")
    def update_ID(self, new_ID):
        self.patient_id = new_ID 
        print("patient ID has been updated successfully")

    # Class method
    @classmethod
    def get_system_name(cls):
        return cls.system_name

# CLASS 2: DOCTOR
class Doctor:

    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    # Instance method
    def display_info(self):
        print("\n--- Doctor Information ---")
        print("Doctor ID:", self.doctor_id)
        print("Name:", self.name)
        print("Specialization:", self.specialization)

# CLASS 3: APPOINTMENT
class Appointment:

    def __init__(self, appointment_id, patient, doctor, date):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date

    # Instance method
    def display_appointment(self):
        print("\n--- Appointment Information ---")
        print("Appointment ID:", self.appointment_id)
        print("Patient:", self.patient.name)
        print("Doctor:", self.doctor.name)
        print("Specialization:", self.doctor.specialization)
        print("Date:", self.date)


patients = []


def add_patient():
    print("\n--- Add New Patient ---")

    patient_id = input("Enter patient ID: ")
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))

    patient = Patient(patient_id, name, age)

    patients.append(patient)

    print("\nPatient added successfully!")



def display_patients():

    if len(patients) == 0:
        print("\nNo patients have been registered.")
        return

    print("\n===== ALL PATIENTS =====")

    for patient in patients:
        patient.display_info()


def create_appointment():

    if len(patients) == 0:
        print("\nPlease add a patient first.")
        return

    print("\n--- Create Appointment ---")

    # Use the first patient from the list
    patient = patients[0]

    doctor = Doctor(
        "D001",
        "Dr. Hassanatu",
        "General Medicine"
    )

    appointment = Appointment(
        "A001",
        patient,
        doctor,
        "15 October 2026"
    )

    print("\nAppointment created successfully!")

    doctor.display_info()
    appointment.display_appointment()



def main():

    print("==========================================")
    print("   PATIENT RECORD MANAGEMENT SYSTEM")
    print("==========================================")

    # Demonstrate class method
    print("System:", Patient.get_system_name())

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Add Patient")
        print("2. Display Patients")
        print("3. Create Appointment")
        print("4. Update Patient Age")
        print("5. Update Patient ID")
        print("6. Exit")
        print(

        )

        choice = input("Enter your choice: ")

        # Add patient
        if choice == "1":
            add_patient()

        # Display patients
        elif choice == "2":
            display_patients()

        # Create appointment
        elif choice == "3":
            create_appointment()

        # Update patient
        elif choice == "4":

            if len(patients) == 0:
                print("\nNo patients available.")
            else:
                new_age = int(input("Enter new age: "))
                patients[0].update_age(new_age)



        # Exit
        elif choice == "5":
             if len(patients) == 0:
                print("\nNo patients available.")
             else:
                new_ID = int(input("Enter new ID: "))
                patients[0].update_ID(new_ID)
                    
        
        # Exit
        elif choice == "6":
            print("\nThank you for using the Patient Record Management System.")
            break
        else:
            print("\nInvalid choice. Please try again.")



if __name__ == "__main__":
    main()




        
    
            
