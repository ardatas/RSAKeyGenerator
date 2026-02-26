document.addEventListener("DOMContentLoaded", () => {
  const generateButton = document.getElementById("generate-button");
  const resetButton = document.getElementById("reset-button");
  const publicKeyTextarea = document.getElementById("public-key");
  const privateKeyTextarea = document.getElementById("private-key");

  async function generateKeys() {
    try {
      generateButton.disabled = true;
      generateButton.textContent = "Generating keys (may take a moment)...";
      publicKeyTextarea.value = "Generating keys, please wait...";
      privateKeyTextarea.value = "";

      const response = await fetch("/api/generate");
      if (!response.ok) {
        throw new Error("Failed to generate keys");
      }

      const data = await response.json();
      const pub = data.public_key;
      const priv = data.private_key;

      publicKeyTextarea.value = `e: ${pub.e}\n\nn: ${pub.n}`;
      privateKeyTextarea.value = `d: ${priv.d}\n\nn: ${priv.n}`;
    } catch (error) {
      publicKeyTextarea.value = "Error generating keys.";
      privateKeyTextarea.value = String(error);
    } finally {
      generateButton.disabled = false;
      generateButton.textContent = "Generate keys";
    }
  }

  function resetKeys() {
    publicKeyTextarea.value = "";
    privateKeyTextarea.value = "";
  }

  generateButton.addEventListener("click", generateKeys);
  resetButton.addEventListener("click", resetKeys);
});
