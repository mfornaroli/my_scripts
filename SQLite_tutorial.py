import sqlite3

# first we define a class we are going to use as example
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@micron.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}, '{}', '{}')".format(self.first, self.last, self.pay)

# now lets add some functions will turn out to be useful
def insert_emp(emp):
    with conn:  # contex manager
        c.execute(""" INSERT INTO employees VALUES (?, ?, ?)""", (emp.first, emp.last, emp.pay))


def get_emp_by_name(lastname):
    '''
    this doesnt need to be committed, no with statement needed!
    :param lastname:
    :return:
    '''
    c.execute(""" SELECT * FROM employees WHERE last=:last""", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay WHERE first = :first AND last = :last""",
                  {'pay': pay, 'first': emp.first, 'last': emp.last})


def remove_emp(emp):
    with conn:
        c.execute(""" DELETE FROM employees WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last})


# initialize two variables
emp1 = Employee('John', 'Doe', 45000)
emp2 = Employee('Eric', 'Doe', 100000)
print(emp1.first)
print(emp2.first)

# initialize connection (must have __enter__ and __exit__ methods..)
conn = sqlite3.connect('employee.db')  # creates employee.db file in the directory! connection manager!
c = conn.cursor()

# execute only the first time...

# c.execute(""" CREATE TABLE employees (
#                 first text,
#                 last text,
#                 pay int
#                 ) """)

# c.execute(""" INSERT INTO employees VALUES ('enzo', 'maestri', '70000')""")
# c.execute(""" INSERT INTO employees VALUES ('enzo', 'forlami', '30000')""")
# c.execute(""" INSERT INTO employees VALUES (?, ?, ?)""", (emp1.first, emp1.last, emp1.pay))
# c.execute(""" INSERT INTO employees VALUES (:first, :last, :pay)""", {'first': emp2.first, 'last': emp2.last, 'pay': emp2.pay})

insert_emp(Employee('mauro', 'ragazzetti', 27.500))   # we can use the function instead! amaing!
insert_emp(Employee('mauro', 'bello figo', 97.500))


# c.execute(""" SELECT * FROM employees WHERE first = 'enzo' """)
c.execute(""" SELECT * FROM employees""")
# c.execute(""" SELECT * FROM employees WHERE last=?""", ('forlami',))  # strange syntax
# c.execute(""" SELECT * FROM employees WHERE last=:last""", {'last': 'forlami'})  # this is the other possibility
for elem in c.fetchall():
    print(elem)

update_pay(emp1, 200000)

print('\n')
c.execute(""" SELECT * FROM employees""")
for elem in c.fetchall():
    print(elem)


# committing current transaction. make sure to commit changes!
conn.commit()
conn.close()



