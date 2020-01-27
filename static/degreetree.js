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
            alert("Course Already added or input empty")
            $("#cinput").val('');
        }
         });
        $("#removecourses").click(function(){
        options = options.filter(function(elem){
        		return elem != $("#coursestaken option:selected").val();
        });

        $("#coursestaken option:selected").remove();
        });

        $(".cantake").click(function(){
            $("#coursestaken").append(new Option($(this).val(), $(this).val()));
            options.push($(this).val());
        });

        $("#form").submit(function(){
            $('#form').append('<input type="hidden" id="hidden" name="hidden" value="'+options+'" />');
        });


        });