import streamlit as st
from Bio.Seq import Seq
import matplotlib.pyplot as plt
from collections import Counter
import base64

st.set_page_config(page_title="DNA Analyzer", layout="centered")
st.title("🧬 DNA Sequence Analyzer")

# Base64 encoded DNA helix image (small PNG)
dna_image_base64 = """
iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAB+S61WAAAABlBMVEUAAAD///+l2Z/dAAAArklEQVR4nO3BAQ0AAAwCoNm/9HI83GBA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAQQlYABXFrZ0EAAAAASUVORK5CYII=
"""

# Decode and display the image
st.image(base64.b64decode(dna_image_base64), caption="DNA Double Helix", use_column_width=True)

st.subheader("Enter a DNA Sequence (A, T, C, G):")
user_input = st.text_area("Paste or type the DNA sequence here:", height=150)

def clean_sequence(seq):
    return ''.join(filter(lambda x: x in "ATCGatcg", seq.upper()))

if user_input:
    seq = clean_sequence(user_input)
    dna_seq = Seq(seq)

    st.markdown("### ✅ Basic Analysis:")
    st.write(f"Length: {len(dna_seq)} bases")
    st.write(f"GC Content: {100 * (seq.count('G') + seq.count('C')) / len(seq):.2f}%")
    
    st.markdown("### 🔁 Reverse Complement:")
    st.code(str(dna_seq.reverse_complement()))

    st.markdown("### 🧬 Transcription (DNA → mRNA):")
    st.code(str(dna_seq.transcribe()))

    st.markdown("### 🧫 Translation (mRNA → Protein):")
    st.code(str(dna_seq.translate(to_stop=True)))

    st.markdown("### 📊 Nucleotide Frequency:")

    freq = Counter(seq)
    labels = list(freq.keys())
    values = list(freq.values())

    fig, ax = plt.subplots()
    ax.bar(labels, values, color=["#4CAF50", "#2196F3", "#FFC107", "#F44336"])
    ax.set_ylabel("Count")
    ax.set_title("Nucleotide Count")
    st.pyplot(fig)

else:
    st.info("Enter a DNA sequence to start analysis.")
