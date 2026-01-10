const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const result = document.getElementById("result");
const details = document.getElementById("details");
const startBtn = document.getElementById("capture-btn");

let analyzing = false;

// Start webcam immediately
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => video.srcObject = stream)
  .catch(err => console.error("Webcam error:", err));

// Start analysis ONLY when button is clicked
startBtn.addEventListener("click", () => {
  const dressCode = document.getElementById("dress_code").value;
  const temperature = document.getElementById("temperature").value;

  if (!dressCode || !temperature) {
    result.textContent = "Please select dress code and temperature.";
    return;
  }

  analyzing = true;
  result.textContent = "Analyzing outfit...";
});

// Capture & analyze frame ONLY if analyzing = true
function capture() {
  if (!analyzing) return;

  const ctx = canvas.getContext("2d");
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

  canvas.toBlob(async blob => {
    const formData = new FormData();
    formData.append("frame", blob, "frame.jpg");
    formData.append("dress_code", document.getElementById("dress_code").value);
    formData.append("temperature", document.getElementById("temperature").value);

    try {
      const res = await fetch("/analyze/", {
        method: "POST",
        body: formData
      });

      const data = await res.json();

      result.textContent = data.result;
      details.textContent =
        `Detected: ${data.predicted_label} | Confidence: ${data.confidence}`;

    } catch (err) {
      console.error(err);
      result.textContent = "Error analyzing outfit";
    }
  }, "image/jpeg");
}

// Run loop, but gated
setInterval(capture, 1000);

