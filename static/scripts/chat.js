document.addEventListener('DOMContentLoaded',()=>{
var socket = io();
socket.on('connect',()=> {
socket.send(email)
});
socket.on('message',data=>{
  console.log(`${data} is connected`)
});
socket.on('my_event',data=>{
  console.log(data)
});
document.querySelector('#submit').onclick=()=>{
  var now=current_time();
  var mesg=document.querySelector('#input').value;
  var rcpnt=document.querySelector('#receiver').value;
  console.log(rcpnt);
  if (mesg.length>0){
  socket.emit('new_event',{'msg':mesg,'name':firstName,'receiver':rcpnt});
  const p=document.createElement('p');
  const br=document.createElement('br');
  const span_myname = document.createElement('span');
  const span_timestamp = document.createElement('span');
  p.setAttribute("class","my_msg");
  span_myname.setAttribute("class","my_username");
  span_myname.innerText=firstName;
  span_timestamp.setAttribute("class","timestamp")
  span_timestamp.innerText=now;
  p.innerHTML += span_myname.outerHTML + br.outerHTML + mesg + br.outerHTML + span_timestamp.outerHTML;
  document.querySelector('#messages').append(p);
}
document.querySelector('#input').value="";

};
socket.on('new_response',data=>{
  const q=document.createElement('p');
  const dr=document.createElement('br');
  const span_hername = document.createElement('span');
  const span_timestamp2 = document.createElement('span');
  q.setAttribute("class","her_msg");
  span_hername.setAttribute("class","her_username");
  span_hername.innerText=data.name;
  span_timestamp2.setAttribute("class","timestamp")
  span_timestamp2.innerText=data.time;
  q.innerHTML += span_hername.outerHTML + dr.outerHTML + data.msg + dr.outerHTML + span_timestamp2.outerHTML;
  document.querySelector('#messages').append(q);
});
});
function current_time(){
  var time = new Date();
  return time.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })
}
