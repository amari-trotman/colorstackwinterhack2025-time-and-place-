const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const result = document.getElementById('result');
const details = document.getElementById('details');

// Start video stream
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {video.srcObject = stream; });

// Capture frame and send to server
function capture() {
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    canvas.toBlob((blob) => {
        const formData = new FormData();
        formData.append('frame', blob);
        formData.append('dressCode', document.getElementById('dressCode').value);
        formData.append('temperature', document.getElementById('temperature').value);

        fetch('/analyze', { method: 'POST', body: formData})
        .then(res => res.json())
        .then(res => {
            result.textContent = res.result;
            details.textContent = `Detected: ${res.predictedLabel} | Confidence: ${res.confidenceScore}`;
        });
    }, 'image/jpeg');
}

setInterval(capture, 1000); // 1 FPS