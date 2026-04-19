from io import BytesIO

import streamlit as st
from googletrans import Translator
from gtts import gTTS


translator = Translator()


def build_audio_bytes(text: str, language_code: str) -> bytes:
    audio_buffer = BytesIO()
    gTTS(text=text, lang=language_code).write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer.read()


st.set_page_config(page_title="Language Translation Tool", layout="centered")
st.title("Language Translation Tool")
st.caption("Translate text between languages and listen to the translated output.")

text = st.text_area("Enter text to translate", height=180)
col1, col2 = st.columns(2)
with col1:
    src_lang = st.text_input(
        "Source language code",
        value="en",
        help="Example: en, hi, fr, es",
    ).strip().lower()
with col2:
    target_lang = st.text_input(
        "Target language code",
        value="es",
        help="Example: en, hi, fr, es",
    ).strip().lower()

if st.button("Translate", use_container_width=True):
    if not text.strip():
        st.warning("Please enter some text to translate.")
    elif not src_lang or not target_lang:
        st.warning("Please provide both source and target language codes.")
    else:
        try:
            translated = translator.translate(text, src=src_lang, dest=target_lang)
            st.subheader("Translated Text")
            st.success(translated.text)
            st.caption(
                f"Detected source: {translated.src} | Target language: {target_lang}"
            )

            audio_bytes = build_audio_bytes(translated.text, target_lang)
            st.audio(audio_bytes, format="audio/mp3")
        except Exception as exc:
            st.error(f"Translation failed: {exc}")
