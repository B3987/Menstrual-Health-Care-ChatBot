
# HerCare: Menstrual Health Chatbot

**HerCare** is a menstrual healthcare assistant chatbot powered by AI. It offers users helpful and accurate responses to queries related to menstrual health through a text-based and optionally audio-enhanced interface.

---

## 💻 Features

- **ChatGPT Integration** using OpenAI API (or a local LLM like Mistral).
- **Streamlit Web App** UI with custom backgrounds.
- **Local Language Model Support** using `langchain` and `CTransformers`.
- **Audio Playback** for a multimedia experience.
- **Menstrual Health Focused Responses** only — filtered by system instructions.

---

## 🧾 File Descriptions

| File | Description |
|------|-------------|
| `app.py` | Core GPT chat logic with OpenAI API (local). CLI interface for interaction. |
| `app2.py` | Streamlit-based UI wrapper that uses the chat logic from `app.py` and a Mistral language model via `langchain` and `CTransformers`. |
| `audio_checkig.py` | Streamlit script to loop and play a local audio file (`mini.mp3`). |
| `dfg.py` | Streamlit UI with integrated chatbot, system prompt restrictions, background styling, and embedded audio. |

---

## 🧰 Requirements

Make sure to install the following packages:

```bash
pip install openai streamlit langchain ctransformers
```

---

## ⚙️ Setup & Usage

### 1. Run the Streamlit Interface

You can run the chatbot interface with either `app2.py` or `dfg.py` depending on your preference.

```bash
streamlit run app2.py
```

_or_

```bash
streamlit run dfg.py
```

> **Note:** Make sure the local LLM (`Mistral-7B-Instruct-v0.1`) is properly installed and accessible at the path specified in `app2.py`.

### 2. Run the CLI version

```bash
python app.py
```

You can chat with the assistant directly in your terminal. Type `exit`, `quit`, or `bye` to stop.

---

## 🧠 Model Configuration

- **Model Type**: `mistral` (used in both OpenAI-like API and CTransformers)
- **Custom Instructions**: Strictly limited to menstrual healthcare; avoids answering math, current affairs, or off-topic content.
- **Parameters** (in `CTransformers`):
  - `max_new_tokens`: 1024
  - `temperature`: 0.8
  - `top_p`: 0.95
  - `top_k`: 40
  - `repetition_penalty`: 1.1

---

## 🎨 UI Customization

- Backgrounds are set via inline CSS using Streamlit's `st.markdown`.
- You can change the image URL or local image path inside `dfg.py` and `app2.py` for different visual themes.

---

## 🔉 Audio Integration

- Audio file `mini.mp3` is played in a loop using `st.audio`.
- Ensure correct path to the audio file when running `audio_checkig.py` or `dfg.py`.

---

## 🛡️ Disclaimer

This chatbot is intended for **informational purposes only** regarding menstrual health. It is **not a substitute for professional medical advice**. Always consult a qualified healthcare provider for medical concerns.

---

## 📂 Project Structure

```
HerCare/
├── app.py
├── app2.py
├── dfg.py
├── audio_checkig.py
└── README.md
```
