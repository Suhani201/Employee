# test_employee.py
import pytest
from employee import get_employee_info

def test_get_employee_info():
    # Sample data
    name = "Jhon Doe"
    emp_id = "E101"
    department = "IT"
    salary = 55000
    # Expected result
    expected_output = (
        " Employee Name : Jhon Doe\n"
        " Employee ID : E101\n"
        " Department : IT\n"
        " Salary : 55000"
    )
    # Assertion
    assert get_employee_info(name, emp_id, department, salary) == expected_output