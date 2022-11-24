const canvas = document.getElementById("canvas")

const context = canvas.getContext("2d")
// Start with black background
context.fillStyle = "black"
context.fillRect(0, 0, canvas.width, canvas.height)

let prevX = null
let prevY = null
let draw = false

// Cleans entire canvas
let clearBtn = document.querySelector("#clear")
clearBtn.addEventListener("click", () => {
    context.fillStyle = "black"
    context.fillRect(0, 0, canvas.width, canvas.height)
});

// Opens current canvas in new tab
let newTab = document.querySelector("#save")
newTab.addEventListener("click", () => {
    const dataUrl = canvas.toDataURL("png");
    console.log(dataUrl);
    window.open(dataUrl, '_blank');
});

// Posts canvas image to prediction model
const canvastoimage = () => {
    const canvas = document.querySelector("#canvas");
    document.getElementById("canvasimg").value = canvas.toDataURL();
};

// Set draw to true when mouse is pressed
window.addEventListener("mousedown", (e) => draw = true)
// Set draw to false when mouse is released
window.addEventListener("mouseup", (e) => draw = false)

window.addEventListener("mousemove", (e) => {
    // If draw is false then we won't draw
    if (prevX == null || prevY == null || !draw) {
        prevX = e.clientX
        prevY = e.clientY
        return
    }
    // If draw is true then draw
    context.fillStyle = "white"
    context.strokeStyle = "white"
    context.lineWidth = 15
    context.lineCap = "round"

    let currentX = e.clientX
    let currentY = e.clientY

    context.beginPath()
    context.moveTo(prevX, prevY)
    context.lineTo(currentX, currentY)
    context.stroke()

    prevX = currentX
    prevY = currentY
});