# 📘 Multilingual Alignment Corpus for Historical Texts


*Curated verse-aligned dataset to support multilingual NLP and historical-text alignment modeling.*


> A multilingual corpus of aligned biblical and Qur’anic texts, primarily in medieval languages. Select modern editions are included to enhance diversity and robustness. Designed to support the training and evaluation of sentence alignment models for historical, philological, and comparative-linguistic use cases.


---


## 📂 Project Scope

This dataset provides training data for multilingual alignment models. It includes over **48,000 aligned verses** and over **4 million verse-level pairs**, covering **29 versions** in **9 languages**. The corpus spans both **medieval** and **modern** textual traditions.

It is intended as an **open, extensible training resource** for multilingual NLP, not a fixed benchmark. Future releases may add sources or metadata.

> 📌 Each aligned verse includes two or more versions. Pair counts reflect all *N choose 2* language pairs per verse.

---
## 🌟 Goals and Audience

<!-- The primary goal of this alignment corpus is to support the development and evaluation of multilingual alignment models tailored to historical texts.

Unlike standard parallel corpora, this dataset addresses specific challenges such as:

- Structural divergence across religious and textual traditions
- Free or flexible word order in premodern languages
- Non-standardized orthography and editorial conventions
- Gaps, mismatches, and overlaps in verse numbering

By providing aligned data across a diverse set of languages and time periods, the corpus aims to:

- Enable **robust training of sentence alignment systems** for historical and philological contexts
- Support research on translation shifts and **textual transmission in multilingual traditions**
- Offer a flexible and extensible foundation for further corpus-building or annotation efforts -->

This dataset aims to support the development and evaluation of multilingual alignment models tailored to **historical texts**, a niche often underserved by modern NLP resources.

Unlike standard parallel corpora, this dataset addresses challenges specific to historical-language contexts, such as:

- Structural divergence across traditions and textual lineages  
- Flexible or free word order in premodern languages  
- Non-standardized orthographies and inconsistent editorial practices  
- Gaps, mismatches, and overlap in verse segmentation across versions  

By providing aligned data across a diverse set of languages and time periods, the corpus aims to:

- Enable **robust training of sentence alignment systems** for historical and philological contexts
- Support research on translation shifts and **textual transmission in multilingual traditions**
- Offer a flexible and extensible foundation for further corpus-building or annotation efforts 

### 🎯 This corpus is designed for:
- NLP researchers working on low-resource or historical alignment tasks
- Digital humanists studying translation or textual variants 
- Scholars exploring textual transmission across religious or linguistic traditions

---

## 📊 Dataset Overview

| Feature            | 📖 Biblia Corpus                                                                                   | 🕋 Qur’anic Corpus                                                                 |
|--------------------|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| **Text Types**     | Biblical texts (medieval + modern editions)                                                       | Qur’anic translations across historical European languages and Arabic             |
| **Languages**      | Latin, French, English, Castilian, Catalan, Italian, Portuguese, Greek                            | Arabic, Latin, English, French, Italian                                           |
| **Alignment Unit** | Verse-level (sentence or clause approximation)                                                    | Verse-level (surah:ayah)                                                          |
| **Format**         | JSON                                                                                              | JSON                                                                              |
| **Use Case**       | Training multilingual alignment models (not for scholarly textual criticism)                      | Training multilingual alignment models (not for religious or exegetical purposes) |
| **Aligned Verses** | 42,562 verses                                                                                     | 6,236 verses                                                                      |
| **Aligned Pairs**  | 3,927,811 pairs                                                                                   | 114,226 pairs                                                                     |

---

## 🔍 Challenges

### 🧩 Source Heterogeneity

- Modern Bibles are abundant online, but medieval ones are rare, sometimes only available in printed editions or inaccessible formats.
- Encoding inconsistencies and varying editorial norms require extensive normalization.


### ⚖️ Traditions and Variant Structures

- Medieval texts stem from diverse religious traditions, requiring textual literacy to align them responsibly.
- Canonical order and verse mapping varies across traditions (e.g. *Esther* in LXX, *Baruch 6* = *Epistle of Jeremiah*).

