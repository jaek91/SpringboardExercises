
$("#movie-info").on("submit", function(evt){
    evt.preventDefault();
    let movieName = $("#movie-name").val();
    let movieScore =$("#movie-score").val();
    let movieData = {movieName, movieScore};
    const movieDataHTML = createMovieDataHTML(movieData);

    $("#table-content").append(movieDataHTML);

})

$("#table-content").on("click", ".del-btn", function(evt) {

    $(evt.target).closest("tr").remove();
})
function createMovieDataHTML(data) {
    return `
      <tr>
        <td>${data.movieName}</td>
        <td>${data.movieScore}</td>
        <td>
          <button class="del-btn">
            <span> 
                X
            <span>
          </button>
        </td>
      <tr>
    `;
}