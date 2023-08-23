function articles(){
    window.location.href="./articles.html";
}
function hobbies(){
    window.location.href="./hobbies.html";
}
function linkedin(){
    window.location.href="https://www.linkedin.com/in/andres-baron-sandoval-76ab96186/";
}
function git(){
    window.location.href="https://github.com/abaron10";
}

function main(){
    window.location.href="./index.html";
}

function download(){
    window.open("./cves.pdf", '_self');
}


function contact(){
    document.getElementById("subtitle-contact").scrollIntoView({behavior: 'smooth'});

}

let textLength = 0;
let text = "Architecting Dreams: A Journey Through the Code Realm with Andrés";

function type() {
    let textChar = text.charAt(textLength++);
    let paragraph = document.getElementById("typed");
    let charElement = document.createTextNode(textChar);
    paragraph.appendChild(charElement);
    if(textLength < text.length+1) {
        setTimeout('type()', 50);
    } else {
        text = 'Coding Journeyman: Navigating the Software World as an Engineer';
    }
}

document.addEventListener("DOMContentLoaded", function() {
    type();
});
