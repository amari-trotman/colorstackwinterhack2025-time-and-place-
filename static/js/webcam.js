const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const result = document.getElementById('result');
const details = document.getElementById('details');

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => video.srcObject = stream);

function capture() {
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    canvas.toBlob((blob) => {
        const formData = new FormData();
}