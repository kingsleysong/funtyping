$(function(){
    $('#sure').click(function(){
        var email = $('#email').val();
        var password = $('#password').val();
        if(!email){
            $('#error_mes').html('邮箱不能为空');
            return false;
        }
        else if(!password){
            $('#error_mes').html('密码不能为空');
            return false;
        }
    })       
})
