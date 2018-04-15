// Select color input
// Select size input

// When size is submitted by the user, call makeGrid()
function makeGrid() {

// Your code goes here!
  var place = $("table");
  place.children().remove();
  var rows = $("#inputHeight").val();
  var cols = $("#inputWeight").val();
  for(var i = 0; i < rows; i++){
    $(place).append("<tr></tr>");
  }
  $("tr").each(function(index){for(var j = 0; j < cols; j++){
      $(this).append("<td></td>");
  }});
}

$("#sizePicker").submit(function(e){
  e.preventDefault();
  console.log($("#inputHeight").val());
  console.log($("#inputWeight").val());
  makeGrid();
});

$(function(){
  $("#pixelCanvas").on("click","td",function(){
    $(this).css("background-color", $("#colorPicker").val());
  });
});
