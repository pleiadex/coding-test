/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function(a, b) {
  while (b != 0) {
    const temp = (a & b) << 1;
    a = a ^ b;
    b = temp;
  }
  return a;
};

// I used JS since Python uses a variable number of bits to store integers
exports.getSum = getSum;