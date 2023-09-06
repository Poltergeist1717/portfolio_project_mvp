 // JavaScript for Scroll-to-Top Button
const scrollToTopButton = document.getElementById('scroll-to-top');

// Function to scroll to the top of the page
function scrollToTop() {window.scrollTo({ top: 0, behavior: 'smooth' });}

// Add click event listener to the button
scrollToTopButton.addEventListener('click', scrollToTop);

// active hamburger menu 
let menuIcon = document.querySelector(".menu-icon");
let navlist = document.querySelector(".navlist")
menuIcon.addEventListener("click",()=>{
    menuIcon.classList.toggle("active");
    navlist.classList.toggle("active");
    document.body.classList.toggle("open");
});


// Get references to the div and button
const longDiv = document.querySelector('.long-div');
const readMoreButton = document.querySelector('.read-more-button');

// Add a click event listener to the button
readMoreButton.addEventListener('click', function () {
    if (longDiv.style.maxHeight) {
        longDiv.style.maxHeight = null;
        readMoreButton.textContent = 'Read More';
    } else {
        longDiv.style.maxHeight = longDiv.scrollHeight + 'px';
        readMoreButton.textContent = 'Read Less';
    }
});


const longText = [
    "Effortless candidate access, save time, and expand your talent pool with ease.",
    "Swift, efficient hiring, so you focus on building your dream team.",
    "Robust data security ensures your information is always safe and protected.",
    "User-friendly interface for easy profile creation and seamless login.",
    "Structured user management simplifies admin tasks and user interactions.",
    "Efficient interview assessments offer vital insights for better evaluations.",
    "Customize the app to fit your specific needs, no matter your business size.",
    "Integrated features for efficient, data-driven decision-making.",
    "Optimize interviews, save time, and boost productivity in your hiring process.",
    "Revolutionize hiring with the easiest way to access top-notch candidates. Start today!.",
    // Add more lines as needed
];

const delay = 50; // Delay between each character in milliseconds
const typewriterText = document.getElementById("typewriter-text");

function typeWriter(lineIndex, charIndex) {
    if (lineIndex < longText.length) {
        const line = longText[lineIndex];
        if (charIndex < line.length) {
            typewriterText.style.color = "white"
            typewriterText.innerHTML += line.charAt(charIndex);
            charIndex++;
            setTimeout(() => {
                typeWriter(lineIndex, charIndex);
            }, delay);
        } else {
            // Move to the next line
            lineIndex++;
            charIndex = 0;
            setTimeout(() => {
                typewriterText.innerHTML += "<br>"; // Add a line break
                typeWriter(lineIndex, charIndex);
            }, 80); // Pause for 80 miliseconds before starting the next line
        }
    } else {
        // Clear the screen and restart the animation
        setTimeout(() => {
            typewriterText.innerHTML = "";
            typeWriter(0, 0); // Start from the beginning
        }, 1000); // Pause for 1 seconds before restarting
    }
}

let i = 0; // Initialize line index
let j = 0; // Initialize character index
typeWriter(i, j);









// // Get references to the paragraph and button
// const paragraph = document.querySelector('.long-paragraph');
// const readMoreButton = document.querySelector('.read-more-button');

// // Add a click event listener to the button
// readMoreButton.addEventListener('click', function () {
//     if (paragraph.style.maxHeight) {
//         paragraph.style.maxHeight = null;
//         readMoreButton.textContent = 'Read More';
//     } else {
//         paragraph.style.maxHeight = paragraph.scrollHeight + 'px';
//         readMoreButton.textContent = 'Read Less';
//     }
// });

// const text = "We are expecting you to join us.";
// const delay = 50; // Delay between each character in milliseconds
// const typewriterText = document.getElementById("typewriter-text");

// function typeWriter() {
//     if (i < text.length) {
//         typewriterText.innerHTML += text.charAt(i);
//         i++;
//         setTimeout(typeWriter, delay);
//     }
//     // Optionally, reset the animation after finishing
//     else {
//         setTimeout(() => {
//             typewriterText.innerHTML = "";
//             i = 0;
//             typeWriter();
//         }, 2000); // Pause for 2 seconds before restarting
//     }
// }

// let i = 0;
// typeWriter();
