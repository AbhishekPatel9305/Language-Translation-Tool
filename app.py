import streamlit as st
from googletrans import Translator
from gtts import gTTS
import os
import tempfile
from io import BytesIO
from playsound import playsound

# Initialize translator
translator = Translator()

# Streamlit UI
st.set_page_config(page_title="Language Translation Tool", layout="centered")
st.title("🌐 Language Translation Tool")

text = st.text_area("Enter text to translate:")
col1, col2 = st.columns(2)
with col1:
    src_lang = st.text_input("Source Language Code (e.g. 'en', 'fr')", "en")
with col2:
    target_lang = st.text_input("Target Language Code (e.g. 'es', 'hi')", "es")

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            translated = translator.translate(text, src=src_lang, dest=target_lang)
            st.subheader("Translated Text:")
            st.success(translated.text)

            # Text-to-speech option
            tts = gTTS(translated.text, lang=target_lang)
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts.save(temp_file.name)
            st.audio(temp_file.name, format="audio/mp3")

        except Exception as e:
            st.error(f"Translation failed: {e}")
