const Solution = require('./Sum_of_Two_Integers');

const testcases =  [
  [2, 3, 5],
  [1, 2, 3],
  [-10, 9, -1],
  [-1, -1, -2],
  [-1, 1, 0]
]

testcases.forEach(testcase => {
  console.assert(Solution.getSum(testcase[0], testcase[1]) === testcase[2]);
})

console.log("OK")