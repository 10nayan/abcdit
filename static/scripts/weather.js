window.addEventListener('load', ()=>{
  let long;
  let lat;
  let temp=document.querySelector("#temp")
  let tempf=document.querySelector("#tempf")
  let feels=document.querySelector("#feels")
  let location=document.querySelector("h1")
  let timezone=document.querySelector("#timezone")
  let image=document.getElementById("image")
  if (navigator.geolocation){
    navigator.geolocation.getCurrentPosition(position=>{
      long=position.coords.longitude;
      lat=position.coords.latitude;
      const api=`http://api.weatherapi.com/v1/forecast.json?key=df0058859b884b02af754250201105&q=${lat},${long}`
      fetch(api)
      .then(response=>{
        return response.json();

      })
      .then(data=>{
        const {temp_c,feelslike_c,is_day}=data.current;
        const{text,code}=data.current.condition;
        const{name,region,country,tz_id}=data.location;
        temp.textContent=`Tempereture: ${temp_c}°C`;
        tempf.textContent=`Feels like: ${feelslike_c}°C`;
        timezone.innerHTML=tz_id;
        feels.textContent=text;
        location.innerHTML=`${name},${region}`;
        if (is_day){
          image.innerHTML=`<img src="static/images/icon/day/${code}.png"/>`;
        }
        else{
          image.innerHTML=`<img src="icon/night/${code}.png"/>`;
        }
      });
    });
  }
});
