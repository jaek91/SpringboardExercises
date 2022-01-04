/** Given a query string, return array of matching shows:
 *     { id, name, summary, episodesUrl }
 */


/** Search Shows
 *    - given a search term, search for tv shows that
 *      match that query.  The function is async show it
 *       will be returning a promise.
 *
 *   - Returns an array of objects. Each object should include
 *     following show information:
 *    {
        id: <show id>,
        name: <show name>,
        summary: <show summary>,
        image: <an image from the show data, or a default imege if no image exists, (image isn't needed until later)>
      }
 */

async function searchShows(query) {
  const url = await axios.get("http://api.tvmaze.com/search/shows", {params: {q:query}});
  let resultArr = url.data;
  let final = [];
  for (el of resultArr) {
    final.push({
      id: el.show.id,
      name: el.show.name,
      summary: el.show.summary,
      image: el.show.image ? el.show.image.medium : "http://tinyurl.com/tv-missing"
    })
  }
     return final;
}


/** Populate shows list:
 *     - given list of shows, add shows to DOM
 */

function populateShows(shows) {
  const $showsList = $("#shows-list");
  $showsList.empty();

  for (let show of shows) {
    let $item = $(
      `<div class="col-md-6 col-lg-3 Show" data-show-id="${show.id}">
         <div class="card" data-show-id="${show.id}">
           <img class="card-img-top" src="${show.image}">
           <div class="card-body">
             <h5 class="card-title">${show.name}</h5>
             <p class="card-text">${show.summary}</p>
             <button class="btn btn-primary get-episodes">Episodes</button>
           </div>
         </div>
       </div>
      `);

    $showsList.append($item);
     $(".get-episodes").click( async function(evt) {
      let showid = $(evt.target).closest(".Show").data("show-id");
      let eps = await getEpisodes(showid);
      populateEpisodes(eps);
    }) 
  }
}


/** Handle search form submission:
 *    - hide episodes area
 *    - get list of matching shows and show in shows list
 */

$("#search-form").on("submit", async function handleSearch (evt) {
  evt.preventDefault();

  let query = $("#search-query").val();
  if (!query) return;

   $("#episodes-area").hide(); 

  let shows = await searchShows(query);

  populateShows(shows);
});

async function getEpisodes(id) {
  let results = await axios.get(`http://api.tvmaze.com/shows/${id}/episodes`);

  let finalResults =  results.data.map(obj => ({
      id: obj.id, 
      name: obj.name,
      season: obj.season,
      number: obj.number
    }));
  return finalResults;
}

/**Used to populate the list of episode information */ 
function populateEpisodes(eps) {

let $epsList = $("#episodes-list");
$epsList.empty(); 

for (let ep of eps) {
  let $epInfo = $(`<li> ${ep.name} (season ${ep.season}, number ${ep.number}) </li>`);
  $epsList.append($epInfo);
  }

  $("#episodes-area").show();
}


/** Given a show ID, return list of episodes:
 *      { id, name, season, number }
 */

async function getEpisodes(id) {
  // TODO: get episodes from tvmaze
  //       you can get this by making GET request to
  //       http://api.tvmaze.com/shows/SHOW-ID-HERE/episodes
  let results = await axios.get(`http://api.tvmaze.com/shows/${id}/episodes`);

  let finalResults =  results.data.map(obj => ({
      id: obj.id, 
      name: obj.name,
      season: obj.season,
      number: obj.number
    })
  )
  return finalResults;
}

