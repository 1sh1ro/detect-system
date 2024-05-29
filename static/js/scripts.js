 scripts.js

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const fileInput = document.getElementById('file');

    form.addEventListener('submit', function(event) {
        if (!fileInput.value) {
            event.preventDefault();
            alert('Please select a file to upload.');
        }
    });
});
