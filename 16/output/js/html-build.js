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
	// windows text


	// add data to the properties box
	$('props-').prepend('number of floors is '+num_floors);
	$('props-').prepend('site elevation is '+$('site-').attr('elev')+'<br>');
	$('props-').prepend('Total number of windows: '+$('building-').attr('windows')+'<br>');

	
	// load the plan so we can edit it
	plan('Duplex building');
	
	//The .each() method is unnecessary here:
	$('floor-','window-').each(function() {
	console.log($('floor-','window-')[0].innerHTML);
	$( 'floor-','window-' ).on("click", function(){
			//$('plan-').css("background-color","black");
			
			changePlan($('floor-').attr('name')+':'+$('floor-').attr('level')+'<br>'+$('window-').attr('Level')+':'+$('window-').attr('count'));
			//$( this ).innerHTML
		});
	});
	
	//$( 'window-' ).each(function() {
	//console.log($(num_windows)[0].innerHTML);
	//$( this ).on("click", function(){
			//$('plan-').css("background-color","black");
			
	//		changePlan($(this).attr('Level')+':'+$(this).attr('count'));
	
			//$( this ).innerHTML
	//	});
	//});
	
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