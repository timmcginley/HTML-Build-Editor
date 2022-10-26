/* written by Tim McGinley 2022 */

// ok in here we need to include a lot of stuff.
// we need a menu... where would this fit?
// we need to start (over)loading stuff into the DOM.
// we need to split the screen into section and plan and KPIs and info - where should this go?


function main() {
	
	// calculate the floors
	const floors = document.getElementsByTagName("floor-");
	let num_floors = floors.length;
	console.log(num_floors);
	
	// add data to the properties box
	$('props-').prepend('number of floors is '+num_floors);
	$('props-').prepend('site elevation is '+$('site-').attr('elev')+'<br>');
	
	// load the plan so we can edit it
	plan('Please select floor to get properties'); // G12: Edited text
	
	// The .each() method is unnecessary here:
	$( 'floor-' ).each(function() {
	console.log($(this)[0].innerHTML);
		$( this ).on("click", function(){
			//$('plan-').css("background-color","black");
			
            // G12: New implemented code: 
            roomList = $(this).attr('roomnames'); // Calling the roomnames from floot_entities in the HTMLBuild.py code. Expressed as room = "['exmpl','string']"
			roomList = roomList.replace(/'/g, '"');	//JSON parse recognizes "" for strings
			roomList = JSON.parse(roomList);

			text = '<b>' + $(this).attr('name') + '</b><br>' // Written in bold as headline
			//+ 'Floor level: ' + $(this).attr('level')+'<br>' // Not necessary?
			//+ 'Elevation: ' + $(this).attr('elev') +'<br>' // Is already listed
			+ 'Number of rooms: ' + $(this).attr('rooms') +'<br><br>'
			+ '<i><u>Rooms:</u></i>' // Listing rooms on this floor in cursive
			+ '<ul>';


			for(let i=0; i < roomList.length; i++){
				text += '<li>'+ roomList[i] +'</li>';
			}
			+'</ul>';
			changePlan(text);
            // Until here
            
			//changePlan($(this).attr('name')+':'+$(this).attr('level')); // Deleted, otherwise it will overwrite the plan
            $('props-').prepend('The area of ' +$(this).attr('name') +' is ' +$(this).attr('area') +'<br>'); // Area output is implemented after the click.
			//$( this ).innerHTML
		});
        
	});
	
	
}

function plan(text) {
jQuery('<div>', {
    id: 'plan',
    class: 'plan',
    title: 'click a floor to see the plan',
	html:text
}).appendTo('plan-');  
jQuery('#plan').css("overflow-y", "scroll"); // G12: adds scrollbar	
}

function changePlan(text) {
	$('#plan').html(text);
}





// <project-> - title etc.... | <site-> - also menu? site specific data?
// ---------------------------------------------------------------------
// <building-> - name of the building? this then needs to split in two...
// could also be more views and show a 3d? but maybe left is consistent
// ---------------------------------------------------------------------
// #section                   |               #plan
// this shows the floors      |      this shows a floor in plan         |
// in section                 |                 #plan                   |
//    <floor...->              -----------------------------------------
//                            |                 <properties->           |
// ---------------------------------------------------------------------