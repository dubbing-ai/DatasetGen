# Thai Language Datasets

This repository contains a Thai-English parallel dataset generation system and a reference Thai phoneme dataset (Tsync2)

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
└── XX-YYY-claude.csv # From Anthropic Claude
```

Where:

- XX: Sequential file number (01-99)
- YYY: Number of sentences in file
- Optional suffix indicates the model used

### Setup for Generation

1. Install required packages:

   ```bash
   pip install openai anthropic python-dotenv requests jupyter
   ```

2. Configure API keys in `.env`:

   ```plaintext
   OPENAI_API_KEY=your_openai_key
   ANTHROPIC_API_KEY=your_anthropic_key
   ```

3. For local models, ensure Ollama is running

### Generation Features

- 5-10 second spoken sentence length
- Natural conversational style
- Comprehensive phoneme coverage
- Parallel Thai-English translations
- Automatic file organization
- CSV output format

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
├── tsync2/             # Reference dataset for validation and future expansion
│   └── wrd_ph/         # Word-phoneme mappings
├── generator.ipynb     # Generation tool
└── README.md
```
