var days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
var months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
now=new Date();
var day = days[ now.getDay() ];
var month = months[ now.getMonth() ];
var date= now.getDate();
var year= now.getFullYear();
var nextDay1=new Date();
var nextDay2=new Date();
var nextDay3=new Date();
var nextDay4=new Date();
var nextDay5=new Date();
var nextDay6=new Date();
nextDay1.setDate(now.getDate()+1);
nextDay2.setDate(now.getDate()+2);
nextDay3.setDate(now.getDate()+3);
nextDay4.setDate(now.getDate()+4);
nextDay5.setDate(now.getDate()+5);
nextDay6.setDate(now.getDate()+6);
var n=0;
var id_days=[{id:'first-day',val:days[nextDay1.getDay()]},{id:'second-day',val:days[nextDay2.getDay()]},{id:'third-day',val:days[nextDay3.getDay()]},{id:'forth-day',val:days[nextDay4.getDay()]},
{id:'fifth-day',val:days[nextDay5.getDay()]},{id:'sixth-day',val:days[nextDay6.getDay()]}];
var id_dates=[{id:'first-date',val:nextDay1.getDate()},{id:'second-date',val:nextDay2.getDate()},{id:'third-date',val:nextDay3.getDate()},{id:'forth-date',val:nextDay4.getDate()},
{id:'fifth-date',val:nextDay5.getDate()},{id:'sixth-date',val:nextDay6.getDate()}];
var id_months=[{id:'first-month',val:months[nextDay1.getMonth()]+' '+nextDay1.getFullYear()},{id:'second-month',val:months[nextDay2.getMonth()]+' '+nextDay2.getFullYear()},{id:'third-month',val:months[nextDay3.getMonth()]+' '+nextDay3.getFullYear()},{id:'forth-month',val:months[nextDay4.getMonth()]+' '+nextDay4.getFullYear()},
{id:'fifth-month',val:months[nextDay5.getMonth()]+' '+nextDay5.getFullYear()},{id:'sixth-month',val:months[nextDay6.getMonth()]+' '+nextDay6.getFullYear()}];
document.addEventListener('DOMContentLoaded',()=>{
	document.querySelector('h1').innerText=day;
	document.querySelector('h3').innerText=`${date} ${month} ${year}`;
	id_days.map(set_days);
	id_dates.map(set_dates);
	id_months.map(set_months);
	colours=['#03fc49','#03fc80','#03fcba','#03dbfc','#03a1fc','#036bfc','#033dfc','#0303fc','#4103fc','#7303fc','#4103fc','#0303fc','#033dfc','#036bfc','#03a1fc','#03dbfc','#03fcba','#03fc80','#03fc49']
	window.setInterval(changeColor,1000);
});
function changeColor(){
	document.querySelector('h1').style.color=colours[n];
	n++;
	if (n==20){
		n=1;
	}
}
function set_day(id,val){
	document.getElementById(id).innerText=val;
}
function set_date(id,val){
	document.getElementById(id).innerText=val;
}
function set_month(id,val){
	document.getElementById(id).innerText=val;
}
function set_days(item){
	set_day(item.id,item.val)
}
function set_dates(item){
	set_day(item.id,item.val)
}
function set_months(item){
	set_day(item.id,item.val)
}
