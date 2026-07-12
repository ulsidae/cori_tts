# cori_tts 

> A UX-oriented wrapper built on top of Piper TTS.

Long ago, I suffered from a severe cold that left me unable to speak.  
In that silence, I started thinking: *what if I could prepare my voice in advance?*

A strange idea came to mind —  
“Why not just record my voice beforehand?”

That simple thought became the starting point of this project.

Over time, it evolved into something more practical:  
a system focused not only on speech synthesis, but also on usability, time efficiency, and real-world constraints.

This document summarizes the cori_tts project and the design decisions behind building a practical TTS system.

---

> ⚠️ **Important**
> cori_tts is licensed under the GNU GPL v3.0, the same license used by Piper TTS.
> It is freely available as open-source software.

---
  
| 📚 Table of Contents |
| :--- |
| [📌 Why the name “cori_tts”?](#0) |
| [🧠 Background and why Piper TTS was chosen](#1) |
| [⚙️ Limitations of Piper TTS and improvements made](#2) |
| [🔄 Design trade-offs and rationale](#3) |
| [📩 Feedback from upstream maintainers](#4) |
| [🚀 How to use cori_tts](#5) |

---

<h2 id="0">📌 1. Why the name “cori_tts”?</h2>

The name comes from the Piper TTS public-domain voice model **“cori”**, which was used as the initial test voice.

Model:  
https://huggingface.co/rhasspy/piper-voices/blob/main/en/en_GB/cori/high/MODEL_CARD

Since it was the first model I experimented with, I named the project *cori_tts*.  
The name stuck — simple, but unexpectedly fitting.

---

<h2 id="1">🧠 2. Background and why Piper TTS was chosen</h2>

### Early development

This project originally started as a high school portfolio project.

<img src="https://github.com/ulsidae/cori_tts/blob/main/img/IMG_0447.PNG" height="400"/>

 🌐 [related video (Korean)](https://youtu.be/29DK4ZOEiGU)

It began with an experimental voice dataset created in my sophomore year of high school and completed during the spring break of my senior year.

The goal was to build a TTS system and explore how synthesized speech could be used in communication and research contexts.

At the time, I also explored multilingual phoneme systems, including tonal combinations inspired by Chinese, and adapted them into early Japanese TTS prototypes.

Later, I even attempted real-time communication with a friend using this system in an online game environment.

However, the result was unstable:

- Japanese and Korean phonetics differed significantly  
- Audio playback interruptions occurred  
- Based on these early experiments, approximately 15% of communication was lost  

This made it clear that the system needed a fundamental redesign.

---

### Transition to English-based experiments

 🌐 [related videos](http://youtube.com/watch?v=tMdp9uIgFi8&list=PLX1CN-Qq27HF1DIDQODYL4SVXQI7EffGf&index=3)

To address these issues, I shifted the system to English and restarted experiments.

This allowed me to study pronunciation differences more deeply.

For example:

- The pronunciation of “J” differs between Spanish and English  
- Words like “John” and “José” demonstrate distinct phonetic behaviors  

This led me to refine the system toward a recording-and-replay-based synthesis approach.

Code reference:  
https://github.com/ulsidae/dev_logs/tree/main/AI/My%20own%20voice%20TTS

One notable attempt involved adding timed pauses between recorded segments to simulate natural speech flow.

---

### Why Piper TTS

Eventually, I realized that manually recording every word was not scalable.

Although the approach worked, it was inefficient and did not scale in terms of time or maintenance.

While searching for alternatives, I discovered Piper TTS.

What stood out was:

- Support for custom voice models  
- Availability of prebuilt test voices  
- A strong open-source ecosystem  

Although its primary workflow is command-line based, it provided a far more practical path toward usable speech synthesis.

---

<h2 id="2">⚙️ 3. Limitations of Piper TTS and improvements made</h2>

While Piper TTS is powerful, its primary interface is aimed at developers.

It works well when used through Python or the command line, but from a non-technical perspective:

- Using Piper typically requires familiarity with the command line or Python.
- Switching between models may be less convenient for non-technical users.
- Quick testing generally requires some initial setup. 

To address this, cori_tts was built as a usability-focused layer on top of Piper TTS.

The goal was simple:

> “Load a model and start speaking immediately.”

---

<h2 id="3">🔄 4. Design trade-offs and rationale</h2>

Building cori_tts involved several intentional trade-offs.

The core design decision can be summarized as:

**flexibility vs usability** and **control vs time efficiency**

- Keeping raw Piper TTS would maximize flexibility but reduce usability  
- Building a wrapper system reduces flexibility but significantly improves user experience  
- The simplified workflow prioritizes time efficiency over full configuration control  

From a trade-off management perspective, the system prioritizes:

> time efficiency + accessibility + open-source compatibility

rather than maximal configurability.

This also means cori_tts is not intended to replace Piper TTS, but to reduce friction in real-world usage.

---

<h2 id="4">📩 5. Upstream Feedback and Licensing Discussion</h2>

- Running cori_tts requires placing `piper.exe` inside the `/piper` directory.

To ensure proper licensing and compatibility, I contacted the Piper TTS upstream maintainer regarding the development of a usability-focused wrapper around Piper.

The main questions were:

- Whether a wrapper-based approach for improving usability was appropriate
- How the GPL license applies to a project built around Piper
- Whether there were recommended approaches for improving local usage

The maintainer replied that there were no issues with wrappers around Piper, especially when they improve usability.

Key feedback:

> "I have no problem with wrappers around Piper, especially if they improve usability :)"

The maintainer explained the relationship between Piper's GPL licensing and its upstream dependencies, including `espeak-ng`, and suggested using Piper's built-in local HTTP server for easier browser-based testing.

This feedback confirmed the design direction of cori_tts as a usability-focused layer built on top of Piper while maintaining open-source compatibility.

---

<h2 id="5">🚀 6. How to use cori_tts</h2>

> **Note**:
> cori_tts is currently designed for Windows.
> Support for Linux and other operating systems is planned for future releases.

### 1. Install Piper TTS

Download Piper TTS from the official repository:

Official repository: [Piper TTS](https://github.com/OHF-Voice/piper1-gpl)

Install the required Python package:

```bash
pip install piper-tts
```

> **Tip**: 
> If you encounter issues while using Piper TTS, installing [`espeak-ng`](https://github.com/espeak-ng/espeak-ng) may resolve them.

---

### 2. Download this repository

<img src="https://github.com/ulsidae/cori_tts/blob/main/img/1.png" height="400"/>

Clone or download the `cori_tts` repository.

---

### 3. Add `piper.exe`

<img src="https://github.com/ulsidae/cori_tts/blob/main/img/2.png" height="400"/>

Copy the `piper.exe` file from your Piper TTS installation into the `piper/` directory of this project.

---

### 4. Download a voice model

Download your preferred voice model from: [Piper TTS Voice Models](https://huggingface.co/rhasspy/piper-voices/tree/main)

> **Important**: 
> Voice models may use different licenses.
> Please review the license before using a model.

---

### 5. Place the model files

<img src="https://github.com/ulsidae/cori_tts/blob/main/img/3.png" height="400"/>

Copy the following files into the `models/` directory:

- `.onnx`
- `.json`
- `MODEL_CARD`

All three files are required for each voice model.

---

### 6. (Optional) Customize the character image

<img src="https://github.com/ulsidae/cori_tts/blob/main/img/4.png" height="400"/>

You can replace `character.png` to visually distinguish different voice models.

If you use multiple models, you may create multiple copies of `cori_tts`, each configured for a different voice.

---

### 7. Launch cori_tts

If you follow this instruction, the cori_tts directory structure may look like this:

```
cori_tts/
├── main.py              
├── character.png        
├── models/             
│   └── [model_name].onnx
│   └── [model_name].json
│   └── MODEL_CARD
└── piper/               
    └── piper.exe        
```

Run `main.py`.

<img src="https://github.com/ulsidae/cori_tts/blob/main/img/5.png" height="400"/>

Write the text you want to synthesize in a `.txt` file, then select that file by clicking the "Select TXT" button.

---

### 8. Wait for synthesis

By pressing the "RUN TTS" button, you can generate the synthesized audio.
After processing is complete, the generated audio file will be saved in the `output/` directory.

---

### 9. You're ready to use cori_tts!

You can now continue generating speech by selecting any supported text file through `cori_tts`.

---

### 📚 Building an executable

If you prefer a standalone executable, you can build `cori_tts` using PyInstaller.


> The goal of cori_tts is to make local TTS technology more accessible by reducing the technical barriers of existing command-line workflows.
