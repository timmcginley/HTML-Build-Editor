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

	let vol_floor = 248*(num_floors-1) + 272;
	
	// add data to the properties box
	$('props-').prepend('number of floors is '+num_floors);
	$('props-').prepend('site elevation is '+$('site-').attr('elev')+'<br>');
	$('props-').prepend('volume is '+vol_floor);
	
	// load the plan so we can edit it
	plan('This figure shows the volume of each floor');
	
	// The .each() method is unnecessary here:
	$( 'floor-' ).each(function() {
	console.log($(this)[0].innerHTML);
		$( this ).on("click", function(){
			//$('plan-').css("background-color","black");
			
			changePlan($(this).attr('name')+':' +'Volume concrete [m3] = '+$(this).attr('volume'));
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
	
}

function changePlan(text) {
	$('#plan').html(text);
}

// HTML-Build DOM

// shoulds include...
/*





*/


// ---------------------------------------------------------------------
//   model                    |             view
//    '-> project             |               '-> plan               
//      '-> site              |       this shows a floor in plan        |
//        '-> building        |                                         |
// #section                   |               '-> props                 |
// this shows the floors      |      this shows the selected properties |
// in section                 |                                         |
//    <floor...->             |                                         |
//                            |                                         |
// ---------------------------------------------------------------------





