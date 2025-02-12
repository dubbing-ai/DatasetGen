# Thai Language Datasets

This repository contains a Thai-English parallel dataset generation system and a reference Thai phoneme dataset (Tsync2).

## 1. Thai-English Parallel Dataset

### Overview

A generated dataset of Thai-English sentence pairs created using Large Language Models (LLMs). The generation process focuses on covering all Thai phonemes while maintaining natural conversational flow.

### Generation Tool

Located in `generator.ipynb`, the tool supports multiple LLMs:

- OpenAI GPT-4 or O1
- Anthropic Claude
- Ollama (local models)
- Deepseek R1

### Generated Data

Located in `generated/` directory:

```plaintext
generated/
├── XX-YYY.csv        # From OpenAI O1
├── XX-YYY-claude.csv # From Anthropic Claude
└── processed/        # Processed and combined datasets
    ├── combined_sentences_no_filter.csv      # All generated data combined
    ├── combined_sentences.csv                # Combined data excluding sentences with "ๆ ฯ 0-9 a-z A-Z"
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

Located in `generated/processed/`:

1. `combined_sentences_no_filter.csv`
   - Raw combination of all generated data
   - Includes all sentences without filtering

2. `combined_sentences.csv`
   - Filtered version excluding sentences containing "ๆ", "ฯ", numbers, and English alphabet
   - These characters are excluded due to complexity in Thai pronunciation handling

3. `combined_sentences_with_phoneme.csv`
   - Based on filtered dataset
   - Includes generated phonemes for both Thai and English sentences
   - Four columns: Thai sentence, English sentence, Thai phonemes, English phonemes

### Reviewed Datasets

Located in `generated/reviewed/`, the reviewed datasets contain manually corrected sentences:

1. `combined_sentences_reviewed.csv`
   - First step of the review process based on `combined_sentences_no_filter.csv`
   - Rough review focusing on removing sentences that are:
     - Weird or inappropriate
     - Out of context
     - Not meaningful
   - No editing or modifications made - only removal of problematic sentences

2. `combined_sentences_revised.csv`
   - Second step of the review process based on `combined_sentences_reviewed.csv`
   - Enhanced review including:
     - Removal of similar sentences using cosine similarity
     - Manual grammar corrections
     - Manual translation corrections

### Sentence Similarity Analysis

Located in `sentence_sim_analysis/`, this component provides tools for analyzing semantic similarity between sentences:

1. `cosine_sim_gen.ipynb`
   - Generates sentence embeddings using BGE-M3 model
   - Creates histogram plots of similarity distribution
   - Helps identify duplicate or very similar sentences

2. `cosine_sim_search.ipynb`
   - Searches for similar sentences based on text and cosine similarity threshold
   - Outputs similar sentence pairs for manual review

The analysis uses the BGE-M3 model for generating sentence embeddings and calculates cosine similarity between them. This helps in:

- Identifying and removing duplicate content
- Finding semantically similar sentences
- Quality control of the dataset
- Ensuring diverse sentence coverage

### Transliterate Module

The [Transliterate](https://github.com/dubbing-ai/Transliterate) module is for phoneme generation:

- Converts Thai and English text to phoneme representations
- Handles complex Thai language rules

### Setup for Generation

1. Clone the repository:

   ```bash
   git clone https://github.com/dubbing-ai/DatasetGen
   ```

2. Install required packages:

   ```bash
   pip install openai anthropic python-dotenv requests jupyter
   pip install git+https://github.com/dubbing-ai/Transliterate.git
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

### Processing and Output Files

Located in `tsync2/processed/`, the processed dataset contains:

1. `combined_tsync2_thai_sentences.csv`
   - All Thai sentences from the Tsync2 dataset
   - Single-column format with "thai sentence" header
   - Contains 2,710 unique sentences
   - Maintains original sentence integrity

2. `combined_tsync2_thai_sentences_phoneme.csv`
   - Thai sentences with phoneme mappings
   - Two columns: "thai sentence" and "thai phoneme"
   - Phonemes are space-separated with '_' denoting word boundaries
   - Includes all sentences successfully converted to phonemes

### Processing

The dataset processing is handled by `tsync2.ipynb`, which performs:

- File combination from all Tsync2 text sources
- Thai text to phoneme conversion using the Transliterate module

### Structure

The Tsync2 dataset is organized as follows:

```plaintext
tsync2/
├── wrd_ph/                   # Raw word-phoneme mapping files
│   ├── tsync2_noon_0_*.txt
│   ├── tsync2_noon_1_*.txt
│   └── ...
└── processed/               # Combined and processed datasets
    ├── combined_tsync2_thai_sentences.csv         # All Thai sentences combined
    └── combined_tsync2_thai_sentences_phoneme.csv # Sentences with phoneme mappings
```

### File Formats

#### Input Files

- Raw files in `wrd_ph/` use Thai text with phoneme mappings
- Naming convention: `tsync2_noon_GROUP_ID.txt`
  - GROUP: Phoneme group number (0-99)
  - ID: Unique identifier
- Multi-part files indicated by `_1.txt`, `_2.txt` suffixes

#### Output Files

- CSV format with appropriate headers
- UTF-8 encoding for Thai character support

### Current Role

- Reference for checking phoneme coverage completeness
- Validation tool for generated dataset
- Guide for identifying missing phonemes

### Future Plans

- Translation of Tsync2 sentences to English
- Integration into the main parallel dataset
- Ensures comprehensive phoneme coverage
- Will serve as verified, high-quality additions to the dataset

## 3. Analysis Tools

### Overview

The repository includes analysis tools to examine and compare phoneme distributions between the generated dataset and Tsync2 reference dataset.

### Analysis Features

Located in `analysis`, the analysis tools provide:

- Uni-phoneme, bi-phoneme, tri-phoneme distribution visualization and comparison between datasets
- Identification of missing or unique phonemes
- Visual representation through comparative plots
- Validation of phoneme coverage completeness

#### Output Files

- `analysis/ThaiPhonemesDistribution.png` - Visual comparison of uni-phoneme distributions
- `analysis/ThaiBiPhonemesDistribution.png` - Visual comparison of bi-phoneme distributions
- `analysis/ThaiTriPhonemesDistribution.png` - Visual comparison of tri-phoneme distributions

#### Usage

The notebook compares phoneme distributions between:

- Generated dataset: `generated/processed/combined_sentences_with_phoneme.csv`
- Reference dataset: `tsync2/processed/combined_tsync2_thai_sentences_phoneme.csv`

The analysis helps validate phonemic coverage of the generated dataset against the reference Tsync2 corpus.

## Repository Structure

```plaintext
.
├── analysis/
│   └── analyse_corpus.ipynb     # Analysis and visualization tools
├── generated/                   # Generated Thai-English pairs
│   ├── processed/               # Processed and combined datasets
│   └── reviewed/                # Reviewed and corrected datasets
├── sentence_sim_analysis/       # Semantic similarity analysis tools
│   ├── cosine_sim_gen.ipynb     # Embedding generation and visualization
│   ├── cosine_sim_search.ipynb  # Similar sentence search tool
│   ├── encoder/                 # Encoder model for sentence embeddings
│   └── results/                 # Analysis results and plots
├── tsync2/                      # Reference dataset for validation and future expansion
│   ├── wrd_ph/                  # Raw word-phoneme mappings
│   └── processed/               # Processed and combined datasets
├── generator.ipynb              # Generation tool
├── combine_and_phonemize.ipynb  # Dataset processing tool
├── tsync2.ipynb                 # Tsync2 dataset processor
└── README.md
```
