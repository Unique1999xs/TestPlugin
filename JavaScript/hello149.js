// let arr = [1, 2, 3];
// console.log(arr[3]);

let arr = [1, 2, 3];
// 访问最后一个元素的正确方式
console.log(arr.at(-1));
// 或动态索引的通用检查方式
const targetIndex = 3;
if (targetIndex >= 0 && targetIndex < arr.length) {
  console.log(arr[targetIndex]);
} else {
  console.error(`索引 ${targetIndex} 超出数组有效范围`);
}
