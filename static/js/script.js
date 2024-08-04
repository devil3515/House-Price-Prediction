// Get the modal
var modal = document.getElementById("myModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// Get the form and the modal close button
var form = document.getElementById("predictionForm");
var modalCloseBtn = document.getElementById("modalCloseBtn");

// When the user clicks on <span> (x), close the modal and reset the form
span.onclick = function() {
    modal.style.display = "none";
    form.reset();
}

// When the user clicks the modal close button, close the modal and reset the form
modalCloseBtn.onclick = function() {
    modal.style.display = "none";
    form.reset();
}

// When the user clicks anywhere outside of the modal, close it and reset the form
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
        form.reset();
    }
}

// Show the modal if there is a prediction value
document.addEventListener("DOMContentLoaded", function() {
    var predictionValue = document.getElementById("predictionValue").textContent;
    if (predictionValue) {
        modal.style.display = "block";
    }
});
