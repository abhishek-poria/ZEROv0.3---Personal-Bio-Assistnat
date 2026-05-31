# 🧬 ZEROv0.3: Personal Bio Assistant

ZEROv0.3 is an interactive, browser-based bioinformatics application designed to streamline core molecular biology workflows. Built entirely in Python using **Streamlit** and **Biopython**, this web dashboard transitions genetic analysis away from rigid command-line environments into a clean, event-driven user interface.

This repository serves as a foundational prototype for building rapid, scalable automation tools in computational biology.

---

## 🚀 Key Modules & Capabilities

### 1. Advanced Genomics Sequence Utilities
* **DNA Sequence Length Calculator:** Instantly measures sequence lengths with built-in nucleobase error-handling.
* **DNA Slicing (Codon Fragmenter):** Formats raw sequences into structured, 3-letter codon reading frames via optimized list comprehensions.

### 2. Central Dogma Processing Pipeline
Simulates the core pathways of molecular biology with standalone modular verification checks:
* **Transcription:** Converts raw DNA strings into viable mRNA transcripts.
* **Translation:** Synthesizes mRNA sequences directly into active amino acid protein chains.
* **Reverse Transcription:** Re-engineers RNA molecules back into functional DNA.
* **Replication Matrix:** Generates perfect complementary DNA strands.

### 3. Quantitative Biomarker Calculators
* **GC Content Profiler:** Computes total GC percentage ratios to analyze thermal and structural stability.
* **Purine vs. Pyrimidine Metric Tracker:** Uses an isolated sidebar control panel to separate, identify, and measure custom nucleobase distributions across dynamic input thresholds.

---

## 🛠️ Built With

* **Core Language:** Python 3
* **Computational Biology Engine:** [Biopython](https://biopython.org/) — Structural biological data analysis.
* **User Interface Framework:** [Streamlit](https://streamlit.io/) — High-performance, low-code data web architectures.

---

## ⚙️ Installation & Deployment

To run this laboratory workspace locally on your machine, clone the repository and execute the following commands in your terminal:

```bash
# Install the necessary dependencies
pip install streamlit biopython

# Launch the interactive web server
streamlit run app.py
