const canvas = document.getElementById("canvas")
canvas.height = 280
canvas.width = 280

const context = canvas.getContext("2d")
context.lineWidth = 15
context.lineCap = 'round'

let prevX = null
let prevY = null
let draw = false

let clearBtn = document.querySelector(".clear")
clearBtn.addEventListener("click", () => {
    // Clearning the entire canvas
    context.clearRect(0, 0, canvas.width, canvas.height)
})

let predictBtn = document.querySelector(".predict")
predictBtn.addEventListener("click", () => {
    // Send canvas image to prediction model
    document.getElementById('canvasimg').value = canvas.toDataURL()
})

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

    let currentX = e.clientX
    let currentY = e.clientY

    context.beginPath()
    context.moveTo(prevX, prevY)
    context.lineTo(currentX, currentY)
    context.stroke()

    prevX = currentX
    prevY = currentY
})