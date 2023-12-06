function newReview() {
    // Redirect the user to the desired page
    window.location.href = "newReview";
  }

  function addReview() {
    // Redirect the user to the desired page
    window.location.href = "addReview";
  }

function albumChanged()
{
  var album = document.getElementById("album-select");
  var artist = document.getElementById("artist-textbox");

}

// function jukebox(dataList)

function jukebox(album, artist, bestGenre)
{
  alert("Jukeboxd's recommendation for you is:\n" + album + " by " + artist +"\n\nYour favourite genre is: " + bestGenre);
  window.location.href = "/";
}

function addAlbum()
{
  window.location.href = "addAlbum";
}

function viewReview(id)
{
  window.location.href = "viewReview/" + id;
}



function filterTable() {
  const filterValue = albumSearch.value.toLowerCase();
  const table = document.getElementById('albums-table');
  const rows = table.getElementsByTagName('tr');

  for (let i = 0; i < rows.length; i++) {
    const albumName = rows[i].getElementsByTagName('td')[0].textContent.toLowerCase();
    if (albumName.includes(filterValue)) {
      rows[i].style.display = '';
    } else {
      rows[i].style.display = 'none';
    }
  }


}

document.getElementById("album-search").addEventListener("input", function() {
  // Call a function to handle the search logic
  alert("not implemented yet");
});

// does not work
function searchAlbums(query) {
  var table = document.getElementById("albums-table");
  var rows = table.getElementsByTagName("td");
  var titles = rows.getElementById("album-title");
  alert(titles.length);

  // Loop through each row of the table
  for (var i = 0; i < rows.length; i++) {
    var row = rows[i];
    var albumTitle = row.getElementsByClassName("album-title")[0].innerHTML;
    alert(albumTitle);
   
    // Check if the album title matches the search query
    if (albumTitle.toLowerCase().includes(query.toLowerCase())) {
      // Show the row if it matches the search query
      row.style.display = "table-row";
    } else {
      // Hide the row if it doesn't match the search query
      row.style.display = "none";
    }
  }
}

function refresh()
{
  window.location.href = "/explore";
}