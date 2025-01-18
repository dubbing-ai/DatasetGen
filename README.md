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

### Data Format

The generated CSV files contain two columns:

1. Thai sentence
2. English sentence translation

Example content:

```csv
"วันนี้อากาศดีมาก ฉันคิดว่าเราควรออกไปเดินเล่นที่สวนสาธารณะด้วยกันไหม","The weather is very nice today; do you think we should go for a walk in the park together?"
"แม้ว่าฝนจะตกหนัก แต่ฉันก็ยังต้องไปทำงานเพราะมีการประชุมสำคัญที่ต้องเข้าร่วม","Even though it's raining heavily, I still have to go to work because there's an important meeting I need to attend."
"เมื่อวานฉันได้พบกับเพื่อนเก่าที่ไม่ได้เจอกันมานาน เราเลยนั่งคุยกันจนดึกดื่น","Yesterday I met an old friend whom I haven't seen in a long time, so we ended up chatting until late at night."
"ถ้าคุณมีเวลาว่างสุดสัปดาห์นี้ เราไปเที่ยวภูเขาหรือทะเลกันดีไหม","If you have free time this weekend, should we go to the mountains or the sea?"
```

Format specifications:

- CSV format with quotation marks around both Thai and English text
- Each row contains one sentence pair
- Sentences are 5-10 seconds in spoken length

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
