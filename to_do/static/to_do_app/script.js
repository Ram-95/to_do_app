$(document).ready(function(){

	/*if ($("#maintable tbody tr").length == 0) {
		alert('Length is ' + $("#maintable").length);
		var new_row = '<tr><td><button type="button" class="btn btn-success" id="add-new-row"><strong>Add New Task</strong></button></td></tr>'
		$("#maintable").append(new_row);


	};*/

	//Adds a New Row to the Table

	$(document).on("click", "#add-new-row", function() {
		//$(this).parent().parent().remove();
		var row = '<tr><td><input type="checkbox" title="Mark as Done" class="form-check-input" id="exampleCheck"></td><td><input type="text" name="task" class="form-control" placeholder="Enter your Task" maxlength="60"></td><td><button type="button" style="float: right;" class="btn btn-danger deleterow" title="Delete this task">Delete</button></td></tr>';
		$("#maintable").append(row);
	});

	/*//Adds a row to the To-Do List
	$(document).on("click", ".addrow", function() {
	var row = '<tr><td><input type="checkbox" title="Mark as Done" class="form-check-input" id="exampleCheck"></td><td><input type="text" class="form-control" placeholder="Enter your Task"></td><td class="button-row"><button type="button" class="btn btn-success addrow">Add Task</button> &nbsp; &nbsp; &nbsp;<button type="button" class="btn btn-danger deleterow" title="Delete this task">Delete</button></td></tr>';
		   $("#maintable").append(row);
	});
	*/


	//Deletes the selected row
	$(document).on("click", ".deleterow", function() {
       $(this).parent().parent().remove();
	});

	/* Moves the row from Active Tasks Table to Complete Tasks Table and Vice versa */
	$("table").on('click', ".mark_as_done, .mark_as_undone", function() {
        if($(this).hasClass('mark_as_done')) {
           // Script to Move the task from Active Table to Complete Table
           var check_id;
           check_id = $(this).attr("id");
           class_name = $(this).attr("class");
           //alert('Class: ' + class_name)
           task_name = $("#title"+check_id).html();
           //alert('Task is: ' + task_name);
           $.ajax(
           {
                // Method of sending the Data.
                type: "GET",
                // URL to which the Data should be sent to.
                url: "/move_tasks",
                // Data - We're sending the selected Task's ID and CLASS Name to the URL.
                data: {
                        task_id: check_id,
                        task_class: class_name
                      },
                success: function()
                {
                    //Remove from the Active Table
                    $("#"+check_id).parent().parent().remove();
                    //Append to the Complete Table
                    var row = '<tr><td><input type="checkbox" title="Completed" class="form-check-input mark_as_undone" id="'+ check_id +'" checked></td><td><h4 align="left" id="title'+ check_id + '" class="completed_tasks">'+ task_name + '</h4></td><td class="button-row"></td></tr>';
                    $('#completed-table').append(row);

                }
           })
        }
        else {
           //Script to Move the Tasks from Complete Table to Active Table
           var un_check_id;
           un_check_id = $(this).attr("id");
           task_name = $("#title"+un_check_id).html();
           class_name = $(this).attr("class");
           //alert('Task is: ' + task_name);
           $.ajax(
           {
                type: "GET",
                url: "/move_tasks",
                data: {
                        task_id: un_check_id,
                        task_class: class_name
                },
                success: function()
                {
                    //Remove from the Completed Table
                    $("#"+un_check_id).parent().parent().remove();
                    //Append to the Active Table
                    var row = '<tr><td><input type="checkbox" title="Mark as Done" class="form-check-input mark_as_done" id="' + un_check_id + '"></td><td><h4 align="left" id="title' + un_check_id + '">' + task_name + '</h4></td><td><button type="button" style="float: right;" class="btn btn-danger deleterow" title="Delete this task">Delete</button></td></tr>'
                    $('#maintable').append(row);
                }
           })
        }

    });

});