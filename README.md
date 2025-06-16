# voice-assistant


Voice Assistant with Web Automation

Overview:
This project integrates voice recognition with web automation to build a voice-controlled assistant. It listens to user voice commands, understands them, and performs tasks such as searching for information on Wikipedia, playing videos on YouTube, and answering questions using a custom infow class.

Features:
- Voice Recognition: Converts spoken words into text.
- Text-to-Speech (TTS): Provides voice responses using pyttsx3.
- Web Automation: Performs automated online searches using Selenium.
- YouTube Video Playback: Opens and plays YouTube videos based on user commands.
- ChatGPT-Powered Responses: Provides intelligent responses using a chatbot logic.

Project Structure:
- main.py: Main voice assistant script.
- Salaar.py: Contains the infow class for handling web information.
- requirements.txt: Lists required Python libraries.
- README.md: Documentation file.

Technologies and Libraries:
- pyttsx3: For text-to-speech conversion.
- speech_recognition: For converting speech to text.
- webbrowser: For opening web pages.
- selenium: For automating browser tasks.
- Salaar (custom module): Handles Wikipedia search, ChatGPT queries, and video playback.

How It Works:
1. The assistant listens for user commands.
2. It converts the voice input to text.
3. Based on the command, it may:
   - Search Wikipedia using get_info method.
   - Query a chatbot using get_data method.
   - Play a YouTube video using play_video method.

Error Handling:
- Voice assistant handles unrecognized speech and input errors.
- The infow class catches browser-related exceptions and provides feedback.

Usage Examples:
- User: "Get information about Python" -> Assistant opens Wikipedia for Python.
- User: "Play a video about space exploration" -> Assistant plays a related YouTube video.
- User: "What is machine learning?" -> Assistant returns an answer from the chatbot.

Requirements:
- Python version 3.7 or higher.
- Google Chrome browser.
- ChromeDriver installed and compatible with your Chrome version.

Installation Steps:
1. Clone the repository:
   git clone https://github.com/kiran1929/voice-assistant.git
   cd voice-assistant

2. Install required libraries:
   pip install -r requirements.txt

3. Run the assistant:
   python main.py

Contribution:
Suggestions, issues, and pull requests are welcome.

