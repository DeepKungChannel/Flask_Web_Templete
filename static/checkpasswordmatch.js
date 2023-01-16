var pwd1 = document.getElementById("password")
var pwd2 = document.getElementById("confirm_password")
var form = document.getElementById("form")

form.addEventListener("submit", (event) => {
    if (pwd1.value !== pwd2.value || pwd1.value.length === 0 || pwd2.value.length === 0){
        event.preventDefault();
        var error_text = document.getElementById("error_text")
        error_text.innerHTML = "Password is not match."
    }
    
}, false);


