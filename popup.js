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
