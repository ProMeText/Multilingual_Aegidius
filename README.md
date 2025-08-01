

<p align="left">   <img src="docs/images/logo-cropped.svg" alt="Corpus Overview" width="600"/> </p>


[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC--BY--NC--SA--4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Last Commit](https://img.shields.io/github/last-commit/ProMeText/Multilingual_Aegidius)](https://github.com/ProMeText/Multilingual_Aegidius/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/ProMeText/Multilingual_Aegidius)](https://github.com/ProMeText/Multilingual_Aegidius)
[![Issues](https://img.shields.io/github/issues/ProMeText/Multilingual_Aegidius)](https://github.com/ProMeText/Multilingual_Aegidius/issues)
# 📜 Multilingual Alignment and Collation of the *De Regimine Principum* in Latin, Vernacular, and English Traditions 🌍

**A corpus-based project for sentence segmentation, multilingual alignment, and philological analysis of medieval translations.**

This repository brings together historical linguistics, digital humanities, and natural language processing (NLP) to address a key challenge in premodern textual studies:  
> 🧠 *How can we systematically align, compare, and computationally analyze medieval prose across diverse linguistic, scribal, and editorial traditions?*

We provide open-access datasets and tools for:

- ✂️ **Sentence segmentation**
- 🌐 **Multilingual alignment**
- 🧩 **Textual collation and variant tracking**

### 🏰 *A Mirror for Princes Across Borders*  
**_De Regimine Principum_: Transmission and Translation**

Composed in Latin in the late 13th century, *De Regimine Principum* rapidly circulated throughout Europe and was translated into a range of vernaculars.  
This corpus offers a unique testbed for multilingual comparison, combining literary, political, and philosophical content.

---

## 📚 Research Background

This work on *De Regimine Principum* represents the second phase of a broader research initiative exploring **computational methods for multilingual medieval corpora**.

The first phase, detailed in the [Aquilign repository](https://github.com/ProMeText/Aquilign), focused on building a modular pipeline for **segmentation**, **alignment**, and **collation**.  
It was first applied to the *Lancelot en prose* corpus — a multilingual narrative tradition — to evaluate alignment accuracy across closely related Romance languages.

➡️ The resulting corpus and annotated alignments are published in the companion repository:  
[lancelot-par-maints-langages](https://github.com/carolisteia/lancelot-par-maints-langages)

The present project builds on this foundation and expands the methodology to *De Regimine Principum* and its **vernacular and English translations**, a corpus that introduces greater **generic**, **structural**, and **linguistic diversity**.

---

## 🎯 Project Goals

- Create historically informed, linguistically diverse **training data** for historical NLP
- Model **sentence segmentation** in medieval Romance and Latin languages
- Perform **multilingual alignment** of parallel textual traditions
- Enable **collation and variant tracking** across translated and original versions

---

## 🧪 Methodology

We combine philological insight with machine learning techniques:

- 🧭 **Collation workflow**: a reference collation table is built from Latin witnesses  
- 🌍 **Alignment**: vernacular versions are segmented and aligned using embedding-based tools  
- 🧮 **Variant detection**: semantic and structural divergences are analyzed using both manual and computational methods

---

## 📊 Preliminary Results

Preliminary alignments and exploratory visualizations are available via the dedicated project page:
➡️ [Multilingual Aegidius Project Page](https://prometext.github.io/Multilingual_Aegidius/)

---
## 💾 Data Overview

This section outlines how textual data was prepared and structured in the *Multilingual Aegidius* project.

## 🧩 Corpus Overview

The construction of the multilingual **corpus** involved several stages, combining both curated datasets and primary source texts. Each step in the pipeline is **modular**, **reproducible**, and designed for **extensibility**—enabling future applications across different authors, languages, or textual genres.

---

## 🧠 Training Datasets for Segmentation and Alignment

To support the development of robust segmentation and alignment models, the project relies on two complementary resources hosted in separate repositories:

- [`multilingual-segmentation-dataset`](https://github.com/carolisteia/multilingual-segmentation-dataset) 
  Annotated datasets for **sentence and phrase segmentation** in historical texts. Includes manually segmented examples across seven medieval languages (13th–16th c.), used to train and evaluate BERT-based segmenters for historical prose.

- [`parallelium-scriptures-alignment-dataset`](https://github.com/carolisteia/parallelium-scriptures-alignment-dataset)  
  A multilingual dataset of **aligned Biblical and Qur’anic texts**, combining medieval and modern versions in 9 languages. Designed for training alignment models, especially in historical and philological contexts.

These resources form the foundation for segmentation and alignment tasks within the **Aquilign pipeline**, used to process the *Aegidius* corpus.

---

## 📂 Core Aegidius Corpus

The [`data/aegidius`](https://github.com/ProMeText/Multilingual_Aegidius/tree/main/data/aegidius) directory contains the core multilingual **text corpus** for this project. It features versions of *De Regimine Principum* in several medieval languages, supporting research in:

- Historical linguistics  
- Machine translation  
- Philological analysis

### 📄 Contents:
- Parallel texts in Latin, French, English, and more  
- Sentence-level alignments for comparative study  
- Metadata for sources and editions

This **corpus** forms the foundation of the preliminary results presented in the [Results](#) section.


## 📦 Models

Pretrained models and evaluation outputs will be published here as they become available.

📌 Stay tuned for Hugging Face links and downloadable checkpoints in future releases.


## 🤝 Contributing to the Project

Contributions to the project are highly encouraged, whether they be additional data, bug fixes, or enhancements to the analysis scripts. To contribute:

1. **Fork the Repository** – Start by forking the repository and cloning it locally.  
2. **Create a Branch** – Make your changes in a new branch named after the feature or fix.  
3. **Submit a Pull Request** – After pushing your changes to your fork, open a pull request for discussion and review.

---
## 🔗 Related Projects

This repository is part of a broader ecosystem of tools and corpora developed for the study of medieval multilingual textual traditions:

- [Aquilign](https://github.com/ProMeText/Aquilign)  
  A clause-level multilingual alignment engine based on contextual embeddings (LaBSE), designed specifically for premodern texts.

- [Multilingual Segmentation Dataset](https://github.com/carolisteia/multilingual-segmentation-dataset)
  Source texts and segmented versions in multiple medieval Romance languages, as well as Latin and English, used for training and evaluating clause segmentation models.

- [Parallelium – an aligned scriptures dataset](https://github.com/carolisteia/parallelium-scriptures-alignment-dataset/tree/main)  
  A multilingual dataset of aligned Biblical and Qur’anic texts — spanning medieval and modern languages — designed for training and evaluating multilingual alignment models, especially in historical and philological contexts.

- [Lancelot par maints langages](https://github.com/carolisteia/lancelot-par-maints-langages)  
  A parallel corpus of translations of the *Lancelot en prose* in medieval French, Castilian, and Italian, segmented and aligned using the Aquilign pipeline.

----
## 🧾 Talks & Slides 

### 🎤 *Congrès International de Linguistique et de Philologie Romanes (CILPR 2025)*  
**_Premiers jalons de la collation multilingue du_ De regimine principum _latin et vernaculaire_**  
👥 *Matthias Gille Levenson, Lucence Ing, Carolina Macedo*  
📽️ [View presentation slides (PDF)](docs/slides_cilpr2025.pdf)


## 💰 Funding

This work benefited from national funding managed by the **Agence Nationale de la Recherche** under the *Investissements d'avenir* programme with the reference **ANR-21-ESRE-0005 (Biblissima+)**.

> Ce travail a bénéficié d'une aide de l’État gérée par l’**Agence Nationale de la Recherche** au titre du programme d’**Investissements d’avenir** portant la référence **ANR-21-ESRE-0005 (Biblissima+)**.


<p align="center">
  <img src="https://github.com/user-attachments/assets/915c871f-fbaa-45ea-8334-2bf3dde8252d" alt="Biblissima+ Logo" width="600"/>
</p>


## ⚖️ Licensing

This project is licensed under the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license.  
This license allows users to adapt, remix, and build upon the work non-commercially, as long as they credit the authors and license their new creations under the same terms.
