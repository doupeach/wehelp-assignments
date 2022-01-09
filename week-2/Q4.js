// 要求四 ( 請閱讀英文 ):演算法
// WeHelp Bootcamp Assignment - Week 2
// Given an array of integers,
// show indices of the two numbers such that they add up to a specific target.
// You can assume that each input would have exactly one solution,
// and you can not use the same element twice.

function twoSum(nums, target) {
  // your code here
  for (let x = 0; x < nums.length; x++) {
    let goal = target - nums[x];
    for (let y = x + 1; y <= nums.length; y++) {
      if (nums[y] === goal) return [x, y];
    }
  }
}
let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9
