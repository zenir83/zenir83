class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def getName(self):
    return self.name
  
  def getLevel(self):
    return self.level

  def getNrOfStudents(self):
    return self.numberOfStudents
  
  def SetNumberOfStudents(self, newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents
  
  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students. "

Libanon = School("Libanon", "primary", 200)
Libanon.SetNumberOfStudents(250)
# print(Libanon.numberOfStudents)
# print(repr(Libanon))

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickuppolicy):
    super().__init__(name, 'primary', numberOfStudents)
    self.pickuppolicy = pickuppolicy

  def get_policy(self):
    return self.pickuppolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "The pickup policy is {pickupPolicy}".format(pickupPolicy = self.pickuppolicy)
  
Reigerbos = PrimarySchool("Reigerbos", 150, pickuppolicy ="\n Op maandag, dinsdag, donderdag en vrijdag om 14:30. Op woensdag 12:15" )
# print(repr(Reigerbos))

class HighSchool(School):
  def __init__(self, name, numberOfStudents, *sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams

  def get_sportsTeams(self):
    return self.sportsTeams
  
  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + f" information of our sport Team {', '.join(self.sportsTeams)}"

Erasmiaans = HighSchool("Erasmiaans", 300, "Tennis", "Voetbal", "Kickboxen")

print(repr(Erasmiaans))
