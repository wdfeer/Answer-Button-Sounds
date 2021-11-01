"""
Answer Button Sounds addon for Anki 2.1.20 by Kyle "Khonkhortisan" Mills
"""

import os

from anki import hooks
from aqt.sound import play, clearAudioQueue, AVPlayer
#from aqt.reviewer import Reviewer

addon_path = os.path.dirname(__file__)
user_files = os.path.join(addon_path, "user_files")

#add sounds for extra buttons here
file_names_by_ease = {
	1: "again.mp3",
	2: "hard.mp3",
	3: "good.mp3",
	4: "easy.mp3"
}

def answersound(card, ease, early):
	if (ease not in file_names_by_ease.keys()): 
	    return
	clearAudioQueue() #force feedback to play now. Apparently this has to be within the if to be defined. Or I have to stop using the python console as if it's the addon.
	play(os.path.join(user_files, file_names_by_ease[ease]))
	
	#preventclearingAudioQueue() #see ~~nextCard()~~ play_tags #force feedback to continue playing now
hooks.schedv2_did_answer_review_card.append(answersound)

def _play_tags(self, tags):
    """Clear the existing queue, then start playing provided tags."""
    self._enqueued = tags[:]
    #if self.interrupt_current_audio:
    #if self.interrupt_current_audio and not nextCard
    if self.interrupt_current_audio and False: #TODO: do clear audio when flipping to back, don't clear it when going to the next card. This was easier when it was in the nextCard function so I could just disable it there.
        self._stop_if_playing()
    self._play_next_if_idle()
AVPlayer.play_tags=_play_tags

#def pageflip(self, url):
#	play(os.path.join(user_files, "flip.mp3"))
#	error();
#	if url == "ans":
#		clearAudioQueue()
#		play(os.path.join(user_files, "flip.mp3"))
#		#preventclearingAudioQueue()
#		error();
#	#if url == "del":
#	#	clearAudioQueue()
#	#	play(os.path.join(user_files, "rip.mp3"))
#	#	#preventclearingAudioQueue()
#	#	error();
#Reviewer._linkHandler = hooks.wrap(Reviewer._linkHandler, pageflip, "before")