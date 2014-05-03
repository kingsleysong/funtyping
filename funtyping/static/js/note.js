$(function(){
    $('#older').click(function(){
        note = get_older_note();
        return false;
    });

    $('#newer').click(function(){
        note = get_newer_note();
        return false;
    });

    $('#random').click(function(){
        note = get_random_note();
        return false;
    });
});
function get_older_note(){
    var note_id = $('#note_id').val();
    $.getJSON(
        '/get_older_note',
        {note_id:note_id},
        function(data){
            show_note(data);
        }
    );
}

function get_newer_note(){
    var note_id = $('#note_id').val();
    $.getJSON(
        '/get_newer_note',
        {note_id:note_id},
        function(data){
            show_note(data);
        }
    );
}

function get_random_note(){
    var note_id = $('#note_id').val();
    $.getJSON(
        '/get_random_note',
        {note_id:note_id},
        function(data){
            show_note(data);
        }
    );
}

function show_note(note){
    var note_id = $('#note_id');
    var note_time = $('#note_time');
    var note_weekday = $('#note_weekday');
    var note_content = $('#note_content');
    note_id.val(note.id);
    note_time.html(note.time);
    note_weekday.html(note.weekday);
    note_content.html(note.content);
}


