const canvas = document.getElementById("canvas")
canvas.style.position = "relative"

const context = canvas.getContext("2d")

let prevX = null
let prevY = null
let draw = false

// Start with black background
context.fillStyle = "black"
context.fillRect(0, 0, canvas.width, canvas.height)

// Sets draw to true when mouse is pressed
window.addEventListener("mousedown", (e) => draw = true)

// Sets draw to false when mouse is released
window.addEventListener("mouseup", (e) => draw = false)

// Draws on canvas
window.addEventListener("mousemove", (e) => {
    // If draw is false then we won't draw
    if (prevX == null || prevY == null || !draw) {
        prevX = e.layerX
        prevY = e.layerY
        return
    }
    // If draw is true then draw
    context.fillStyle = "white"
    context.strokeStyle = "white"
    context.lineWidth = 25
    context.lineCap = "round"

    let currentX = e.layerX
    let currentY = e.layerY

    context.beginPath()
    context.moveTo(prevX, prevY)
    context.lineTo(currentX, currentY)
    context.stroke()

    prevX = currentX
    prevY = currentY
});

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
    document.getElementById("uri").value = canvas.toDataURL();
};