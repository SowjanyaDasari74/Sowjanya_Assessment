# class name department id,name,location,hod throught the constructor initialize the department 
# create a method to display the department information
# display total department in your organization

# take the input form the user like how many department does he enter that many times the details of needs to enter and we have to store it and we have to print
# search department by dept by dept ID if not found it should gives like the given dept is not avaliable 
# search dept by dept_name it should give  output for any number character in a dept_name


class Department:
    dept_count = 0
    def __init__(self,id,name,location,dept_head):
        self.id = id
        self.name = name
        self.location = location
        self.dept_head = dept_head
        Department.dept_count += 1
    def display_Department_info(self):
        print("Department Information:")
        print("---------------------")
        print(f"ID: {self.id}")
        print(f"name: {self.name}")
        print(f"location: {self.location}")
        print(f"Dept_head: {self.dept_head}")
        print(f"Total Department: {Department.dept_count}")
    @classmethod
    def get_total_department(cls):
        return cls.department_count

departments = []
num_departments = int(input("How many departments do you want to enter? "))
for i in range(num_departments):
    print(f"\nEnter details for Department {i+1}:")
    
    dept_id = input("Enter Department ID: ")
    name = input("Enter Department Name: ")
    location = input("Enter Department Location: ")
    dept_head = input("Enter Department Head: ")
    department = {
        "id": dept_id,
        "name": name,
        "location": location,
        "dept_head": dept_head
    }
    departments.append(department)

# Display the collected department data
print("\nCollected Department Details:")
for dept in departments:
    print(dept)
