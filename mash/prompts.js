// Info for making a random number display

const display = document.getElementById('display');
const startButton = document.getElementById('startButton');
const stopButton = document.getElementById('stopButton');
const lastNumberDisplay = document.getElementById('lastNumber');

let intervalId;
let lastNumber; // Variable to store the last generated number

function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function updateDisplay() {
    lastNumber = getRandomNumber(3, 10);
    display.textContent = lastNumber;
}

startButton.addEventListener('click', () => {
    updateDisplay();
    intervalId = setInterval(updateDisplay, 100); // Update every 1 second
    startButton.disabled = true;
    stopButton.disabled = false;
});

stopButton.addEventListener('click', () => {
    clearInterval(intervalId);
    startButton.disabled = false;
    stopButton.disabled = true;

    // Store the last number shown as a constant
    const finalNumber = lastNumber;
    lastNumberDisplay.textContent = `Your Magic Number: ${finalNumber}`;
});
    
// info for making a form
document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    // Capture form data for categories 1-4
    const category1 = document.getElementById('category1').value;
    const category2 = document.getElementById('category2').value;
    const category3 = document.getElementById('category3').value;
    const category4 = document.getElementById('category4').value;


    // Cature form data for options within each category
    const option1a = document.getElementById('option1a').value;
    const option1b = document.getElementById('option1b').value;
    const option1c = document.getElementById('option1c').value;
    const option1d = document.getElementById('option1d').value;

    const option2a = document.getElementById('option2a').value;
    const option2b = document.getElementById('option2b').value;
    const option2c = document.getElementById('option2c').value;
    const option2d = document.getElementById('option2d').value;

    const option3a = document.getElementById('option3a').value;
    const option3b = document.getElementById('option3b').value;
    const option3c = document.getElementById('option3c').value;
    const option3d = document.getElementById('option3d').value;

    const option4a = document.getElementById('option4a').value;
    const option4b = document.getElementById('option4b').value;
    const option4c = document.getElementById('option4c').value;
    const option4d = document.getElementById('option4d').value;


    // Create a JSON object
    const userData = {
        category1: [option1a, option1b, option1c, option1d]
        ,category2: [option2a, option2b, option2c, option2d]
        ,category3: [option3a, option3b, option3c, option3d]
        ,category4: [option4a, option4b, option4c, option4d]
    };

    
    // Convert JSON object to string for storage or transmission
    const jsonString = JSON.stringify(userData);

    // Display the JSON string on the webpage
    document.getElementById('output').innerText = jsonString;

    // (Optional) Log the JSON string to the console
    console.log(jsonString);

    
});
