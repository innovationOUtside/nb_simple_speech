from IPython.display import Javascript, display

class Speech():
    def __init__(self, voice=None, reset=True):
        if reset:
            self.count = 1
        self.voice = voice
        self.get_voices()

    def set_voice(self, voicenum):
        """Set voice number."""
        self.voice = voicenum

    def say(self, txt, showtext = True):
        """Speak an utterance."""
        js = f'''
        var utterance = new SpeechSynthesisUtterance("{txt}");
        '''
        if self.voice:
            js = js + f'''
            utterance.voice = window.speechSynthesis.getVoices()[{self.voice}];
            '''
        js = js + 'speechSynthesis.speak(utterance);'
        display(Javascript(js))
        
        if showtext:
            print(f'{self.count}: {txt}')
        self.count = self.count +1
        
    def reset_count(self):
        """Reset the counter."""
        self.count = 1

    def get_voices(self):
        """Get a list of supported voices.
           The voices can be seen in the notebook via the
           `voicelist` global variable.
        """
        # TO DO - how do we reference the voicelist variable in this class?
        # via https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis/getVoices
        js = '''
            var voices =  window.speechSynthesis.getVoices();
        var voicelist = '';
    for(var i = 0; i < voices.length; i++) {
    voicelist = voicelist+i+': '+ voices[i].name + ' ('+ voices[i].lang +')';
        if(voices[i].default) {
        voicelist += ' -- DEFAULT';
        }
    voicelist = voicelist + '\\n'
    }

    IPython.notebook.kernel.execute('voicelist_raw = """'+ voicelist+'"""; voicelist = voicelist_raw.split("*")');
            '''
        display(Javascript(js))
    
    def show_voices(self, voicelist):
        """Display a list of available voices."""
        print('\n'.join(voicelist))



# speaker = Speech()

# speaker.set_voice(49)
# speaker.say('hello how are you')

# speaker.show_voices(voicelist)


# speaker.reset_count()
# speaker.say('hello again')
