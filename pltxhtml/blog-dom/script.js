function binhPhuong(number) {
  return number * number;
}

function tinhDienTichHinhTron(banKinh) {
  if (banKinh <= 0) {
    return "Khong tinh duoc";
  } else {
    return Math.PI * banKinh * banKinh;
  }
}

// Thay đổi màu sắc tiêu đề h1
function changeTitleColor() {
    document.querySelector('h1').style.color = 'red';
}
