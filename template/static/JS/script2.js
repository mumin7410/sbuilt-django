console.log('muminkd');
// scroll navbar 
window.addEventListener("scroll",function(){
    let header = document.getElementById("navbar");
    if(window.scrollY > 40){
        header.classList.add("cus-nav");

    }else{
        header.classList.remove("cus-nav");
    }
});


const tog_gle = document.getElementById('toggle');
const navbar = document.getElementById('dropdown');

tog_gle.addEventListener('click',()=>{
    navbar.classList.toggle('show');
});




