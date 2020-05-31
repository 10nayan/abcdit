document.addEventListener('DOMContentLoaded',()=>{
var socket = io();
socket.on('connect',()=> {
socket.send(firstName)
});
socket.on('message',data=>{
  console.log(`${data} is connected`)
});
socket.on('my_event',data=>{
  console.log(data)
});
document.querySelector('#submit').onclick=()=>{
  var mesg=document.querySelector('#input').value;
  var rcpnt=document.querySelector('#receiver').value;
  console.log(rcpnt);
  socket.emit('new_event',{'msg':mesg,'name':firstName,'receiver':rcpnt});
  const q=document.createElement('p');
  const dr=document.createElement('br');
  q.innerHTML=firstName+' '+mesg;
  document.querySelector('#messages').append(q);
};
socket.on('new_response',data=>{
  const p=document.createElement('p');
  const br=document.createElement('br');
  p.innerHTML=data.time+' '+data.name+' '+data.msg;
  document.querySelector('#messages').append(p);

});
});
