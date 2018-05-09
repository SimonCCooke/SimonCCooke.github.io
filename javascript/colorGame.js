var colors = []

var easyColors = ["white","silver","gray","black","red","maroon","yellow","olive","lime","green","aqua","teal","blue","navy","fuchsia","purple"]

var difficulty = 1;

var numSquares = 6;

var hardColors =          ["IndianRed","LightCoral","Salmon","DarkSalmon","LightSalmon","Crimson","Red","FireBrick","DarkRed","Pink","LightPink","HotPink","DeepPink","MediumVioletRed","PaleVioletRed","LightSalmon","Coral","Tomato","OrangeRed","DarkOrange","Orange","Gold","Yellow","LightYellow","LemonChiffon","LightGoldenrodYellow","PapayaWhip","Moccasin","PeachPuff","PaleGoldenrod","Khaki","DarkKhaki","Lavender","Thistle","Plum","Violet","Orchid","Fuchsia","Magenta","MediumOrchid","MediumPurple","Amethyst","BlueViolet","DarkViolet","DarkOrchid","DarkMagenta","Purple","Indigo","SlateBlue","DarkSlateBlue","MediumSlateBlue","GreenYellow","Chartreuse","LawnGreen","Lime","LimeGreen","PaleGreen","LightGreen","MediumSpringGreen","SpringGreen","MediumSeaGreen","SeaGreen","ForestGreen","Green","DarkGreen","YellowGreen","OliveDrab","Olive","DarkOliveGreen","MediumAquamarine","DarkSeaGreen","LightSeaGreen","DarkCyan","Teal","Aqua","Cyan","LightCyan","PaleTurquoise","Aquamarine","Turquoise","MediumTurquoise","DarkTurquoise","CadetBlue","SteelBlue","LightSteelBlue","PowderBlue","LightBlue","SkyBlue","LightSkyBlue","DeepSkyBlue","DodgerBlue","CornflowerBlue","MediumSlateBlue","RoyalBlue","Blue","MediumBlue","DarkBlue","Navy","MidnightBlue","Cornsilk","BlanchedAlmond","Bisque","NavajoWhite","Wheat","BurlyWood","Tan","RosyBrown","SandyBrown","Goldenrod","DarkGoldenrod","Peru","Chocolate","SaddleBrown","Sienna","Brown","Maroon","White","Snow","Honeydew","MintCream","Azure","AliceBlue","GhostWhite","WhiteSmoke","Seashell","Beige","OldLace","FloralWhite","Ivory","AntiqueWhite","Linen","LavenderBlush","MistyRose","Gainsboro","LightGrey","Silver","DarkGray","Gray","DimGray","LightSlateGray","SlateGray","DarkSlateGray","Black"]

colors = generateRandomColors(numSquares);

var squares = document.querySelectorAll(".colorGameSquare");
var ans = colors[Math.floor(Math.random() * colors.length)].toLowerCase();
var colorDisplay = document.getElementById("colorDisplay");
var messageDisplay = document.querySelector("#message");
var newGame = document.querySelector("#newGame");
var easy = document.querySelector("#easy");
var hard = document.querySelector("#hard");

colorDisplay.textContent = ans;

newGame.addEventListener("click", function(){
  colors = generateRandomColors(numSquares);
  ans = colors[Math.floor(Math.random() * colors.length)].toLowerCase();
  colorDisplay.textContent = ans;
  messageDisplay.textContent = "";
  messageDisplay.style.color = "black";
  for(var i = 0; i<squares.length; i++){
    squares[i].style.backgroundColor = colors[i];
  };
  });

easy.addEventListener("click", function(){
  difficulty = 1;
});

hard.addEventListener("click", function(){
  difficulty = 2;
});

for(var i = 0; i<squares.length; i++){
  squares[i].style.backgroundColor = colors[i];

  squares[i].addEventListener("click", function(){
    var clickedColor = this.style.backgroundColor.toLowerCase();
    if(clickedColor === ans){
      messageDisplay.textContent = "Correct!";
      messageDisplay.style.color = clickedColor;
      changeColors(clickedColor);
    } else {
      this.style.backgroundColor = "#3AAFA9";
      messageDisplay.textContent = "Try Again.";
    }
  });
};

function changeColors(color){
  for(var i = 0; i < colors.length; i++){
    squares[i].style.backgroundColor = color;
  }
}

function pickColor(){
  if(difficulty === 1){
    return easyColors[Math.floor(Math.random() * easyColors.length)];
  } else {
    return hardColors[Math.floor(Math.random() * hardColors.length)];
  }
}

function generateRandomColors(num){
  var colorsArray = [];
  for(var i = 0; i < num; i++){
    colorsArray[i] = pickColor();
  }
  return colorsArray;
}
