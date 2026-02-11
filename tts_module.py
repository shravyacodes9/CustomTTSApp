"""
Text-to-Speech Module using pyttsx3 engine
"""

import pyttsx3
import threading
from queue import Queue


class TextToSpeech:
    """
    Text-to-Speech engine wrapper using pyttsx3
    """
    
    def __init__(self):
        """Initialize the TTS engine"""
        self.engine = pyttsx3.init()
        self.is_speaking = False
        self.is_paused = False
        self.callback = None
        self.highlight_mode = "word"
        self.tts_thread = None
        self.word_queue = Queue()
        
        # Configure engine
        self.engine.setProperty('rate', 170)  # Default speaking rate
        self.engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
        
        # Get available voices
        try:
            voices = self.engine.getProperty('voices')
            if voices:
                self.engine.setProperty('voice', voices[0].id)  # Use first available voice
        except:
            pass
    
    
    def set_callback(self, callback):
        """
        Set a callback function to be called during speech
        
        Args:
            callback: Function to call with (word_idx, word, line_idx) parameters
        """
        self.callback = callback
    
    
    def set_highlight_mode(self, mode):
        """
        Set the highlight mode (word or line)
        
        Args:
            mode (str): 'word' or 'line'
        """
        self.highlight_mode = mode
    
    
    def set_rate(self, rate):
        """
        Set the speaking rate
        
        Args:
            rate (int): Speaking rate in words per minute (typically 50-300)
        """
        try:
            self.engine.setProperty('rate', rate)
        except Exception as e:
            print(f"Error setting rate: {e}")
    
    
    def set_volume(self, volume):
        """
        Set the volume level
        
        Args:
            volume (float): Volume level (0.0 to 1.0)
        """
        try:
            self.engine.setProperty('volume', max(0.0, min(1.0, volume)))
        except Exception as e:
            print(f"Error setting volume: {e}")
    
    
    def speak(self, text):
        """
        Speak the given text
        
        Args:
            text (str): Text to speak
        """
        if not text.strip():
            return
        
        # Run in separate thread to avoid blocking UI
        self.tts_thread = threading.Thread(target=self._speak_thread, args=(text,))
        self.tts_thread.daemon = True
        self.tts_thread.start()
    
    
    def _speak_thread(self, text):
    
        try:
            self.is_speaking = True
            self.is_paused = False

            # Precompute words and lines for highlighting
            words = text.split()
            lines = text.split('\n')

            # Queue the whole text ONCE
            self.engine.say(text)

            # Start a parallel loop for highlighting
            def highlight_loop():
                total_chars_by_line = []
                running = 0
                for line in lines:
                    running += len(line) + 1
                total_chars_by_line.append(running)

            for idx, word in enumerate(words):
                if not self.is_speaking or self.is_paused:
                    break

                if self.callback and self.highlight_mode == "word":
                    char_pos = sum(len(w) + 1 for w in words[:idx])
                    line_idx = 0
                    for i, lim in enumerate(total_chars_by_line):
                        if char_pos <= lim:
                            line_idx = i
                            break
                    # Call GUI callback
                    self.callback(idx, word, line_idx)

        # Run highlighting in same thread before blocking runAndWait()
        highlight_thread = threading.Thread(target=highlight_loop, daemon=True)
        highlight_thread.start()

        # Let engine speak the queued text
        self.engine.runAndWait()

        self.is_speaking = False

    except Exception as e:
        print(f"Error in TTS: {e}")
        self.is_speaking = False


    
    
    def pause(self):
        """Pause the current speech"""
        try:
            if self.is_speaking and not self.is_paused:
                # pyttsx3 doesn't have native pause, we'll stop instead
                self.engine.stop()
                self.is_paused = True
                self.is_speaking = False
        except Exception as e:
            print(f"Error pausing: {e}")
    
    
    def resume(self):
        """Resume the paused speech (Note: requires storing the text)"""
        # This is a limitation of pyttsx3 - it doesn't support true pause/resume
        # We would need to store the text and restart from where it left off
        print("Resume not fully supported - please use Play to restart")
    
    
    def stop(self):
        """Stop the current speech"""
        try:
            if self.is_speaking or self.is_paused:
                self.engine.stop()
                self.is_speaking = False
                self.is_paused = False
        except Exception as e:
            print(f"Error stopping: {e}")
    
    
    def get_available_voices(self):
        """
        Get list of available voices
        
        Returns:
            list: List of voice information dictionaries
        """
        try:
            voices = self.engine.getProperty('voices')
            return voices
        except:
            return []
    
    
    def set_voice(self, voice_id):
        """
        Set the voice to use
        
        Args:
            voice_id (str): ID of the voice to use
        """
        try:
            self.engine.setProperty('voice', voice_id)
        except Exception as e:
            print(f"Error setting voice: {e}")
    
    
    def is_busy(self):
        """
        Check if the engine is currently speaking
        
        Returns:
            bool: True if speaking, False otherwise
        """
        return self.is_speaking
