$(function(){
    $('#submit').click(function(){
        var new_p = $('#new').val();
        var confirm_p = $('#confirm').val();
        if(new_p != confirm_p){
            $('#error_mes').html('两次密码输入不一致');
            return false;
        }
    })       
})
