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

	let Cost_estimate = 1.575*(num_floors)
	
	// add data to the properties box
	$('props-').prepend(' Number of floors is '+num_floors);
	
	$('props-').prepend(' The total cost of the building is '+Cost_estimate+"M"+".");
	$('props-').prepend("C = Columns, B = Beams, W = Walls, S = Slabs.");

	// load the plan so we can edit it
	plan('Press each level to see estimated cost of floor.');
	
	// The .each() method is unnecessary here:
	$( 'floor-' ).each(function() {
	console.log($(this)[0].innerHTML);
		$( this ).on("click", function(){
			//$('plan-').css("background-color","black");
			
			changePlan($(this).attr('name')+':' + "&nbsp"+ "The cost of this floor is " +$(this).attr('Cost_estimate') + "." +"&nbsp"+"This estimation is based on" +"&nbsp" +$(this).attr('Columns') +"C"  + "," + "&nbsp" +$(this).attr('Beams')+"B"+ "," + "&nbsp" +$(this).attr('Walls')+"W"+ "," + "&nbsp" +$(this).attr('Slabs')+"S"+".");
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





