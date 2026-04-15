// function formatDate1(date) {
//   return date.toLocaleDateString();
// }
// function formatDate2(time) {
//   return time.toLocaleDateString();
// }
// let now = new Date();
// console.log(formatDate1(now));
// console.log(formatDate2(now));

// 仅保留一个函数，消除冗余
function formatDate(date) {
  // 入参校验：先判断是否为有效Date对象
  if (!(date instanceof Date) || isNaN(date.getTime())) {
    throw new TypeError("参数必须为有效的Date类型");
  }
  return date.toLocaleDateString();
}

let now = new Date();
console.log(formatDate(now));
