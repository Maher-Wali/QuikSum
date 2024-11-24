let summaryText = ""; // Variable to store the Python output

// Event listener for the "Play" button
document.getElementById("play-btn").addEventListener("click", () => {
  const userInput = document.getElementById("text-input").value;

  fetch("http://localhost:3000/run-python", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ input: userInput }) // Send input as JSON
  })
  .then(response => response.json())
  .then(data => {
    summaryText = data.result;
    alert(`Python Output: ${data.result}`);
  })
  .catch(error => console.error("Error:", error));
});

// Event listener for the "Copy Summary" button
document.getElementById("copy-btn").addEventListener("click", () => {
    console.log("Copying!");
    if (summaryText) {
    navigator.clipboard.writeText(summaryText).then(
      () => {
        alert("Summary copied to clipboard!");
      },
      (err) => {
        console.error("Failed to copy: ", err);
      }
    );
  } else {
    alert("No summary available to copy!");
  }
});

// Get the "Selected Text" button element
const selectedTextButton = document.getElementById("selected-btn");

// Check if there's stored selected text when the popup opens
chrome.storage.local.get("selectedText", (data) => {
  console.log("Retrieved selected text:", data.selectedText);
  const selectedText = data.selectedText || "";

  // Enable the button if there is selected text
  if (selectedText.length > 0) {
    selectedTextButton.disabled = false;

    // Handle button click
    selectedTextButton.addEventListener("click", () => {
      fetch("http://localhost:3000/run-python", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ input: selectedText }) // Send input as JSON
      })
      .then(response => response.json())
  .then(data => {
    summaryText = data.result;
    alert(`Python Output: ${data.result}`);
  })
  .catch(error => console.error("Error:", error));

      // You can also clear the selection from storage after use
      chrome.storage.local.remove("selectedText");
    });
  } else {
    selectedTextButton.disabled = true;
  }
});

// Update button dynamically if storage changes
chrome.storage.onChanged.addListener((changes, namespace) => {
  if (changes.selectedText) {
    const newValue = changes.selectedText.newValue || "";
    selectedTextButton.disabled = newValue.length === 0;
  }
});