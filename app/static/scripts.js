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

function jukebox(title, artist)
{

  alert("Your jukebox suggestion is: " + title + " by " + artist + "!");
  
}