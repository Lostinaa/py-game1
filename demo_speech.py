#!/usr/bin/env python3
"""
Demonstration script for VBAIgame Speech-to-Speech functionality
"""
import os
import sys
import asyncio
import threading
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def print_banner():
    """Print a nice banner for the demo"""
    print("=" * 60)
    print("🎮 VBAIgame Speech-to-Speech Demo")
    print("=" * 60)
    print("This demo will show you how the speech system works.")
    print("Make sure you have:")
    print("✅ OpenAI API key in .env file")
    print("✅ Working microphone and speakers")
    print("✅ Internet connection")
    print("=" * 60)

def check_prerequisites():
    """Check if all prerequisites are met"""
    print("🔍 Checking prerequisites...")
    
    # Check OpenAI API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ OPENAI_API_KEY not found in .env file")
        return False
    print("✅ OpenAI API key found")
    
    # Check audio dependencies
    try:
        import sounddevice as sd
        import numpy as np
        print("✅ Audio libraries available")
    except ImportError as e:
        print(f"❌ Audio libraries missing: {e}")
        return False
    
    # Check OpenAI library
    try:
        from openai import AsyncOpenAI
        print("✅ OpenAI library available")
    except ImportError as e:
        print(f"❌ OpenAI library missing: {e}")
        return False
    
    return True

def test_basic_audio():
    """Test basic audio functionality"""
    print("\n🎵 Testing basic audio...")
    
    try:
        import sounddevice as sd
        import numpy as np
        
        # Test recording
        print("Recording 2 seconds of audio...")
        duration = 2
        sample_rate = 24000
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()
        
        print(f"✅ Recording successful: {recording.shape}")
        
        # Test playback
        print("Playing test tone...")
        t = np.linspace(0, 1, sample_rate, False)
        tone = np.sin(2 * np.pi * 440 * t) * 0.3
        tone = (tone * 32767).astype(np.int16)
        sd.play(tone, sample_rate)
        sd.wait()
        print("✅ Playback successful")
        
        return True
        
    except Exception as e:
        print(f"❌ Audio test failed: {e}")
        return False

def demo_realtime_api():
    """Demonstrate Realtime API connection"""
    print("\n🌐 Testing Realtime API connection...")
    
    try:
        from openai import AsyncOpenAI
        
        api_key = os.getenv('OPENAI_API_KEY')
        client = AsyncOpenAI(api_key=api_key)
        
        async def test_connection():
            try:
                async with client.beta.realtime.connect(model="gpt-4o-realtime-preview-2024-10-01") as conn:
                    print("✅ Realtime API connection successful!")
                    
                    # Update session
                    await conn.session.update(session={
                        "turn_detection": {"type": "server_vad"},
                        "response_format": {"type": "audio"}
                    })
                    print("✅ Session configuration successful!")
                    
                    return True
            except Exception as e:
                print(f"❌ Realtime API connection failed: {e}")
                return False
        
        # Run the async test
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(test_connection())
        loop.close()
        
        return result
        
    except Exception as e:
        print(f"❌ Realtime API test failed: {e}")
        return False

def show_usage_instructions():
    """Show how to use the speech system"""
    print("\n📖 Usage Instructions:")
    print("=" * 40)
    print("1. Start the game: python3 app.py")
    print("2. Use WASD to move around")
    print("3. Approach an NPC (HR or CEO)")
    print("4. Press F5 to start voice recording")
    print("5. Speak your message clearly")
    print("6. Press F5 again to stop and send")
    print("7. Listen to the NPC's voice response")
    print("8. Press F6 to check audio system status")
    print("9. Press Shift+Q to exit dialogue")
    print("=" * 40)

def main():
    """Main demo function"""
    print_banner()
    
    # Check prerequisites
    if not check_prerequisites():
        print("\n❌ Prerequisites not met. Please fix the issues above.")
        return False
    
    # Test audio
    if not test_basic_audio():
        print("\n❌ Audio test failed. Check your audio devices.")
        return False
    
    # Test Realtime API
    if not demo_realtime_api():
        print("\n❌ Realtime API test failed. Check your API key and internet connection.")
        return False
    
    print("\n🎉 All tests passed! Your system is ready for speech-to-speech.")
    
    # Show usage instructions
    show_usage_instructions()
    
    print("\n🚀 Ready to start the game? Run: python3 app.py")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 