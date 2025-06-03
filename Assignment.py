'''>class name department id,name,location,hod throught the constructor initialize the department 
   >create a method to display the department information
   >display total department in your organization
   >take the input form the user like how many department does he enter that many times the details of needs to enter and
    we have to store it and we have to print
   >search department by dept by dept ID if not found it should gives like the given dept is not avaliable 
   >search dept by dept_name it should give  output for any number character in a dept_name
'''
class Department:
  no_of_dept = 0
  details = []
  def __init__(self,name,id,location,head):
    self.name = name
    self.id = id
    self.location = location
    self.head = head
    
  def display_details(self):
    print(f"id : {self.id}")
    print(f"name: {self.name}")
    print(f"location : {self.location}")
    print(f"head :{self.head}")

  @classmethod  
  def get_details(cls):
    cls.no_of_dept = int(input("Enter number of departments: "))
    for i in range(cls.no_of_dept):
      temp_list = []
      name = input("Enter the dept name: ")
      temp_list.append(name)
      dept_id = input("Enter the dept id: ")
      temp_list.append(dept_id)
      location = input("Enter the dept location: ")
      temp_list.append(location)
      head = input("Enter the dept head: ")
      temp_list.append(head)
      cls.details.append(temp_list)
    return cls.details

  @classmethod
  def search(cls):
    id = input("Enter the id to get details: ")
    for i in range(cls.no_of_dept):
      if cls.details[i][1] == id:
        print(f"id : {cls.details[i][0]}\nname : {cls.details[i][1]}\nlocation : {cls.details[i][2]}\nhead : {cls.details[i][3]} ")
      else:
        print("Given dept id is not available: ")

  @classmethod
  def start(cls):
    cls.get_details()
    print("\n")
    print("Select any option from\n1.Get details of all departments\n2.Get details by department id\n3.Get the details by department name\n")
    option = int(input())
    if option == 2:
      Department.search()
    elif option == 3:
      name = input("Enter the department name to get details: ")
      found = False
      for i in range(cls.no_of_dept):
        if cls.details[i][0].lower() == name.lower():
          print(f"id : {cls.details[i][1]}\nname : {cls.details[i][0]}\nlocation : {cls.details[i][2]}\nhead : {cls.details[i][3]}")
          found = True
          break
        if not found:
          print("Given department name is not available.")
    else:
      print("Details of all departments")
      print("---------------------------")
      for i in range(cls.no_of_dept):
        department = Department(cls.details[i][0],cls.details[i][1],cls.details[i][2],cls.details[i][3])
        print(f"\nDetails of department{i+1}")
        department.display_details()

Department.start()

