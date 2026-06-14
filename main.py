import streamlit as st
from deep_translator import GoogleTranslator

# Supported languages
LANGUAGES = {
    "english": ("English", "en"),
    "hindi": ("Hindi", "hi"),
    "kannada": ("Kannada", "kn"),
    "tamil": ("Tamil", "ta"),
    "telugu": ("Telugu", "te"),
    "malayalam": ("Malayalam", "ml"),
    "marathi": ("Marathi", "mr"),
    "bengali": ("Bengali", "bn"),
    "gujarati": ("Gujarati", "gu"),
    "punjabi": ("Punjabi", "pa"),
    "odia": ("Odia", "or"),
    "assamese": ("Assamese", "as"),
    "urdu": ("Urdu", "ur"),
    "sanskrit": ("Sanskrit", "sa"),
    "nepali": ("Nepali", "ne"),
    "sindhi": ("Sindhi", "sd"),
}

st.set_page_config(
    page_title="Basha Bridge",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 Basha Bridge")
st.subheader("Real-Time Indian Language Translator")

# Language Selection
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Source Language",
        list(LANGUAGES.keys()),
        index=0
    )

with col2:
    target_lang = st.selectbox(
        "Target Language",
        list(LANGUAGES.keys()),
        index=2
    )

# Text Input
text = st.text_area(
    "Enter Text",
    height=150,
    placeholder="Type your message here..."
)

def translate_text(text, source_lang, target_lang):
    src_code = LANGUAGES[source_lang][1]
    tgt_code = LANGUAGES[target_lang][1]

    if src_code == tgt_code:
        return text

    translator = GoogleTranslator(
        source=src_code,
        target=tgt_code
    )

    return translator.translate(text)

if st.button("Translate", use_container_width=True):
    if text.strip():
        with st.spinner("Translating..."):
            try:
                translated = translate_text(
                    text,
                    source_lang,
                    target_lang
                )

                st.success("Translation Completed")

                st.markdown("### Original Text")
                st.info(text)

                st.markdown("### Translated Text")
                st.success(translated)

            except Exception as e:
                st.error(f"Translation Failed: {e}")
    else:
        st.warning("Please enter some text.")

# Language List
with st.expander("Supported Languages"):
    for key, value in LANGUAGES.items():
        st.write(f"• {value[0]}")