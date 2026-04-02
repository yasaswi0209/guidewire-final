function VoiceInput({ setWeather }) {
  function startVoice() {
    const recognition = new window.webkitSpeechRecognition();
    recognition.start();

    recognition.onresult = (event) => {
      const text = event.results[0][0].transcript.toLowerCase();

      if (text.includes("rain")) setWeather("rain");
      if (text.includes("heat")) setWeather("heat");
    };
  }

  return (
    <button onClick={startVoice}>
      🎤 Speak Condition
    </button>
  );
}

export default VoiceInput;