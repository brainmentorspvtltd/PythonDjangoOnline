$(document).ready(function() {
    // console.log("Document Ready");
    $("#box_1").change(function() {
        var str = $(this).val();
        // console.log(str);
        $.ajax({
            url: 'validate/?emp_id=' + str,
            method: 'get',
            success: function(data) {
                console.log(data);
                $("#err").html(data);
            }
        })
    })
});