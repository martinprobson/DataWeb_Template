/*!
 * Workaround to highlight the Nav bar item associated with the current page.
 * 
 */

if (typeof jQuery === 'undefined') {
  throw new Error('The script requires jQuery')
}
$(document).ready(function() {
	var d = $('#nav_id').data();
	var nav_id = d.name;
	console.log("Hello")
    $('li[name="' + nav_id +  '"]').addClass("active");
    $('li[name!="' + nav_id +  '"]').removeClass("active");
});