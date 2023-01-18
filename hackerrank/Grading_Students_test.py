import unittest
from Grading_Students import gradingStudents

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      [[73, 67, 38, 33], [75, 67, 40, 33]]
    ]

  def test_grading_students(self):
    for tc in self.testcases:
      self.assertEqual(gradingStudents(tc[0]), tc[1])

if __name__ == '__main__':
    unittest.main()