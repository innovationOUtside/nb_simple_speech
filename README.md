# nb_simple_speech
Simple speech package for Jupyter notebook using the browser's Javascript `speechSynthesis` API.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/innovationOUtside/nb_simple_speech/master)

Install via:

`pip install --upgrade git+https://github.com/innovationOUtside/nb_simple_speech.git`

Usage:

```python
from simple_speech import Speech

speaker = Speech()


# `voicelist` is automatically set as a global variable
# as part of the creation of the Speech() object
speaker.show_voices(voicelist)


speaker.set_voice(49)
speaker.say('hello how are you')

speaker.reset_count()
speaker.say('hello again')
```
