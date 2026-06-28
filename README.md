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

## 📚 Table of Contents

- 📌 Why the name “cori_tts”
- 🧠 Background and why Piper TTS was chosen
- ⚙️ Limitations of Piper TTS and improvements made
- 🔄 Design trade-offs and rationale
- 📩 Feedback from upstream maintainers
- 🚀 How to use cori_tts

---

## 📌 1. Why the name “cori_tts”?

The name comes from the Piper TTS public-domain voice model **“cori”**, which was used as the initial test voice.

Model:  
https://huggingface.co/rhasspy/piper-voices/blob/main/en/en_GB/cori/high/MODEL_CARD

Since it was the first model I experimented with, I named the project *cori_tts*.  
The name stuck — simple, but unexpectedly fitting.

---

## 🧠 2. Background and why Piper TTS was chosen

### Early development

This project originally started as a high school portfolio project.

 🌐 [related video (Korean)](https://youtu.be/29DK4ZOEiGU)

It began with an experimental voice dataset created in my sophomore year of high school and completed during the spring break of my senior year.

The goal was to build a TTS system and explore how synthesized speech could be used in communication and research contexts.

At the time, I also explored multilingual phoneme systems, including tonal combinations inspired by Chinese, and adapted them into early Japanese TTS prototypes.

Later, I even attempted real-time communication with a friend using this system in an online game environment.

However, the result was unstable:

- Japanese and Korean phonetics differed significantly  
- Audio playback interruptions occurred  
- Approximately 15% of communication was lost  

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

## ⚙️ 3. Limitations of Piper TTS and improvements made

While Piper TTS is powerful, its primary interface is aimed at developers.

It works well when used through Python or the command line, but from a non-technical perspective:

- Using Piper typically requires familiarity with the command line or Python.
- Switching between models may be less convenient for non-technical users.
- Quick testing generally requires some initial setup. 

To address this, cori_tts was built as a usability-focused layer on top of Piper TTS.

The goal was simple:

> “Load a model and start speaking immediately.”

---

## 🔄 4. Design trade-offs and rationale

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

## 📩 5. Feedback from upstream maintainers

To ensure proper usage, I intentionally excluded Piper TTS source code from this project.

As a result, running cori_tts requires placing `piper.exe` inside the `/piper` directory.

Since this setup is not very user-friendly, I reached out to the upstream maintainers to confirm licensing and proper usage.

Their response was:

> TODO

---

## 🚀 6. How to use cori_tts

> TODO
