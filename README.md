# Language Translation Tool

A Streamlit-based translation web application that allows users to translate text between languages and listen to the translated result using text-to-speech.

## Overview

This project provides a lightweight multilingual interface for text translation. Users can enter source text, provide source and target language codes, generate the translation, and play the translated output directly in the app.

## Features

- translate text between user-selected languages
- browser-based Streamlit interface
- translated text display with source-language detection
- in-app audio playback for translated text

## Tech Stack

- Python
- Streamlit
- googletrans
- gTTS

## Main File

- `app.py` - Streamlit application for translation and audio playback

## How To Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Usage

1. Enter the text to translate.
2. Provide the source language code, such as `en`.
3. Provide the target language code, such as `hi`, `fr`, or `es`.
4. Click `Translate` to view the translated text and play the generated audio.

## Learning Focus

This project demonstrates:

- API-backed language translation workflows
- rapid prototyping with Streamlit
- integrating text-to-speech into Python apps
- building simple user-facing AI utility tools

## Future Improvements

- replace free translation libraries with a more stable production API
- add language dropdowns instead of manual code entry
- improve validation and error handling
- support downloadable translated audio files
