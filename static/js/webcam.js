const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const result = document.getElementById('result');
const details = document.getElementById('details');

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => video.srcObject = stream);