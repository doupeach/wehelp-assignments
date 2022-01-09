// 要求三:演算法
// 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
// 提醒:請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。

function maxProduct(nums) {
  // 請用你的程式補完這個函式的區塊

  // 若只有兩個數字，直接印出相乘結果
  if (nums.length === 2) {
    return console.log(nums[0] * nums[1]);
  } else {

    // 求最大值
    let max1 = nums[0];
    nums.forEach(function (value) {
      if (max1 < value) {
        max1 = value;
      }
    });
    // 再求次大值
    newNums = nums.filter((item) => item !== max1);
    let max2 = newNums[0];
    newNums.forEach(function (value) {
      if (max2 < value) {
        max2 = value;
      }
    });

    // 求最小值
    let min1 = nums[0];
    nums.forEach(function (value) {
      if (min1 > value) {
        min1 = value;
      }
    });
    // 再求次小值
    newNums = nums.filter((item) => item !== min1);
    let min2 = newNums[0];
    newNums.forEach(function (value) {
      if (min2 > value) {
        min2 = value;
      }
    });

    // 判斷最小及次小值相乘結果，是否大於最大值乘以次大值
    if (min1 * min2 > max1 * max2) {
      console.log(min1 * min2);
    } else {
      console.log(max1 * max2);
    }
  }
}

maxProduct([5, 20, 2, 6]); // 得到 120
maxProduct([10, -20, 0, 3]); // 得到 30
maxProduct([-1, 2]); // 得到 -2
maxProduct([-1, 0, 2]); // 得到 0
maxProduct([-1, -2, 0]); // 得到 2
