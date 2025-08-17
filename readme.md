# VBAIgame - Speech-to-Speech Integration

A 3D adventure game with integrated OpenAI Realtime API for natural speech-to-speech interactions with NPCs.

## Features

- **3D OpenGL Graphics**: Immersive 3D office environment
- **Speech-to-Speech**: Real-time voice conversations with NPCs using OpenAI Realtime API
- **Text Chat**: Traditional text-based conversations as fallback
- **NPC Characters**: HR Director and CEO with unique personalities
- **Push-to-Talk**: F5 key for voice recording

## Prerequisites

- Python 3.8+
- OpenGL support
- PyGame

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Felmeta-M/VBAIgame.git
   cd VBAIgame
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:
   ```plaintext
   OPENAI_API_KEY=your_api_key_here
   ```

## Project Structure

```plaintext
venture-builder-ai/
├── textures/           # Generated texture files
│   ├── wall.png
│   ├── floor.png
│   └── ceiling.png
├── texture_generator.py # Texture generation script
├── requirements.txt    # Project dependencies
├── .env               # Environment variables (not in repo)
└── README.md          # Project documentation
```

## Usage

1. Generate textures (if not already present):
   ```bash
   python texture_generator.py
   ```

2. upgrade openai
```bash
   pip install --upgrade openai
   ```

2. Run the main application:
   ```bash
   python app.py
   ```

   ### Controls

- **WASD**: Move around the 3D environment
- **Mouse**: Look around
- **E**: Interact with NPCs (when close)
- **F5**: Push-to-talk for voice recording
- **Enter**: Send text messages
- **Shift+Q**: Exit dialogue
- **Escape**: Exit game

### Speech-to-Speech Interaction

1. **Approach an NPC** (HR or CEO) within interaction distance
2. **Press F5** to start recording your voice
3. **Speak your message** clearly into the microphone
4. **Press F5 again** to stop recording and send to the NPC
5. **Listen** to the NPC's voice response

### Text Chat (Fallback)

If voice isn't working or you prefer typing:
1. **Approach an NPC** as above
2. **Type your message** in the text input
3. **Press Enter** to send

## Audio System

The game uses a sophisticated audio pipeline:

- **Input**: Real-time microphone recording (24kHz, mono, 16-bit)
- **Processing**: OpenAI Realtime API for speech recognition and generation
- **Output**: Real-time audio playback through speakers/headphones

### Audio Troubleshooting

If you experience audio issues:

1. **Run the audio test**:
   ```bash
   python3 test_audio.py
   ```

2. **Check audio devices**:
   - Ensure microphone is not muted
   - Check system audio settings
   - Verify device permissions

3. **Common issues**:
   - **No sound**: Check speaker volume and device selection
   - **No microphone**: Check microphone permissions and device selection
   - **Audio lag**: Check internet connection (OpenAI API dependency)


## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for providing the AI capabilities
- PyGame community for the gaming framework
- OpenGL for 3D rendering support
```

