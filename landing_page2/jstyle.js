// Function to check if an element is in the viewport
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Function to handle the animation
function animateOnScroll() {
    const section = document.querySelector('section.intro');
    if (isInViewport(section)) {
        section.style.opacity = 1;
        window.removeEventListener('scroll', animateOnScroll);
    }
}

// Add a scroll event listener to trigger the animation
window.addEventListener('scroll', animateOnScroll);


// Function to check if an element is in the viewport
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.right >= 0 &&
        rect.left <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Function to handle the animation
function slideInOnScroll() {
    const slideElement = document.querySelector('div.intro');
    if (isInViewport(slideElement)) {
        slideElement.style.left = '0'; /* or slideElement.style.right = '0'; */
        slideElement.style.opacity = '1';
        window.removeEventListener('scroll', slideInOnScroll);
    }
}

// Add a scroll event listener to trigger the animation
window.addEventListener('scroll', slideInOnScroll);
