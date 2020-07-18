$(document).ready(function(){

	//Adds a New Row to the Table

	$(document).on("click", "#add-new-row", function() {
		//$(this).parent().parent().remove();
		var row = '<tr><td><input type="checkbox" title="Mark as Done" class="form-check-input" id="exampleCheck"></td><td colspan="2"><span><input type="text" name="task" style="float: left;" class="form-control add_task" placeholder="Enter your Task" maxlength="60"></td></span><td><button class="btn btn-side" id="add_task_btn" title="Add Task" style="background-color: green;"><i class="fa fa-plus"></i></button>&nbsp;&nbsp;<button title="Delete this Task" class="btn btn-side deleterow"><i class="fa fa-close"></i></button></td></tr>';
		if($('.add_task').length == 0) {
    		$("#maintable").append(row);
		}
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

	/* Adding a New Task to the Database and show the same in the Active Task Table */
	$("table").on('click', "#add_task_btn", function() {
	    var task_name;
	    // Getting the Task Name
	    task_name = $('.add_task').val();
	    if (task_name != "") {
            $.ajax(
            {
                type: "GET",
                url: "/add_new_task",
                data: {
                        task_title: task_name,
                },
                success: function(data) //This will get the data returned by the /add_new_task end point in JSON Format.
                {
                    //'data' variable is in JSON Format. {key: value}
                    // The task_id that is generated for the newly added Task is present in the task_id variable
                    task_id = data.id;
                    task_name = data.task_title;

                    //Remove the current row
                    $("#add_task_btn").parent().parent().remove();

                    //Add the added task to the Active Tasks Table
                    var row = '<tr><td><input type="checkbox" title="Mark as Done" class="form-check-input mark_as_done" id="' + task_id + '"></td><td colspan="2"><h4 align="left" id="title' + task_id + '">' + task_name + '</h4></td><td><button class="btn btn-side deleterow" title="Delete this Task" style="float: right;"><i class="fa fa-close"></i></button></td></tr>';
                    $('#maintable').append(row);
                }
            })
        }
        else {
            alert('Enter a Valid Task Name!');
        }
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
                    var row = '<tr><td><input type="checkbox" title="Mark as Undone" class="form-check-input mark_as_undone" id="'+ check_id +'" checked></td><td><h4 align="left" id="title'+ check_id + '" class="completed_tasks">'+ task_name + '</h4></td><td class="button-row"></td></tr>';
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
                    var row = '<tr><td><input type="checkbox" title="Mark as Done" class="form-check-input mark_as_done" id="' + un_check_id + '"></td><td colspan="2"><h4 align="left" id="title' + un_check_id + '">' + task_name + '</h4></td><td><button class="btn btn-side deleterow" title="Delete this Task" style="float: right;"><i class="fa fa-close"></i></button></td></tr>';
                    $('#maintable').append(row);
                }
           })
        }

    });

});