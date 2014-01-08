$(function(){
    $(document).foundation();
    $("[data-match-height]").each(function() {
      var parentRow = $(this),
      childrenCols = $(this).find("[data-height-watch]"),
      childHeights = childrenCols.map(function(){ return $(this).height(); }).get(),
      tallestChild = Math.max.apply(Math, childHeights);

      childrenCols.css('min-height', tallestChild);
  });
});
