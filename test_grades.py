import unittest
from grades import calculate_grade, NegativeValue,OutOfRange

class Test_Grades(unittest.TestCase):
  def test_A_grade(self):
    self.assertEqual(calculate_grade(100),"A grade")
  def test_B_grade(self):
    self.assertEqual(calculate_grade(80),"B grade")
  def test_C_grade(self):
    self.assertEqual(calculate_grade(79),"C grade")
  def test_D_grade(self):
    self.assertEqual(calculate_grade(67),"D grade")
  def test_F_grade(self):
    self.assertEqual(calculate_grade(44),"F grade")
  #edge cases
  def test_edgeCases(self):
    self.assertEqual(calculate_grade(0),'F grade')
    self.assertEqual(calculate_grade(59),'F grade')
    self.assertEqual(calculate_grade(60),'D grade')
    self.assertEqual(calculate_grade(100),'A grade')
  #invalid input
  def test_negativeValue(self):
    with self.assertRaises(NegativeValue):
      calculate_grade(-100)
  def test_outOfRange(self):
    with self.assertRaises(OutOfRange):
      calculate_grade(500)
  def test_valueError(self):
    with self.assertRaises(ValueError):
      calculate_grade("eighty")

if __name__ == "__main__":
  unittest.main()