# Language Translation Tool

A simple translation web application built with Streamlit that allows users to translate text between languages and listen to the translated output using text-to-speech.

## Overview

This project provides a lightweight interface for multilingual text conversion. Users can enter source text, choose source and target language codes, and generate a translated version along with audio playback.

## Features

- text translation between user-selected languages
- simple Streamlit-based interface
- translated text display
- text-to-speech audio output using gTTS

## Tech Stack

- Python
- Streamlit
- googletrans
- gTTS

## Main File

- `app.py` - Streamlit application for translation and audio playback

## How To Run

```bash
pip install streamlit googletrans==4.0.0-rc1 gtts
streamlit run app.py
```

## Usage

1. Enter the text to translate.
2. Provide the source language code, such as `en`.
3. Provide the target language code, such as `hi`, `fr`, or `es`.
4. Click `Translate` to generate the translated text and audio.

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
