# -*- coding: utf-8 -*-
import datetime

from django.utils import timezone
from django.test import TestCase

from kapra.models import Employee

# Create your tests here.

class EmployeeMethodTests(TestCase):

    def employee_duration_test(self):
        employee1 = Employee()
      	self.assertEqual(employee1.employee_duration(), True)
