# YouTube shorts Generator

> **This tool "YouTube shorts generator" is used to convert Web Articles into YouTube shorts using AI.**

> [!NOTE]
> Work in Progress

### Stuff left ToDo

- [x] Implementation of Summarizer
- [x] Implementation of TTS
- [x] Implementation of Subtitles
- [x] Implementation of final video output
- [ ] Backend
- [ ] Frontend
- [ ] Final Deployment

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
```


Create and Source a virtual environment (Linux):
```
$ python3 -m venv shortsgen-venv
$ source shortsgen/venv/activate
```

Create and Source a virtual environment (Windows):
```
python -m venv shortsgen-venv
./shortsgen-venv/Scripts/Activate
```

If you get the following error:
```
Activate.ps1 cannot be loaded because running scripts is disabled on this system.
```

Then try this:
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
./shortsgen-venv/Scripts/Activate
```

Install dependencies:
```
$ pip install sentencepiece
$ pip install transformers
$ pip install datasets
$ pip install torch
$ pip install soundfile
$ pip install elevenlabs
$ pip install python-dotenv
```
