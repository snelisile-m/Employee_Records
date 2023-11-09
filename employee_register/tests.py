from django.test import TestCase
from .models import Employee

class EmployeeModelTest(TestCase):
    def setUp(self):
        """Creating a sample employee for testing"""
        self.employee = Employee.objects.create(
            eid="1",
            ename="sne",
            eemail="sne@hotmail.com",
            econtact="0712833983"
        )

    def test_employee_creation(self):
        """To test if the employee is created successfully"""
        self.assertEqual(self.employee.eid, "1")
        self.assertEqual(self.employee.ename, "sne")
        self.assertEqual(self.employee.eemail, "sne@hotmail.com")
        self.assertEqual(self.employee.econtact, "0712833983")


