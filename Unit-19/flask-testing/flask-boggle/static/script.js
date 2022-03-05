class BoggleGame {
    /* make a new game with given DOM id */
  
    constructor(boardId, secs = 60) {
      this.secs = secs; // length of each game
      this.showTimer();
  
      this.score = 0;
      this.words = new Set();
      this.board = $("#" + boardId);
  
      // we call "tick" every 1000 msec for the time
      this.timer = setInterval(this.tick.bind(this), 1000);
      $("#submit-word-form", this.board).on("submit", this.handleSubmit.bind(this));
    }

    showWord(word) {
        $(".words", this.board).append($("<li>", { text: word }));
    }
    
    showMessage(msg, cls) {
        $(".msg", this.board)
          .text(msg)
          .removeClass()
          .addClass(`msg ${cls}`);
    }

    showScore() {
        $("#score", this.board).text(this.score);
    }

/* handle submission of word: if the word is unique and valid then score & show */

  async handleSubmit(evt) {
    evt.preventDefault();
    const $word = $("#submitted-word", this.board);

    let userInput = $word.val();
    if (!userInput) return;

    if (this.words.has(userInput)) {
      this.showMessage(`Already found ${userInput}`, "err");
      return;
    }

    // check server for valid word
    const resp = await axios.get("/check-word", { params: { word: userInput }});
    if (resp.data.result === "not-word") {
      this.showMessage(`${userInput} is not a valid English word`, "err");
    } else if (resp.data.result === "not-on-board") {
      this.showMessage(`${userInput} is not a valid word on this board`, "err");
    } else {
      this.showWord(userInput);
      this.score += userInput.length;
      this.showScore();
      this.words.add(userInput);
      this.showMessage(`Added: ${userInput}`, "ok");
    }

    $word.val("").focus();
  }

  /* Update timer in DOM */

  showTimer() {
    $("#timer", this.board).text(this.secs);
  }

  /* Tick: handle a second passing in game */

  async tick() {
    this.secs -= 1;
    this.showTimer();

    if (this.secs === 0) {
      clearInterval(this.timer);
      await this.scoreGame();
    }
  }

  /* end of game: score and update message. */

  async scoreGame() {
    $("#submit-word-form", this.board).hide();
    const resp = await axios.post("/post-score", { score: this.score });
    if (resp.data.newRecord) {
      this.showMessage(`New record: ${this.score}`, "ok");
    } else {
      this.showMessage(`Final score: ${this.score}`, "ok");
    }
  }
}

