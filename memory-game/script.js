const gameContainer = document.getElementById("game");

const COLORS = [
  "red",
  "blue",
  "green",
  "orange",
  "purple",
  "brown",
  "red",
  "blue",
  "green",
  "orange",
  "purple",
  "brown"
];

let cardsColors = [];
let selectedCards = [];
let storedCards = [];
let cardsFlipped = 0;
let clickDisabled = false;

// here is a helper function to shuffle an array
// it returns the same array with values shuffled
// it is based on an algorithm called Fisher Yates if you want to research more
function shuffle(array) {
  let counter = array.length;

  // While there are elements in the array
  while (counter > 0) {
    // Pick a random index
    let index = Math.floor(Math.random() * counter);

    // Decrease counter by 1
    counter--;

    // And swap the last element with it
    let temp = array[counter];
    array[counter] = array[index];
    array[index] = temp;
  }

  return array;
}

let shuffledColors = shuffle(COLORS);

// this function loops over the array of colors
// it creates a new div and gives it a class with the value of the color
// it also adds an event listener for a click for each card
function createDivsForColors(colorArray) {
  for (let color of colorArray) {
    // create a new div
    const newDiv = document.createElement("div");
 
    // give it a class attribute for the value we are looping over
    newDiv.classList.add(color);

    //**define a unique id for each card for ease of access** 
    let uniqueId = Date.now() + Math.random();
    newDiv.id = uniqueId;
    
    newDiv.addEventListener("click", handleCardClick);

    // append the div to the element with an id of game
    gameContainer.append(newDiv);  
  }
}

// TODO: Implement this function!
function handleCardClick(event) {
  // you can use event.target to see which element was clicked

  if (clickDisabled) {
    return;
  }
  let pickedCard = event.target;
  
  if (pickedCard.classList.contains("flipped")){
    return;
  }
  let pickedCardColor = pickedCard.classList[0];
  pickedCard.classList.add("flipped");
  
  pickedCard.style.backgroundColor = pickedCardColor;
  selectedCards.push(pickedCard);

  if (selectedCards.length == 2) {
    clickDisabled = true;
    checkforMatches();
  }
  
} 


function checkforMatches() {
   
   let card1 = selectedCards[0];
   let card2 = selectedCards[1];

   let card1Color = card1.classList[0];
   let card2Color = card2.classList[0];
   //compare the colors of card 1 and 2 to find a match
   if (card1Color === card2Color) {
     
     console.log("You have found a match");
     cardsFlipped += 2;
    
     card1.removeEventListener("click", handleCardClick);
     card2.removeEventListener("click", handleCardClick); 
     
     selectedCards = [];
     clickDisabled = false;
   }

   else { 
      setTimeout(function(){
        clickDisabled = false;
        card1.style.backgroundColor = "";
        card2.style.backgroundColor = ""; 
        card1.classList.remove("flipped");
        card2.classList.remove("flipped");
        selectedCards = [];
      }, 1000);
   }
   
   if (cardsFlipped === COLORS.length) {
     setTimeout(function(){alert("game over!")},1000);
   }
}

// when the DOM loads
createDivsForColors(shuffledColors);