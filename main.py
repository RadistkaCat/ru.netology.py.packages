from application import salary
from application.db import people

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()