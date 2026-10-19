Patient Record Management System
A beginner-friendly Python console application developed for the PROG211 Object-Oriented Programming 1 assignment. 
It demonstrates object-oriented programming (OOP), a Python list, instance methods, a class method, 
and interaction between objects.

Features
Add a patient record.
Display all registered patients.
Create an appointment for a selected patient.
Update a patient's age, name, or ID.
Display doctor and appointment information.
Basic input validation.

Requirements
Python 3.8 or later
No third-party packages are required.

How to run
Save patient_record_management_system.py to your computer.
Open a terminal or command prompt in that folder.
Run:
python patient_record_management_system.py
On some systems, use python3 instead of python.

Example usage
PATIENT RECORD MANAGEMENT SYSTEM
System: Patient Record Management System

1. Add Patient
2. Display Patients
3. Create Appointment
4. Update Patient Age
5. Update Patient Name
6. Update Patient ID
7. Exit
Choose an option by entering its number and follow the prompts. For example, select 1 to add a patient, then select 2 to display the saved patient during the current run.

OOP concepts used
Classes: Patient, Doctor, and Appointment.
Objects: Instances of these classes represent individual records.
Attributes: Store IDs, names, age, specialization, and appointment date.
Instance methods: display_info(), update_age(), update_name(), update_id(), and display_appointment().
Class attribute and class method: system_name and get_system_name().
Object interaction: An Appointment object refers to a Patient object and a Doctor object.
Data structure: One list, patients, stores multiple Patient objects.

Digital Public Goods (DPG) alignment
Open source: The source code can be published in a public GitHub repository with a suitable open-source licence.
Inclusive and accessible: Uses a simple text menu and clear prompts.
Privacy-respecting: The demonstration stores no sensitive medical details and does not save records to a permanent database. Use fictional/sample information for demonstrations.
Modular and reusable: The program separates classes and menu functions so the code can be extended.

Sustainable Development Goal (SDG) Supported
The Patient Record Management System supports Sustainable Development Goal 3 (SDG 3): Good Health and Well-being.
This goal aims to ensure healthy lives and promote well-being for all. 
The system contributes to this goal by organising basic patient information, displaying patient records, and supporting appointment management between patients and doctors.
These features can help improve the organisation and accessibility of healthcare information. Although the system is a basic educational prototype,
it demonstrates how information technology can support healthcare administration and contribute to better healthcare services.

Limitations
Records are held in memory and are lost when the program closes.
This is an educational prototype, not a production healthcare system.
It does not provide authentication, access control, encryption, or clinical decision support. Do not enter real patient information.
The example uses one demonstration doctor and simple appointment IDs.
