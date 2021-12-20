/** Connect Four
 *
 * Player 1 and 2 alternate turns. On each turn, a piece is dropped down a
 * column until a player gets four-in-a-row (horiz, vert, or diag) or until
 * board fills (tie)
 */

const COLUMNS = 7;
const HEIGHT = 6;

let currPlayer = 1; // active player: 1 or 2
let pieceCount = 0; //number of pieces that have been played so far
let board = []; // array of rows, each row is array of cells  (board[y][x])

/** makeBoard: create in-JS board structure:
 *    board = array of rows, each row is array of cells  (board[y][x])
 */

function makeBoard() {
  for (let i = 0; i < HEIGHT; i++) {  
    board[i] =[];
    for (let j = 0; j < COLUMNS; j++) {
      board[i][j] = null;
    }
  }
  return board;
}

  // TODO: set "board" to empty HEIGHT x COLUMNS matrix array

/** makeHtmlBoard: make HTML table and row of column tops. */

function makeHtmlBoard() {
  let htmlBoard = document.getElementById("board");
  let top = document.createElement("tr"); 
  top.setAttribute("id", "column-top");
  top.addEventListener("click", handleClick); //checks for if the top opening element has been clicked to drop the piece

  for (let x = 0; x < COLUMNS; x++) {
    let headCell = document.createElement("td");
    headCell.setAttribute("id", x); //set each element in the top row with an id corresponding to the column number
    top.append(headCell);
  }
  htmlBoard.append(top);

  for (let y = 0; y < HEIGHT; y++) {
    const row = document.createElement("tr"); //create each row element
    for (let x = 0; x < COLUMNS; x++) {
      const cell = document.createElement("td"); //create 7 elements for each row
      cell.setAttribute("id", `${y}-${x}`); //set the id of each element in each row
      row.append(cell);
    }
    htmlBoard.append(row); //append each row element to the html board
  }
}

/** findSpotForCol: given column x, return top empty y (null if filled) */

function findSpotForCol(x) {
   for (let i = HEIGHT - 1 ; i >= 0 ; i--) {
    if(!board[i][x]) {
      return i;
    }
  }
  return null;
} 

/** placeInTable: update DOM to place piece into HTML table of board */

function placeInTable(y, x) {
  // TODO: make a div and insert into correct table cell
  let piece = document.createElement("div");
  piece.classList.add("piece");
  piece.classList.add(`p${currPlayer}`);

  ++pieceCount; //increment pieces played by one each time the top row is clicked to populate the board
  const celltoPlace = document.getElementById(`${y}-${x}`);
  celltoPlace.append(piece);
}

/** endGame: announce game end */

function endGame(msg) {
  alert(msg);
}

/** handleClick: handle click of column top to play piece */

function handleClick(evt) {
  // get x from ID of clicked cell
  let x = +evt.target.id;

  // get next spot in column (if none, ignore click)
  let y = findSpotForCol(x);
  if (y === null) {
    return;
  }

  // place piece in board and add to HTML table
  board[y][x] = currPlayer;
  placeInTable(y, x);

  // check for win
  if (checkForWin()) {
    return endGame(`Player ${currPlayer} won!`);
  }

  // check for tie
  if(pieceCount === HEIGHT * COLUMNS) {
    return endGame("This is a tie!");
  };

  // switch players
  currPlayer = currPlayer === 1 ? 2: 1;

}

/** checkForWin: check board cell-by-cell for "does a win start here?" */

function checkForWin() {
  function _win(cells) {
    // Check four cells to see if they're all color of current player
    //  - cells: list of four (y, x) cells
    //  - returns true if all are legal coordinates & all match currPlayer

    return cells.every(
      ([y, x]) =>
        y >= 0 &&
        y < HEIGHT &&
        x >= 0 &&
        x < COLUMNS &&
        board[y][x] === currPlayer
    );
  }

  // TODO: read and understand this code. Add comments to help you.

  //Store all of the (y,x) four cell lines of connecting fours
  for (let y = 0; y < HEIGHT; y++) {
    for (let x = 0; x < COLUMNS; x++) {
      let horiz = [[y, x], [y, x + 1], [y, x + 2], [y, x + 3]];
      let vert = [[y, x], [y + 1, x], [y + 2, x], [y + 3, x]];
      let diagDR = [[y, x], [y + 1, x + 1], [y + 2, x + 2], [y + 3, x + 3]];
      let diagDL = [[y, x], [y + 1, x - 1], [y + 2, x - 2], [y + 3, x - 3]];

      // check to see if there's a match with the possible win combinations
      if (_win(horiz) || _win(vert) || _win(diagDR) || _win(diagDL)) {
        return true; 
      }
    }
  }
}

makeBoard();
makeHtmlBoard();
