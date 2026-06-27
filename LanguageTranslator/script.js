const translateBtn = document.getElementById("translateBtn");
const copyBtn = document.getElementById("copyBtn");
const speakBtn = document.getElementById("speakBtn");
const swapBtn = document.getElementById("swapBtn");
translateBtn.addEventListener("click", async () => {
    const text = document.getElementById("inputText").value.trim();
    const source = document.getElementById("sourceLanguage").value;
    const target = document.getElementById("targetLanguage").value;
    if (text === "") {
        alert("Please enter some text.");
        return;
    }
    document.getElementById("outputText").value = "Translating...";
    try {
        const response = await fetch(
            `https://api.mymemory.translated.net/get?q=${encodeURIComponent(text)}&langpair=${source}|${target}`
        );
        const data = await response.json();
        document.getElementById("outputText").value = data.responseData.translatedText;
    } catch (error) {
        console.error(error);
        document.getElementById("outputText").value = "";
        alert("Translation failed.");
    }
});
copyBtn.addEventListener("click", () => {
    const output = document.getElementById("outputText");
    if (output.value === "") {
        alert("Nothing to copy!");
        return;
    }
    navigator.clipboard.writeText(output.value);
    alert("Copied Successfully!");
});
speakBtn.addEventListener("click", () => {
    const text = document.getElementById("outputText").value;
    if (text === "") {
        alert("Nothing to speak!");
        return;
    }
    const speech = new SpeechSynthesisUtterance(text);
    speech.lang = document.getElementById("targetLanguage").value;
    speechSynthesis.speak(speech);
});
swapBtn.addEventListener("click", () => {
    const source = document.getElementById("sourceLanguage");
    const target = document.getElementById("targetLanguage");
    let temp = source.value;
    source.value = target.value;
    target.value = temp;
});
