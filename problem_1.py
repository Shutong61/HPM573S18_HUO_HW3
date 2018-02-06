
class Patient:
    """ base class """
    def __init__(self, name):
        """
        :param name: name of the patient

        """
        self.name = name

    def discharge(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")



class Emergency(Patient):
    def __init__(self, name):

        Patient.__init__(self, name)
        self.expected_cost = 1000

    def discharge(self):
        print(self.name + " Emergency")

class Hospitalized(Patient):
    def __init__(self, name):

        Patient.__init__(self, name)
        self.expected_cost = 2000

    def discharge(self):
        print(self.name + " Hospitalized")




class Hospital():
    def __init__(self):

        self.cost = 0
        self.patient = []

    def admit(self, patient):
        self.patient.append(patient) # object last.add the patient one by one

    def discharge_all(self):
        for patient in self.patient:
            patient.discharge()
            self.cost += patient.expected_cost

    def get_total_cost(self):
        return self.cost



p1 = Hospitalized("p1")
p2 = Hospitalized("p2")
p3 = Emergency("p3")
p4 = Emergency("p4")
p5 = Emergency("p5")

YaleHealth = Hospital()

YaleHealth.admit(p1)
YaleHealth.admit(p2)
YaleHealth.admit(p3)
YaleHealth.admit(p4)
YaleHealth.admit(p5)


YaleHealth.discharge_all()

print(YaleHealth.get_total_cost())





