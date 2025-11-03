
fetch("/loginsubmit", {
    method: 'POST',
    headers:{
        'Content-Type': 'application/json'
    }
})
    .then(response => response.json())
    .then(loginsubmit => {
        let user_error = document.getElementById('user_error')
        let pass_error = document.getElementById('pass_error')
        if (loginsubmit.pass_valid === true){
            console.log("pass valid")
            pass_error.style.display = "hidden";
        }
        else{
            console.log("pass invalid")
            pass_error.style.display = "visible";
        }
        if(loginsubmit.user_valid === true){
            user_error.style.display = "hidden";
            console.log("username is valid")
        }
        else{
            user_error.style.display = "visible";
        }
    })
    .catch()