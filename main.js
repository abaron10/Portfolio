function articles(){
    window.location.href="https://af-baron10.medium.com/";
}
function linkedin(){
    window.location.href="https://www.linkedin.com/in/andres-baron-sandoval-76ab96186/";
}
function git(){
    window.location.href="https://github.com/abaron10";
}

function download(){
    window.open("./cves.pdf", '_self');
}


function contact(){
    document.getElementById("subtitle-contact").scrollIntoView({behavior: 'smooth'});

}

let textLength = 0;
let text = "Full Stack developer & Master in Software Engineering Student";

function type() {
    let textChar = text.charAt(textLength++);
    let paragraph = document.getElementById("typed");
    let charElement = document.createTextNode(textChar);
    paragraph.appendChild(charElement);
    if(textLength < text.length+1) {
        setTimeout('type()', 50);
    } else {
        text = 'Full Stack developer & Master in Software Engineering Student';
    }
}

document.addEventListener("DOMContentLoaded", function() {
    type();
});
