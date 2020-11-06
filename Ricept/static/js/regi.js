var pswd = document.getElementById("password");
var pswd_conf = document.getElementById("password_confirmation");
var number = document.getElementById("number");
var length = document.getElementById("length");
var equal = document.getElementById("equal");
var sub_btn = document.getElementById("sub_btn");
var capital = document.getElementById("capital");


var b_number = false;
var b_length = false;
var b_equal = false;
var b_capital = false;


// When the user starts to type something inside the password field
pswd.onkeyup = function() {

  // Validate numbers
  var numbers = /[0-9]/g;
  if(pswd.value.match(numbers)) {  
    number.setAttribute("style","color: green;")
    b_number = true;
    number.innerText = "✔Як мінімум 1 цифра";
  } else {
    number.setAttribute("style","color: red;")
    b_number = false;
    number.innerText = "✖Як мінімум 1 цифра";
  }

  var upperCaseLetters = /[A-Z]/g;
  if(pswd.value.match(upperCaseLetters)) {  
    capital.setAttribute("style","color: green;")
    b_capital = true;
    capital.innerText = "✔Як мінімум 1 буква у верхньому регістрі";
  } else {
    capital.setAttribute("style","color: red;")
    b_capital = false;
    capital.innerText = "✖Як мінімум 1 буква у верхньому регістрі";
  }
  
  // Validate length
  if(pswd.value.length >= 8) {
    length.setAttribute("style","color: green;")
    b_length = true;
    length.innerText = "✔Мінімальна довжина пароля 8 символів";
  } else {
    length.setAttribute("style","color: red;")
    b_length = false;
    length.innerText = "✖Мінімальна довжина пароля 8 символів";
  }

  if(pswd.value === pswd_conf.value){
  	equal.setAttribute("style","color: green;")
  	b_equal = true;
  	equal.innerText = "✔Паролі збігаються";
  }else{
  	equal.setAttribute("style","color: red;")
  	b_equal = false;
  	equal.innerText = "✖Паролі збігаються";
  }

  if(b_number == true &&  b_length == true && b_equal == true && b_capital == true){
  	sub_btn.removeAttribute("disabled", "disabled");
  }
  else{
  	sub_btn.setAttribute("disabled", "disabled");
  }
}
pswd_conf.onkeyup = function() {
  if(pswd.value === pswd_conf.value){
  	equal.setAttribute("style","color: green;")
  	b_equal = true;
  	equal.innerText = "✔Паролі збігаються";
  }else{
  	equal.setAttribute("style","color: red;")
  	b_equal = false;
  	equal.innerText = "✖Паролі збігаються";
  }

  if(b_number == true &&  b_length == true && b_equal == true && b_capital == true){
  	sub_btn.removeAttribute("disabled", "disabled");
  }
  else{
  	sub_btn.setAttribute("disabled", "disabled");
  }
}