---

## 🤔 Alignment Principles

- **Anchor Text**: The Latin Vulgate serves as the primary reference text for alignment. When the Vulgate is unavailable for a given verse, other available language pairs are still retained.

- **Minimum Pairing Requirement**: A verse or book is included only if at least one pair of aligned texts is available. Segments represented in only one tradition (e.g., found solely in the LXX) are excluded, as the corpus focuses on comparative alignment.

- **Exclusions for Structural Complexity**: Some books were excluded due to significant challenges in verse mapping across traditions. For instance, the Septuagint version of *Esther* could potentially be aligned (at least in part), but would require significantly more time and manual effort.

---

## 🛠️ Use and Limitations

⚠️ This dataset is intended **exclusively for training and evaluation purposes**.

It does **not preserve canonical verse numbering**, and therefore it is **not suitable** for scholarly edition, canonical citation, or textual-critical research.

### 📌 Examples of structural divergence:

- *Epistle of Jeremiah* appears as **Baruch 6** in some traditions.
- *Susanna* is integrated as **Daniel 11**, and *Bel and the Dragon* as **Daniel 13**, depending on the version.

---

# 📂 Data Sources

The Biblical and Qur’anic texts were selected for their **structural compatibility** — namely, their verse-based (or surah:ayah in the case of the Qur’an) organization — and their widespread **cross-linguistic transmission**, which enables meaningful alignment across centuries and traditions.


### 🕰️ Medieval Bibles

