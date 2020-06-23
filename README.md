# nb\_simple\_speech
Simple speech package for Jupyter notebook using the browser's Javascript `speechSynthesis` API.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/innovationOUtside/nb_simple_speech/master)

Install via:

`pip install --upgrade git+https://github.com/innovationOUtside/nb_simple_speech.git`

Usage:

```python
from simple_speech import Speech

speaker = Speech()

speaker.say('hello how are you')
speaker.say('Is it sunny today?')
```

We get a transcript of the speech by default.

Disable the trasncript with:

```python
speaker.say("It's always raining here...",showtext = False)`
```

Reset the transcript statement counter using:

```python
speaker.reset_count()
speaker.say('hello again')
```

We can get a list of available voices:

```python
# `voicelist` is automatically set as a global variable
# as part of the creation of the Speech() object
# although it is only available when
# run in a separate code cell to the object instantiation
speaker.show_voices(voicelist)
```

Set a voice as follows:
```python
speaker.set_voice(49)
```
