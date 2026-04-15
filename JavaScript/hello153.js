function unique(arr) {
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    let isRepeat = false;
    for (let j = 0; j < result.length; j++) {
      if (arr[i] === result[j]) isRepeat = true;
    }
    if (!isRepeat) result.push(arr[i]);
  }
  return result;
}
let data = [1, 2, 2, 3];
console.log(unique(data));
