function changeTitleColor() {
    document.querySelector('div1').style.color = 'green';
    document.querySelector('div2').style.color = 'yellow';
    document.querySelector('div3').style.color = 'red';
}
function changeBgColor(color){
    document.body.style.backgroundColor = color;
}
function copyContent(paragraph1, paragraph2){
    document.getElementById(paragraph1).innerHTML= document.getElementById(paragraph2).innerHTML
}
function changeFontSize(x){
    document.getElementById('dv3').style.fontSize = x;
}
function increaseFontSize(paragraph){
    document.getElementById(paragraph).style.fontSize = "larger";
}
function decreaseFontSize(paragraph){
    document.getElementById(paragraph).style.fontSize = "smaller";
}