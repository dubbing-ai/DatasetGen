# Thai Language Datasets

This repository contains a Thai-English parallel dataset generation system and a reference Thai phoneme dataset (Tsync2).

## 1. Thai-English Parallel Dataset

### Overview

A generated dataset of Thai-English sentence pairs created using Large Language Models (LLMs). The generation process focuses on covering all Thai phonemes while maintaining natural conversational flow.

### Generation Tool

Located in `generator.ipynb`, the tool supports multiple LLMs:

- OpenAI GPT-4
- Anthropic Claude
- Ollama (local models)

### Generated Data

Located in `generated/` directory:

```plaintext
generated/
├── XX-YYY.csv        # From OpenAI O1
├── XX-YYY-claude.csv # From Anthropic Claude
└── combined/         # Combined and processed datasets
    ├── combined_sentences_no_filter.csv      # All generated data combined
    ├── combined_sentences.csv                # Combined data excluding sentences with "ๆ ฯ"
    └── combined_sentences_with_phoneme.csv   # With Thai and English phonemes
```

Where:

- XX: Sequential file number (01-99)
- YYY: Number of sentences in file
- Optional suffix indicates the model used

### Data Format

The generated CSV files contain two columns:

1. Thai sentence
2. English sentence translation

Example content:

```csv
"วันนี้อากาศดีมาก ฉันคิดว่าเราควรออกไปเดินเล่นที่สวนสาธารณะด้วยกันไหม","The weather is very nice today; do you think we should go for a walk in the park together?"
"แม้ว่าฝนจะตกหนัก แต่ฉันก็ยังต้องไปทำงานเพราะมีการประชุมสำคัญที่ต้องเข้าร่วม","Even though it's raining heavily, I still have to go to work because there's an important meeting I need to attend."
```

Format specifications:

- CSV format with quotation marks around both Thai and English text
- Each row contains one sentence pair
- Sentences are 5-10 seconds in spoken length

### Combined Datasets

Located in `generated/combined/`:

1. `combined_sentences_no_filter.csv`
   - Raw combination of all generated data
   - Includes all sentences without filtering

2. `combined_sentences.csv`
   - Filtered version excluding sentences containing "ๆ" and "ฯ"
   - These characters are excluded due to complexity in Thai pronunciation handling

3. `combined_sentences_with_phoneme.csv`
   - Based on filtered dataset
   - Includes generated phonemes for both Thai and English sentences
   - Four columns: Thai sentence, English sentence, Thai phonemes, English phonemes

### Transliterate Module

The [Transliterate](https://github.com/dubbing-ai/Transliterate) module is included as a Git submodule for phoneme generation:

- Converts Thai and English text to phoneme representations
- Handles complex Thai language rules
- Integrated directly into the repository

### Setup for Generation

1. Clone the repository with submodules:

   ```bash
   git clone --recursive https://github.com/dubbing-ai/DatasetGen
   ```

   Or if already cloned:

   ```bash
   git submodule update --init --recursive
   ```

2. Install required packages:

   ```bash
   pip install openai anthropic python-dotenv requests jupyter
   ```

3. Configure API keys in `.env`:

   ```plaintext
   OPENAI_API_KEY=your_openai_key
   ANTHROPIC_API_KEY=your_anthropic_key
   ```

4. For local models, ensure Ollama is running

### Generation Features

- 5-10 second spoken sentence length
- Natural conversational style
- Comprehensive phoneme coverage
- Parallel Thai-English translations
- Automatic file organization
- CSV output format
- Phoneme generation capability

## 2. Tsync2 Dataset

### Overview

A comprehensive collection of Thai sentences that serves two purposes:

1. **Current Use**: Reference dataset for validating phoneme coverage in our generated dataset
2. **Future Plan**: Source material for expanding the parallel dataset with verified phoneme coverage

### Structure

Located in `tsync2/wrd_ph/` directory:

```plaintext
tsync2/
└── wrd_ph/
    ├── tsync2_noon_0_*.txt
    ├── tsync2_noon_1_*.txt
    └── ...
```

### File Format

- Naming pattern: `tsync2_noon_GROUP_ID.txt`
  - GROUP: Phoneme group number (0-99)
  - ID: Unique identifier
- Some files have multiple parts (indicated by `_1.txt`, `_2.txt`, etc.)
- Contains Thai sentences with phoneme mappings

### Current Role

- Reference for checking phoneme coverage completeness
- Validation tool for generated dataset
- Guide for identifying missing phonemes

### Future Plans

- Translation of Tsync2 sentences to English
- Integration into the main parallel dataset
- Ensures comprehensive phoneme coverage
- Will serve as verified, high-quality additions to the dataset

## Repository Structure

```plaintext
.
├── generated/          # Generated Thai-English pairs
│   └── combined/       # Combined and processed datasets
├── tsync2/             # Reference dataset for validation and future expansion
│   └── wrd_ph/         # Word-phoneme mappings
├── Transliterate/      # Phoneme generation module (submodule)
├── generator.ipynb     # Generation tool
├── combine_and_phonemize.ipynb  # Dataset processing tool
└── README.md
```