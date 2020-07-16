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

	/* Moves the row from To-Do list to Done list */
	// Checks if the Checkbox is Checked - That is if a task is Marked as Done
	$('.mark_as_done').click(function(){
        if (this.checked) {
           //alert('Mark as Complete?');
           var check_id;
           check_id = $(this).attr("id");
           task_name = $("#title"+check_id).html();
           //alert('Task is: ' + task_name);
           $.ajax(
           {
                type: "GET",
                url: "/mark_as_done",
                data: {
                        task_id: check_id
                      },
                success: function()
                {
                    //Remove from the Active Table
                    $("#"+check_id).parent().parent().remove();
                    //Append to the Complete Table
                    var row = '<tr><td><input type="checkbox" title="Completed" class="form-check-input mark_as_undone" id="'+ check_id +'" checked></td><td><h4 align="left" class="completed_tasks">'+ task_name + '</h4></td><td class="button-row"></td></tr>';
                    $('#completed-table').append(row);

                }
           })
        }
    });

    // Check if the task is marked as Undone - Unchecked
    $('.mark_as_undone').click(function(){
           alert('Mark as UnDone?');
    });
});