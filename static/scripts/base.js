var is_login=`{{current_user.is_authenticated}}`;
function disable_link(){
  document.querySelector('#disable').disabled=true;
  document.querySelector('#disable').removeAttribute('href');
  document.querySelector('#disable').style.textDecoration='None';
  document.querySelector('#disable').style.cursor='default';
}
function show_link(){
  document.querySelector('#disable').disabled=false;
  document.querySelector('#disable').href='signout';
  document.querySelector('#disable').style.textDecoration='default';
  document.querySelector('#disable').style.cursor='hand';
}
if (is_login=='True'){
  show_link()
}
