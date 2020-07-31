$(document).ready(function(){

	/* Adds a New Row to the Table */
	$(document).on("click", "#add-new-row", function() {
		var row = '<tr><td colspan="3"><input type="text" name="task" style="float: left;" class="form-control add_task" placeholder="Enter your Task" maxlength="60"></td><td><button class="btn btn-side" id="add_task_btn" title="Save" style="background-color: green; float: left;"><i class="fa fa-save"></i></button><button title="Delete this Task" style="float: right;" class="btn btn-side deleterow delete_new_row"><i class="fa fa-close"></i></button></td></tr>';
		if($('.add_task').length == 0) {
		    // Append the new row to the tbody of the table and not the Table.
    		$("#maintable > tbody").append(row);
		}
	});

    /* Script to fadeout flash messages after 5 seconds */
    window.setTimeout(function() {
          $(".alert").fadeTo(500, 0).slideUp(500, function(){
              $(this).remove();
          });
        }, 5000);
    
    /* Refreshes the Content of Tables when any AJAX Call is Successful */
    function refreshData() {
         /* Refreshes both the tables with new Data we got by AJAX Calls */
         $( "#maintable" ).load(window.location.href + " #maintable" );
         //console.log('MainTable Refresh Complete');
         $( "#completed-table" ).load(window.location.href + " #completed-table" );
         //console.log('Completed Table Refresh Complete');
    }


	/* Deletes the selected row */
	$(document).on("click", ".delete_existing_row, .delete_new_row", function() {
	    // If the delete button of new row is clicked, then delete that row
	    if($(this).hasClass('delete_new_row')) {
            $(this).parent().parent().remove();
        }
        // If the delete button of existing row is clicked, Delete that task from DB and delete if from table as well
        else {
            // Gets the ID of the Task i.e Checkbox
            var val = $(this).parent().parent().find('input').attr("id");
            // AJAX Call - Will pass the task_id to be deleted to the delete_task view and upon success will remove the same from the Active task table
            $.ajax(
            {
                type: "POST",
                url: "/delete_task/",
                cache: false,
                data: {
                       task_id: val,
                },
                success: function()
                {
                    refreshData();
                }
            });
        }

      });



    /* Deletes all the Completed Tasks */
    $("#completed-table").on('click', '#clear_all_completed_tasks', function() {
        // Checks if the Number of rows in Completed Table. If less than or equal to 2 then alerts the user with appropriate message
        // Else Deletes all the Completed Tasks
        if($('#completed-table tr').length <= 2) {
            alert('No Completed Tasks to Clear!');
        }
        else
        {
               $.ajax(
               {
                   type: "POST",
                   url: "/delete_all_completed_tasks/",
                   data:{},
                   success: function()
                   {
                        refreshData();
                   }
               })
        }
    });


	/* Adding a New Task to the Database and show the same in the Active Task Table */
	$("table").on('click', "#add_task_btn", function() {
	    var task_name;
	    // Getting the Task Name
	    task_name = $('.add_task').val();
	    if (task_name != "") {
            $.ajax(
            {
                type: "POST",
                url: "/add_new_task/",
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
                    //$("#add_task_btn").parent().parent().remove();

                    //Add the added task to the Active Tasks Table
                    //var row = '<tr><td><input type="checkbox" title="Mark as Done" class="form-check-input mark_as_done" id="' + task_id + '"></td><td colspan="2"><h4 align="left" id="title' + task_id + '">' + task_name + '</h4></td><td><button class="btn btn-side deleterow delete_existing_row" title="Delete this Task" style="float: right;"><i class="fa fa-close"></i></button></td></tr>';
                    //$('#maintable').append(row);
                    refreshData();
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
                type: "POST",
                // URL to which the Data should be sent to.
                url: "/move_tasks/",
                // Data - We're sending the selected Task's ID and CLASS Name to the URL.
                data: {
                        task_id: check_id,
                        task_class: class_name
                      },
                success: function()
                {
                    //Remove from the Active Table
                    //$("#"+check_id).parent().parent().remove();
                    //Append to the Complete Table
                    //var row = '<tr><td><input type="checkbox" title="Mark as Undone" class="form-check-input mark_as_undone" id="'+ check_id +'" checked></td><td><h4 align="left" id="title'+ check_id + '" class="completed_tasks">'+ task_name + '</h4></td><td class="button-row"></td></tr>';
                    //$('#completed-table').append(row);
                    refreshData();

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
                type: "POST",
                url: "/move_tasks/",
                data: {
                        task_id: un_check_id,
                        task_class: class_name
                },
                success: function()
                {
                    //Remove from the Completed Table
                    //$("#"+un_check_id).parent().parent().remove();
                    //Append to the Active Table
                    //var row = '<tr><td><input type="checkbox" title="Mark as Done" class="form-check-input mark_as_done" id="' + un_check_id + '"></td><td colspan="2"><h4 align="left" id="title' + un_check_id + '">' + task_name + '</h4></td><td><button class="btn btn-side deleterow delete_existing_row" title="Delete this Task" style="float: right;"><i class="fa fa-close"></i></button></td></tr>';
                    //$('#maintable').append(row);
                    refreshData();
                }
           })
        }

    });

});