let close = document.getElementsByClassName("close");
for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
        let div = this.parentElement;
        div.style.display = "none";
    }
}

let list = document.querySelector('ul');
list.addEventListener("click", function(ev) {
    let target = ev.target;
    if(target.type === "checkbox"){
        let li = target.closest('li');
        if(li){
            li.classList.toggle('checked', target.checked);
        }
    }
});

function newElement() {
    let li = document.createElement("li");
    let inputValue = document.getElementById("inputScript").value;
    let t = document.createTextNode(inputValue);

    li.appendChild(t);
    if (inputValue === '') {
        alert("You must write something!");
    } else {
        document.getElementById("listScript").appendChild(li);
    }
    document.getElementById("inputScript").value = "";

    let span = document.createElement("SPAN");
    let checkbox = document.createElement("INPUT")
    checkbox.type = "checkbox";
    checkbox.className = "checkbox";

    span.className = "close";
    li.appendChild(span);
    li.appendChild(checkbox);

    for (i = 0; i < close.length; i++) {
        close[i].onclick = function() {
        let div = this.parentElement;
        div.style.display = "none";
        }
    }
}