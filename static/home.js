$(document).ready(function(){

        $("#submitsearch").click(function(){
        var input_val = $("#courseinput").val();
        if(input_val == ""){
            alert("Please enter valid course code")
        }
        else{
            $("#form").submit();
        }
         });
 });