$(document).ready(() => {
    $("#div_id_other_health_work").addClass("hide");
    $("#div_id_other_other_work").addClass("hide");
    $("#div_id_not_baptized").addClass("hide");

    $("#id_health_work_5").change(() => {

        if($("#id_health_work_5").is(":checked")){
            $("#div_id_other_health_work").addClass("has-error");
            $("#div_id_other_health_work").removeClass("hide");
            $("#id_other_health_work").attr("required", true);
            //  $("#id_health_work_5").parent().parent().append($(`<input id="other_work" class="textinput textInput form-control" id="id_yes_belong_to" maxlength="300" name="yes_belong_to" type="text">`));
        }else{
            $("#div_id_other_health_work").addClass("hide");
            $("#div_id_other_health_work").removeClass("has-error");
            $("#id_other_health_work").removeAttr("required");
        }

    });

    $("#id_other_work_6").change(() => {

        if($("#id_other_work_6").is(":checked")){
            $("#div_id_other_other_work").addClass("has-error");
            $("#div_id_other_other_work").removeClass("hide");
            $("#id_other_other_work").attr("required", true);
            //  $("#id_health_work_5").parent().parent().append($(`<input id="other_work" class="textinput textInput form-control" id="id_yes_belong_to" maxlength="300" name="yes_belong_to" type="text">`));
        }else{
            $("#div_id_other_other_work").addClass("hide");
            $("#div_id_other_other_work").removeClass("has-error");
            $("#id_other_other_work").removeAttr("required");
        }

    });

    $("#id_are_you_a_baptized_catholic").change(() => {
        if($("#id_are_you_a_baptized_catholic").val() == "N"){
            $("#div_id_not_baptized").addClass("has-error");
            $("#div_id_not_baptized").removeClass("hide");
            $("#id_not_baptized").attr("required", true);
        } else{
            $("#div_id_not_baptized").addClass("hide");
            $("#div_id_not_baptized").removeClass("has-error");
            $("#id_not_baptized").removeAttr("required");
        }
    });

});