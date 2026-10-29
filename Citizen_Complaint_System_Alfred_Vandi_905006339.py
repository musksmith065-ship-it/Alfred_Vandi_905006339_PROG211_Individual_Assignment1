class Citizen:
    complaint_registry=[]
    def __init__(self, name, National_id, Age):
        self.name=name
        self.National_id=National_id
        self.Age=Age

    def update_info(self, name, Id, Age):
        for name in self.complaint_registry:
            if name in self.complaint_registry:
                return f"{name}, found"

            else:
               self.complaint_registry={
                   "Name":name,
                   "ID":Id,
                   "Age":Age
               }
               return f"{name}, {Id}, {Age} has been successfully added to the system "


    @staticmethod
    def register(name, id, Age):
       print(f"User name: {name}\nId: {id}\nAge:{Age}")
   

class Complaint(Citizen):
    
    def __init__(self, name, National_id, Age, Description, Location):
        super().__init__(name, National_id, Age)
        self.description=Description
        complaint_registry={
            "Name":name,
            "National_id": National_id,
            "Age":Age,
            "Description": Description,
            "Location":Location
        }
        self.complaint_registry.append(complaint_registry)

    @classmethod
    def display_info(cls):
        return cls.complaint_registry
               

    def see_complaint_info(self):
        for complaint in self.complaint_registry:
            problem=complaint["Description"]
            user=complaint["Name"]
            location=complaint["Location"]
            print("*"*50)
            print("Problem Affecting people")
            print(f"User: {user}\nProblem: {problem}\nLocation: {location}")
            print("*"*50)


citizen=Citizen("alfred", "we123", 786)
complaint=Complaint("angella", "N3425", 14, "I am Having water issues", "new England ville")
complaint2=Complaint("kabia", "fg45", 12, "Bad Road", "sierra leone")
citizen.register("vandi", "wer34", 12)


print(complaint.display_info())
complaint.see_complaint_info()
