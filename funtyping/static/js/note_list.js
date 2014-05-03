$(function(){
    var datenum = $('#datenum_hidden').val();
    if(datenum==''){
        $('#date_sel_all').addClass('on');
    }
    else{
        $('#date_sel_'+datenum).addClass('on');
    }
});
