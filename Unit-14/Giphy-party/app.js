
const apiCode = "947BoRe85KgRfSEsHdSbLiiZp0KVaXCk";
const searchBar = document.querySelector("#search-bar");
const gifForm = document.querySelector("#gif-form");

gifForm.addEventListener('submit', async function(e){
   e.preventDefault();
   const gifs = await axios.get(`http://api.giphy.com/v1/gifs/search`, {params: {q: searchBar.value, api_key: apiCode}})
   getGIF(gifs)
})

function getGIF(gifs) {
    const gifsData = gifs.data;
    let randomgifIndex = Math.floor(Math.random()*(gifsData.data.length));
    const selectedGIF = gifsData.data[randomgifIndex];
    let imgSrc = selectedGIF.images.original.url;
    createGIF(imgSrc);
}

function createGIF(imgURL) {
    const gifContainer = document.querySelector("#gif-container"); 
    let img = document.createElement("img");
    img.src = imgURL; 
    gifContainer.append(img);
} 



