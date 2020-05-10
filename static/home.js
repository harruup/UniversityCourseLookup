$(document).ready(function(){

        $("#submitsearch").click(function(){
        var input_val = $("#courseinput").val();
        if(input_val == ""){
            $('#homeinputerror').html("Please enter valid course code")
        }
        else{
            $("#form").submit();
        }
         });
 });