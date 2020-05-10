    $(document).ready(function(){
        var options = []
        $('#coursestaken option').each(function() {
            options.push($(this).val())
        });
        $("#addcourses").click(function(){
        var option_val = $("#cinput").val();
        if(option_val != "" && $('#coursestaken option[value="'+option_val+'"]').length == 0){
            options.push(option_val);
            $("#cinput").val('');
            $("#coursestaken").append(new Option(option_val, option_val));
        }
        else{
            $('#treeinputerror').html("Course Already added or input empty")
            $("#cinput").val('');
        }
         });
        $("#removecourses").click(function(){
        options = options.filter(function(elem){
        		return elem != $("#coursestaken option:selected").val();
        });

        $("#coursestaken option:selected").remove();
        });

        /*
            Clicking on buttons will add the course to options list
        $(".cantake").click(function(){
            if($('#coursestaken option[value="'+$(this).val()+'"]').length == 0){
                options.push($(this).val());
                $("#coursestaken").append(new Option($(this).val(), $(this).val()));
        }
        else{
            alert($(this).val()+" already added to the list")
            }
        });*/

        $("#buildbutton").click(function(){
            if($('#coursestaken').has('option').length == 0){
                $('#treeinputerror').html("Please add a course")
             }
            else{
                $('#form').append('<input type="hidden" id="hidden" name="hidden" value="'+options+'" />');
                $("#form").submit();
                }
             });
        });