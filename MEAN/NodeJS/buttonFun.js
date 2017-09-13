
<script src="bower_components/jquery/dist/jquery.js"></script>
<style type="text/css">
button{
	background-color: blue;
	color: white;
}
.red{
	background-color: red;
}
.green{
	background-color: green;
}
</style>
<button>Click Me!</button>
<button>No, Click Me!!!</button>
<button>Me Me Me!!!</button>

<script type="text/javascript">



// This assignment will be to create an html page with a single Blue Button that responds to the following events:

// On Click the button should toggle between blue and red
// On Hover the button should turn green (the button should go back to its original color when you hover out)
// Optional:



$(document).on('click', 'button', function(){
	$(this).toggleClass("red");
});


$("button").hover(function(){
	$(this).addClass("green")
}, function(){ $(this).removeClass("green") });


// When the user presses the enter key another Button with the same events should appear on the page. (You will need to use dynamic content for this)

// Note: This assignment is designed to revisit functionality that you have already created and explain exactly how the functions are working. While you go through this assignment pay attention to the use of callbacks.


</script>
