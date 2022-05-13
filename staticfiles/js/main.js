// message section
const message = document.querySelector('.message');


if (message) {
   setTimeout(() => {
     message.classList.add("message-hide");
   }, 5000);
}


// nav section 

$(document).ready(function () {
    if ($(window).width() > 991){
    $('.navbar-light .d-menu').hover(function () {
            $(this).find('.sm-menu').first().stop(true, true).slideDown(150);
        }, function () {
            $(this).find('.sm-menu').first().stop(true, true).delay(120).slideUp(100);
        });
        }
    });


// card dection 
// $(document).ready(function() {
//    console.log("document is ready");
     
   
//      $( ".card" ).hover(
//      function() {
//        $(this).addClass('shadow-lg').css('cursor', 'pointer'); 
//      }, function() {
//        $(this).removeClass('shadow-lg');
//      }
//    );
     
//    // document ready  
//    });
   
   