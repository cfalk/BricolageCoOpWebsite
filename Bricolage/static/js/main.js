$(document).on("ready", function() {

Galleria.loadTheme(STATIC_URL+"js/themes/galleria.classic.min.js");
Galleria.run(".galleria", {
  thumbnails:"lazy",
  popupLinks:false,
  autoplay: 5000,
  imagePanSmoothness:20,
  transitionSpeed:1000
});

});
