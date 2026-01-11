const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const result = document.getElementById("result");
const details = document.getElementById("details");
const startBtn = document.getElementById("capture-btn");
const countdownEl = document.getElementById("countdown");
const stopBtn = document.getElementById("stop-btn");

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
  // Countdown from 3
  let count = 3;
  countdownEl.textContent = count;

  const timer = setInterval(() => {
    count--;
    countdownEl.textContent = count > 0 ? count : "";

    if (count === 0) {
      clearInterval(timer);
      analyzing = true;
      result.textContent = "Analyzing outfit...";
    }
  }, 1000);
});

// Stop analysis when stop button is clicked
stopBtn.addEventListener("click", () => {
  analyzing = false;
  result.textContent = "Analysis stopped.";
  result.className = "result"
  details.textContent = "";
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
      result.className = "result";

      if (data.result === "Appropriate") 
      {
        result.classList.add("appropriate");
      } 
      else if (data.result.includes("mismatch")) 
      {
        result.classList.add("warning");
      }
      else
      {
        result.classList.add("bad")
      }

      details.innerHTML = `
        <div>Detected style: <b>${data.predicted_label}</b></div>
        <div>Confidence: ${(data.confidence * 100).toFixed(1)}%</div>
        <div>Matched prompt: "${data.prompt}"</div>
      `;
      
    } catch (err) {
      console.error(err);
      result.textContent = "Error analyzing outfit";
    }
  }, "image/jpeg");
}

// Dress code button handling
document.querySelectorAll(".dress-buttons button").forEach(btn => {
    btn.addEventListener("click", () => {
        document.querySelectorAll(".dress-buttons button")
            .forEach(b => b.classList.remove("active"));

        btn.classList.add("active");
        document.getElementById("dress_code").value = btn.dataset.code;
    });
});

// Temperature slider handling
const tempSlider = document.getElementById("temperature");
const tempValue = document.getElementById("temp-value");

tempValue.textContent = `${tempSlider.value}°F`;

tempSlider.addEventListener("input", () => {
    tempValue.textContent = `${tempSlider.value}°F`;
});

// Reveal after intro
window.addEventListener("load", () => {
    setTimeout(() => {
        document.getElementById("intro").classList.add("fade-out");
        document.querySelector(".app").classList.remove("hidden");
    }, 2500); // total intro duration
});

// Run loop, but gated
setInterval(capture, 1000);