| Language | Text                        | Source                                                                                                                                                                           | Format        |
|----------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| en       | John Wycliffe Bible         | [GitHub](https://github.com/saibotsivad/john-wycliffes-bible/tree/master/raw-text)                                                                                              | `.txt`        |
| en       | Coverdale Bible             | [GitHub](https://github.com/Isidore-Guild/coverdale)                                                                                                                             | `.xml`        |
| en       | Great Bible                 | [EDGeS Corpus](https://spraakbanken.gu.se/en/resources/openedges)                                                                                                                | `.tsv`        |
| it       | Gospel of St. Matthew       | [SISMEL Edition](https://www.sismel.it/pubblicazioni/2059-il-vangelo-secondo-matteo-in-volgare-italiano-studio-ed-edizione-critica-delle-due-versioni-non-glossate)            | `.pdf`        |
| fr       | La Bible historiale         | [Project site](https://www.biblehistoriale.fr/index.php/xml-tei/)                                                                                                                | `.xml`        |
| fr       | Esther, Judith, Ruth        | Claudio Lagomarsini (unpublished)                                                                                                                                                | Word\*        |
| fr       | Gospel of Matthew           | Seth Middleton Transcription                                                                                                                                                | `.txt`\*      |
| gr       | Septuagint (LXX)            | [Corpus Corporum](https://mlat.uzh.ch/browser?path=/17098/17099/17113/17110/17104)                                                                                               | `.xml`        |
| es       | Three Medieval Bibles       | [Proyecto Biblia Medieval](https://bibliamedieval.es/recursos/textos)                                                                                                            | `.txt`        |
| ca       | Three Medieval Bibles       | Pere Casanellas [(Corpus Biblicum Catalanicum)](https://cbcat.abcat.cat/)                                                                                                       | `.xml`, Word\*|
| la       | Vulgata Sixto-Clementina    | [GitLab](https://gitlab.com/crosswire-bible-society/vulgate/-/blob/master/vulgate.osis.xml?ref_type=heads)                                                                      | `.xml`        |

> \* *These texts are not publicly shareable due to copyright restrictions.*

---

### 📅 Modern Editions

Nine Bibles in French, English, Portuguese, Greek, and Spanish from [this repository](https://github.com/thiagobodruk/bible), used to augment language diversity.

---

### 🕋 Qur’an

Multilingual alignment compiled by **Mouhamadoul-Khaly Wélé**, spanning 7 languages (Arabic, Latin, English, French, Italian, etc.).  
*Note: This resource is not publicly redistributable.*

---
# 🧱 Data Structure

### 📘 Monolingual JSON
Each monolingual file is a **JSON dictionary** where each key is a book name, and each value is a list of verse objects ({`ref`, `text`})
```json
{
  "malachias": [
    {
      "ref": "1:1",
      "text": "Carga dela palabra del sennor a israel en mano de malechias:"
    }
  ]
}
```
### 🌍 Multilingual JSON

The multilingual aligned file is a **JSON list of dictionaries**, where each entry represents a verse with a `book`, a `ref`, and a `data` dictionary mapping version IDs to their corresponding translations (or `null` if missing).


```json
[
  {
    "book": "genesis",
    "ref": "1:2",
    "data": {
      "la_vulgate": "terra autem erat inanis...",
      "gr_lxx": "ἡ δὲ γῆ ἦν ἀόρατος...",
      "en_coverdale": "...",
      "fr_historiale": "...",
      "it_beta": null
    }
  }
]
```


### 📘 Structure Summary

| Format               | Structure                            | Scope               | Use Case                     |
|----------------------|---------------------------------------|----------------------|------------------------------|
| **Monolingual JSON** | `{ book: [ {ref, text} ] }`          | One language         | Intermediate/raw input       |
| **Multilingual JSON**| `[ {book, ref, data} ]`              | Aligned versions     | Final aligned corpus         |

**Field Definitions:**

- `book`: Book name (in lowercase)  
- `ref`: Canonical verse reference in `chapter:verse` format  
- `data`: Dictionary mapping version IDs to verse text (or `null` if missing)

---

## ⚙️ Alignment Workflow (Biblical Corpus)

`Import ➝ Structure ➝ Filter ➝ Align (to Vulgate) ➝ Export`

![Alignment Workflow](alignment_workflow_diagram.png)



This corpus was prepared through a multi-stage alignment pipeline, designed to handle heterogeneous formats and historical variation.

### **Steps:**

1. **Collection**  
   - Source formats include XML, TXT, PDF, Word, and TSV  
   - Texts were selected for having existing verse-based divisions  
   - No orthographic normalization was performed — original spellings are preserved

2. **Cleaning**  
   - Removal of non-textual artifacts, markup noise, and encoding issues  
   - TEI/XML files were simplified or minimally processed for structure

3. **Structuring**  
   - Conversion into a unified JSON schema  
   - Monolingual JSON files prepared per text, then merged into multilingual alignment files  
   - Metadata added for book names, references, and version IDs

4. **Alignment**  
   - Verse-level alignment centered on the Latin Vulgate when available  
   - Where the Vulgate lacked a verse, alignment was constructed from available pairs  
   - Only verse units with at least one valid cross-language pair were retained

5. **Export**  
   - Final outputs include monolingual and multilingual JSON files  
   - Missing verses are represented with `null` values for transparency  

---

## 📈 Dataset Statistics

### 📖 Biblia Corpus

![Verse counts per language (Biblical)](json/verse_counts_by_language_biblical.png)

**Multilingual** — — **3,927,811 pairs across 42,562 aligned verses**

> 📌 The number of aligned pairs refers to verse-level combinations between two or more languages.  
> Each verse aligned between *N* languages generates *N choose 2* pairings.

### 🕋 Qur’anic Corpus

![Verse counts per language (Qur'an)](json/verse_counts_by_language_quran.png)

**Multilingual (Qur’an)** — — **114,226 pairs across 6,236 aligned verses**

> 📌 The number of aligned pairs refers to verse-level combinations between two or more languages.  
> Each verse aligned between *N* languages generates *N choose 2* pairings.


## 📊 Dataset basic stats
###  Verse Counts by Version
> 📌 A "version" corresponds to a specific translation or manuscript tradition in a given language.


| Version ID        | Language     | Verses |
|-------------------|--------------|--------|
| gr_modern_greek   | Greek        | 31,060 |
| la_vulgate        | Latin        | 38,843 |
| fr_lsegond        | French       | 31,102 |
| fr_bible13        | French       |   702  |
| pt_almeida        | Portuguese   | 31,106 |
| es_arragel        | Castilian    | 22,652 |
| es_e6e8           | Castilian    | 31,247 |
| en_wycliffe       | English      | 36,248 |
| ca_peiresc        | Catalan      | 17,245 |
| en_bbe            | English      | 31,063 |
| en_coverdale      | English      | 31,086 |
| en_kjv            | English      | 31,059 |
| es_reina          | Castilian    | 31,065 |
| fr_jerusalem      | French       | 31,207 |
| it_alpha          | Italian      |  1,070 |
| fr_historiale     | French       |  2,241 |
| es_e3             | Castilian    | 24,515 |
| it_beta           | Italian      |  1,070 |
| gr_lxx            | Greek        | 27,616 |
| fr_perret         | French       | 31,102 |
| fr_epee           | French       | 30,933 |
| en_great          | English      | 31,108 |

**Multilingual** — — **3,927,811 pairs across 42,562 aligned verses**

> 📌 The number of aligned pairs refers to verse-level combinations between two or more languages.  
> Each verse aligned between *N* languages generates *N choose 2* pairings.



### 📊 Distribution by Language

The following plot summarizes the **total number of verses grouped by language**, aggregating across all available versions:

[Verse counts per language](/home/carolisteia/Desktop/Biblissima/biblia/alignment/data/json_global/analysis/json/verses_cout_by_language.png) <!-- !CHANGE PATH -->

> 📌 This visualization complements the per-version table by offering a clearer view of data coverage **per language**, helping identify underrepresented areas or strong alignments.

### 🕋 Qur’anic Data

A multilingual alignment of the Qur’an (6,236 verses) was also used in model training. It includes **7 languages**, such as Arabic, English, French, Latin, and Italian. However, this data is **not included in the public release** due to redistribution restrictions.

> Qur’anic verses are structurally consistent and verse-aligned by design, contributing valuable contrast to biblical sources in the training setup.


## 🔍 Alignment Preview (Biblical Corpus)

The snippet below illustrates how to explore aligned verse pairs in the JSON file.  
Each verse contains a `book`, `ref`, and a `data` dictionary mapping version IDs to verse translations.

```python
import json

with open("aligned_data.json") as f:
    data = json.load(f)

# Display all aligned French–Portuguese verse pairs from Genesis
# 💡 Change language IDs below based on your alignment interest
for verse in data:
    if verse["book"] == "genesis":
        fr = verse["data"].get("fr_lsegond")
        pt = verse["data"].get("pt_almeida")
        if fr and pt:
            print(f'{verse["ref"]}:\nFR: {fr}\nPT: {pt}\n')
```
Note: aligned_data.json is not distributed due to licensing.
Use this example to preview the data format and structure.

---


### 🔮 Future Directions

This corpus is an initial foundation intended to grow. Several improvements are planned to enhance its usability, accuracy, and scholarly value:

- Prioritize the **collection and structuring of additional medieval texts**, especially from **Romance-language traditions**, to rebalance the dataset—currently skewed toward modern sources—and progressively specialize it for historical modeling. This will improve alignment robustness for premodern domains and enable the training of models tailored to medieval textual data.

- **Incorporate OCR/HTR of manuscript texts**  
  Leveraging Optical Character Recognition (OCR) and Handwritten Text Recognition (HTR) will allow the inclusion of otherwise inaccessible sources, especially for underrepresented medieval texts not available in digital editions.

- **Annotate editorial provenance and textual lineage**  
  Metadata will be enriched to reflect the textual origin (e.g., manuscript family, editor, edition), enabling philological and stemmatic analysis across traditions.

- **Develop a queryable interface or API**  
  To support broader reuse and exploration, a lightweight web interface or API is under consideration, allowing users to browse and extract aligned verses across versions and languages.

### 🗂️ Versioning

- **Current version**: `v0.1`  
- **Next planned update**: Continued cleaning and integration of additional medieval texts already sourced — targeted for **Q4 2025**


### 📜 License

Corpus annotations and alignment metadata are distributed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/), unless otherwise noted. Some source texts are not redistributable due to third-party copyright restrictions.
