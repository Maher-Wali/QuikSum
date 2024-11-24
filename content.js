document.addEventListener("selectionchange", () => {
    const selectedText = window.getSelection().toString().trim();
    if (selectedText) {
      // Store the selected text in chrome.storage
      chrome.storage.local.set({ selectedText });
    }
});