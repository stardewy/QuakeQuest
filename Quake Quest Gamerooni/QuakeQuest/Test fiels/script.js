// Linear story sequence as an array
const storySequence = [
    "Home sweet home.",
    "It’s been a week since my grandparents asked me to house-sit. It’s closer to my college, so I gladly took up the offer. The area is safe, and conveniently, there’s a church nearby.",
    "It also cuts down the cost, since lolo* also allowed me to use his study whenever I do my schoolwork. No need to commute to the library. On that note, maybe I should clean up there a bit after my all-nighter.",
    "There’s something I’m curious about, though…why is the door to the basement locked? And hidden behind a curtain?",
    "Is there some secret that lolo’s hiding?",
    "I know I shouldn’t snoop around. But what can I say? The curious nature of a scientist runs in my genes.",
    "Let me see if I can find the <bold>key</bold>. I’m sorry, lolo!",
    "PAUSE: You move to the Study....",
];

let currentPartIndex = 0;  // Start the story from the first part

// Function to display the current story part
function displayStoryPart() {
    const storyElement = document.getElementById('story');
    const currentStoryPart = storySequence[currentPartIndex];
    
    // Display the current part of the story
    storyElement.innerHTML = currentStoryPart;

    // If we reach the last part of the story, change the style
    if (currentPartIndex === storySequence.length - 1) {
        storyElement.classList.add('end');
    }
}

// Function to handle the click and move to the next story part
function handleClick() {
    if (!paused && currentPartIndex < storySequence.length - 1) {
        currentPartIndex++;  // Move to the next part
        displayStory();  // Refresh the story display with the new part
    }
}

// Set up the click event listener on the story div
document.getElementById('story').addEventListener('click', handleClick);

// Display the initial part of the story when the page loads
displayStory();
