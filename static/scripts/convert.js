document.addEventListener('DOMContentLoaded',()=>{
  document.getElementById('button1').onclick = () => {
    let a=document.getElementById("area").value;
    let b=document.getElementById("area-change").value;
    if (b==10.7639){
    document.getElementById("convert1").innerHTML=a+" square meter = "+a*b+" square feet";
  }
  else{
    document.getElementById("convert1").innerHTML=a+" square feet = "+a*b+" square meter";
  }
}
document.getElementById('button21').onclick = () => {
  let a=document.getElementById("length1").value;
  let b=document.getElementById("length1-change").value;
  if (b==3.28084){
  document.getElementById("convert21").innerHTML=a+" meter = "+a*b+" feet";
}
else{
  document.getElementById("convert21").innerHTML=a+" meter = "+a*b+" yard";
}
}
document.getElementById('button22').onclick = () => {
  let a=document.getElementById("length2").value;
  let b=document.getElementById("length2-change").value;
  if (b==0.621371){
  document.getElementById("convert22").innerHTML=a+" kilometer = "+a*b+" mile";
}
else{
  document.getElementById("convert22").innerHTML=a+" mile = "+a*b+" kilometer";
}
}
document.getElementById('button3').onclick = () => {
  let a=document.getElementById("speed").value;
  let b=document.getElementById("speed-change").value;
  if (b==0.277778){
  document.getElementById("convert3").innerHTML=a+" kilometer per hour = "+a*b+" meter per second";
}
else{
  document.getElementById("convert3").innerHTML=a+" meter per second = "+a*b+" kilometer per hour";
}
}
document.getElementById('button4').onclick = () => {
  let a=document.getElementById("temp").value;
  let b=document.getElementById("temp-change").value;
  if (b=='temp1'){
    let c=toCelsius(a);
  document.getElementById("convert4").innerHTML=a+" fahrenheit = "+c+" celcius";
}
else{
  let c=toFahrenheit(a);
  document.getElementById("convert4").innerHTML=a+" celcius = "+c+" fahrenheit";
}
}
document.getElementById('button5').onclick = () => {
  let a=document.getElementById("volume").value;
  let b=document.getElementById("volume-change").value;
  if (b==0.219969){
  document.getElementById("convert5").innerHTML=a+" litre = "+a*b+" gallon";
}
else{
  document.getElementById("convert5").innerHTML=a+" gallon = "+a*b+" litre";
}
}
document.getElementById('button6').onclick = () => {
  let a=document.getElementById("weight").value;
  let b=document.getElementById("weight-change").value;
  if (b==2.20462){
  document.getElementById("convert6").innerHTML=a+" kilogram = "+a*b+" pound";
}
else{
  document.getElementById("convert6").innerHTML=a+" pound = "+a*b+" kilogram";
}
}
document.getElementById('button7').onclick = () => {
  let a=document.getElementById("land").value;
  let b=document.getElementById("land-change").value;
  if (b==0.1606){
  document.getElementById("convert7").innerHTML=a+" bigha = "+a*b+" hectare";
}
else{
  document.getElementById("convert7").innerHTML=a+" bigha = "+a*b+" acre";
}
}

});
function toCelsius(f) {
  return (5/9)*(f-32);
}
function toFahrenheit(t){
  return (t*9/5)+32
}
