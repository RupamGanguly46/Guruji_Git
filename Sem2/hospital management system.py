class Patient:
    def __init__(self,patient_id,name,age,gender,contact):
        self.__patient_id=patient_id
        self.__name=name
        self.__age=age
        self.__gender=gender
        self.__contact=contact
    
    def get_patient(self):
        return {
            'patient_id':self.__patient_id,
            'name':self.__name,
            'age':self.__age,
            'gender':self.__gender,
            'contact':self.__contact
        }
    
class Doctor:
    def __init__(self,doctor_id,doctor_name,specialization):
        self.__doctor_id=doctor_id
        self.__doctor_name=doctor_name
        self.__specialization=specialization
    
    def get_doctor(self):
        return {
            'doctor_id':self.__doctor_id,
            'doctor_name':self.__doctor_name,
            'specialization':self.__specialization
        }
    
class Medical_Records():
    # recordnum=0

    def __init__(self):
        self.records={}
        
    
    # def add_records(self,patient,doctor,disease,medication):
    #     self.records.update({recordnum:
    #         {
    #         'patient_info':patient.get_patient(),
    #         'doctor_info':doctor.get_patient(),
    #         'disease':disease,
    #         'medication':medication
    #     }
    #     }
    #     recordnum+=1
    #     )

    def add_records(self,patient,doctor,disease,medication):
        self.records[patient.get_patient()['patient_id']]={
            'patient_info':patient.get_patient(),
            'doctor_info':doctor.get_doctor(),
            'disease':disease,
            'medication':medication
        }
    
patient1=Patient(1,'Rupam',17,'male','+919999999999')
patient2=Patient(2,'Soumik',27,'female','+918888888888')

# print(patient1.get_patient(),patient2.get_patient(),sep='\n\n')

# for patient in [patient1,patient2]:
#     for (detail,value) in list(patient.get_patient().items()):
#         print(f'{detail} : {value}')
#     print()

doctor1=Doctor(1,'Megha','BDS')
doctor2=Doctor(2,'Sona','MBBS')

# for doctor in [doctor1,doctor2]:
#     for (detail,value) in list(doctor.get_doctor().items()):
#         print(f'{detail} : {value}')
#     print()

rec=Medical_Records()
rec.add_records(patient1,doctor1,'Covid','Amoxycilin')
rec.add_records(patient2,doctor2,'Cancer','Chemotherapy')

# for (id,details) in list(rec.records.items()):
#     print(f'Patient Number {id} Details:')
#     print('\n')
#     for (detail,value) in list(details.items()):
#         print(f'{detail} : {value}')
#         print()
#     print('\n\n')

enter=input('Enter patient name')
print()

for (id,details) in list(rec.records.items()):
    if details['patient_info']['name']==enter:
        print(f'Patient [id: {id}] Details:')
        print('\n')
        for (detail,value) in list(details.items()):
            print(f'{detail} : {value}')
            print()
        print('\n\n')
        

