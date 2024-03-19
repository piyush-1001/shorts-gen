# YouTube shorts Generator

> **This tool "YouTube shorts generator" is used to convert Web Articles into YouTube shorts using AI.**

> [!NOTE]
> Work in Progress

## Setup
Clone the repository:
```
git clone https://github.com/piyush-1001/shorts-gen.git
```

Clone the models:
```
#make sure git lfs is installed
git lfs install
git clone https://huggingface.co/facebook/bart-large-cnn
git clone https://huggingface.co/microsoft/speecht5_tts
```


Create and Source a virtual environment (Linux):
```
$ python3 -m venv shortsgen-venv
$ source shortsgen/venv/activate
```

Install dependencies:
```
$ pip install transformers
$ pip install datasets
$ pip install torch
# pip install soundfile
```
