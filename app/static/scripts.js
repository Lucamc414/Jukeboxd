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

function jukebox(album, artist)
{
  alert("jukebox's recommendation for you is: " + album + " by " + artist);
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