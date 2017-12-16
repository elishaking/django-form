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

    $("#id_are_you_a_communicant").change(() => {
        if($("#id_are_you_a_communicant").val() == "N"){
            $("#div_id_not_communicant").addClass("has-error");
            $("#div_id_not_communicant").removeClass("hide");
            $("#id_not_communicant").attr("required", true);
        } else{
            $("#div_id_not_communicant").addClass("hide");
            $("#div_id_not_communicant").removeClass("has-error");
            $("#id_not_communicant").removeAttr("required");
        }
    });

    $("#id_are_you_confirmed").change(() => {
        if($("#id_are_you_confirmed").val() == "N"){
            $("#div_id_not_confirmed").addClass("has-error");
            $("#div_id_not_confirmed").removeClass("hide");
            $("#id_not_confirmed").attr("required", true);
        } else{
            $("#div_id_not_confirmed").addClass("hide");
            $("#div_id_not_confirmed").removeClass("has-error");
            $("#id_not_confirmed").removeAttr("required");
        }
    });

        $("#id_are_wedded_in_the_church").change(() => {
        if($("#id_are_wedded_in_the_church").val() == "N"){
            $("#div_id_not_wedded").addClass("has-error");
            $("#div_id_not_wedded").removeClass("hide");
            $("#id_not_wedded").attr("required", true);
        } else{
            $("#div_id_not_wedded").addClass("hide");
            $("#div_id_not_wedded").removeClass("has-error");
            $("#id_not_wedded").removeAttr("required");
        }
    });

    $("#id_any_tribal_community").change(() => {
        if($("#id_any_tribal_community").val() == "N"){
            $("#div_id_in_tribal_community").addClass("hide");
            $("#div_id_not_in_tribal_community").addClass("has-error");
            $("#div_id_not_in_tribal_community").removeClass("hide");
            $("#id_not_in_tribal_community").attr("required", true);
        } else{
            $("#div_id_not_in_tribal_community").addClass("hide");
            $("#div_id_in_tribal_community").addClass("has-error");
            $("#div_id_in_tribal_community").removeClass("hide");
            $("#id_in_tribal_community").attr("required", true);
        }
    });

        $("#id_member_of_any_pius_society").change(() => {
        if($("#id_member_of_any_pius_society").val() == "N"){
            $("#div_id_yes_In_pius_society").addClass("hide");
            $("#div_id_not_in_pius_society").addClass("has-error");
            $("#div_id_not_in_pius_society").removeClass("hide");
            $("#id_not_in_pius_society").attr("required", true);
        } else{
            $("#div_id_not_in_pius_society").addClass("hide");
            $("#div_id_in_any_pius_society").addClass("has-error");
            $("#div_id_in_any_pius_society").removeClass("hide");
            $("#id_yes_In_pius_society").attr("required", true);
        }
    });

});