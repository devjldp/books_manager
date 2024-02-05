let password = document.getElementById('password');
let form = document.getElementById('register-form')
let message = document.getElementById('message-validation')

form.addEventListener('submit', (e) =>{
  let passw=  /^[a-zA-Z0-9]{5,15}$/;
  if(!password.value.match(passw)){ 
    message.innerText = "Invalid password. Please Introduce a valid password letters a numbers with a length between 5 and 15 characters"
    e.preventDefault()
  }
})


