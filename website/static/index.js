// document.querySelectorAll(".btn")[0].addEventListener("click", function (event) {
    
//     event.preventDefault();
// });
function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
}