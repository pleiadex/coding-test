import unittest
from io import StringIO
from unittest.mock import patch
from The_Full_Counting_Sort import countSort

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
        [
            [
              ['0', 'ab'      ],
              ['6', 'cd'      ],
              ['0', 'ef'      ],
              ['6', 'gh'      ],
              ['4', 'ij'      ],
              ['0', 'ab'      ],
              ['6', 'cd'      ],
              ['0', 'ef'      ],
              ['6', 'gh'      ],
              ['0', 'ij'      ],
              ['4', 'that'    ],
              ['3', 'be'      ],
              ['0', 'to'      ],
              ['1', 'be'      ],
              ['5', 'question'],
              ['1', 'or'      ],
              ['2', 'not'     ],
              ['4', 'is'      ],
              ['2', 'to'      ], 
              ['4', 'the'     ], 
            ],
            "- - - - - to be or not to be - that is the question - - - - "
        ]
    ]
  @patch('sys.stdout', new_callable = StringIO)
  def test_counting_sort(self, stdout):
    for tc in self.testcases:
        countSort(tc[0])
        self.assertEqual(stdout.getvalue(), tc[1])

if __name__ == '__main__':
    unittest.main()