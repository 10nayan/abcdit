document.addEventListener('DOMContentLoaded',()=>{
var socket = io();
socket.on('connect',()=> {
socket.send("I am connected")
});
socket.on('message',data=>{
  console.log(`Message received :${data}`)
});
socket.on('my_event',data=>{
  console.log(data)
});
document.querySelector('#submit').onclick=()=>{
  socket.emit('new_event',{'msg':document.querySelector('#input').value,'name':firstName});
};
socket.on('new_response',data=>{
  const p=document.createElement('p');
  const br=document.createElement('br');
  p.innerHTML=data.time+data.name+data.msg;
  document.querySelector('#messages').append(p);

});
});
