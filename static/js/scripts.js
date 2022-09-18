$(document).ready(function(){
    $(".phone").inputmask("(234) 999-9999", {"onincomplete": function(){
        $(".phone").val("");
        swal("Opss !", "Incomplete Phone Number, Please Review !", "info");
        return false;
    }});
});


var typed = new Typed('#element', {

    strings: [
        'are a job agency',
        'offer you job',
        'work with IT solutions',
        'are the best agency'
    ],
    typeSpeed: 50,
    backSpeed: 30,
    loop: true,
});
//jQuery(function($){
//    $(document).ajaxSend(function(){
//        $('#bg-spinner').fadeIn(500);
//    });
//    $('.bg-send').click(function(){
//        $.ajax({
//        type: 'GET,
//        success: function (data){
//            var d = $.parseJson(data);
//            alert(d.Test);
//        }
//        }).done(function(){
//        setTimeout(function(){
//            $('#bg-spinner').fadeOut(500);
//        }, 700);
//        });
//    });
//});
//$('.btn-send').click(function(){
//    var name = $('#name').val();
//    var age = $('#age').val();
//    var email = $('#email').val();
//    var phone = $('#phone').val();
//    var address = $('#address').val();
//    var experience = $('#experience').val();
//    var file = $('#file').val();
//
//    if ( (name != '') && (age != '') && (email != '')
//    && (phone != '') && (address != '') && (experience != '')
//    && (file != '') ){
//        $('.close-modal').modal('hide');
//    }
//})