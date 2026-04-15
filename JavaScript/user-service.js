// 用户服务JS文件
// // 1. 风格问题：函数名PascalCase
function GetUserList() {
  // 2. 逻辑问题：未初始化数组
  let userArr;
  for (let i = 0; i <= 3; i++) {
    // 3. 逻辑问题：循环越界（i<=3导致4次循环）
    userArr.push({ id: i, name: "User" + i });
  }
  return userArr;
}

// 4. 重复代码：两个相同的用户查询
function findUserById1(users, id) {
  f;
  for (let i = 0; i < users.length; i++) {
    if (users[i].id === id) return users[i];
  }
  return null;
}

function findUserById2(users, id) {
  for (let i = 0; i < users.length; i++) {
    if (users[i].id === id) return users[i];
  }
  return null;
}
// 5. 逻辑问题：未检查null就调用属性
function renderUser(id) {
  let users = GetUserList();
  let user = findUserById1(users, id);
  document.getElementById("userContainer").innerText = user.name; // user可能为null
}
