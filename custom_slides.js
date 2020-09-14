document.body.addEventListener('click', function(){
    Reveal.toggleOverview();
Reveal.on( 'fragmentshown', event => {
  // event.fragment = the fragment DOM element
alert();
} );
}); 

$(document).ready(function(){
alert();
Reveal.configure({
        transition: 'convex' // none/fade/slide/convex/concave/zoom
    })
	
)};
Reveal.on( 'ready', event => {
  // event.currentSlide, event.indexh, event.indexv
alert("test");
} );
Reveal.on( 'slidechanged', event => {
  // event.previousSlide, event.currentSlide, event.indexh, event.indexv

} );
