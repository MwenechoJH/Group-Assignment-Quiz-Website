const input_field = document.getElementById("user-input");
const chat_output = document.getElementById("response");
const send_button = document.getElementById("send");


function construct_body(value){
    const body = {
        name: "mwenecho",
        question: value
    }
    return body
}

function ask_question(){
    const body = construct_body(input_field.value);

    fetch("http://127.0.0.1:8000/ask",{
        method:"POST",
        headers:{
            'Content-Type':'application/json'
        },
        body: JSON.stringify(body)
    })
    .then(response=>response.json())
    .then(data=>{
        chat_output.innerHTML=`${data["Chat_Response"]}`
    })
}
send_button.addEventListener('click', ask_question)