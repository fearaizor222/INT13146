document.getElementById('uploadForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const fileInput = document.getElementById('imageInput');
    const bppSelect = document.getElementById('bppSelect');
    const brightnessInput = document.getElementById('brightnessInput');
    const contrastInput = document.getElementById('contrastInput');
    const file = fileInput.files[0];
    const bpp = bppSelect.value;
    const brightness = brightnessInput.value;
    const contrast = contrastInput.value;

    if (file) {
        const formData = new FormData();
        formData.append('image', file);
        formData.append('bpp', bpp);
        formData.append('brightness', brightness);
        formData.append('contrast', contrast);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const img = document.createElement('img');
                    img.src = data.url;
                    const imageDisplay = document.getElementById('imageDisplay');
                    imageDisplay.innerHTML = '';
                    imageDisplay.appendChild(img);
                } else {
                    alert('Image upload failed');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
});