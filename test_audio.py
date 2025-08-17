#!/usr/bin/env python3
"""
Simple test script to verify audio system components
"""
import os
import sys
import sounddevice as sd
import numpy as np
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_audio_devices():
    """Test if audio devices are accessible"""
    print("=== Audio Device Test ===")
    try:
        devices = sd.query_devices()
        print(f"Available audio devices: {len(devices)}")
        
        # Find default input device
        default_input = sd.query_devices(kind='input')
        print(f"Default input device: {default_input['name']}")
        
        # Find default output device
        default_output = sd.query_devices(kind='output')
        print(f"Default output device: {default_output['name']}")
        
        return True
    except Exception as e:
        print(f"Error querying audio devices: {e}")
        return False

def test_microphone():
    """Test microphone recording"""
    print("\n=== Microphone Test ===")
    try:
        # Test recording for 2 seconds
        duration = 2  # seconds
        sample_rate = 24000
        channels = 1
        
        print(f"Recording for {duration} seconds...")
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype='int16')
        sd.wait()
        
        print(f"Recording completed. Shape: {recording.shape}")
        print(f"Max amplitude: {np.max(np.abs(recording))}")
        
        return True
    except Exception as e:
        print(f"Error testing microphone: {e}")
        return False

def test_audio_playback():
    """Test audio playback"""
    print("\n=== Audio Playback Test ===")
    try:
        # Generate a simple sine wave
        duration = 1  # seconds
        sample_rate = 24000
        frequency = 440  # Hz (A note)
        
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        audio = np.sin(2 * np.pi * frequency * t) * 0.3
        audio = (audio * 32767).astype(np.int16)
        
        print("Playing test tone...")
        sd.play(audio, sample_rate)
        sd.wait()
        print("Test tone completed.")
        
        return True
    except Exception as e:
        print(f"Error testing audio playback: {e}")
        return False

def test_openai_api():
    """Test OpenAI API connection"""
    print("\n=== OpenAI API Test ===")
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("No OPENAI_API_KEY found in environment")
        return False
    
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        
        # Test a simple API call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=5
        )
        
        print("OpenAI API connection successful!")
        return True
    except Exception as e:
        print(f"Error testing OpenAI API: {e}")
        return False

def main():
    """Run all tests"""
    print("VBAIgame Audio System Test")
    print("=" * 40)
    
    tests = [
        ("Audio Devices", test_audio_devices),
        ("Microphone", test_microphone),
        ("Audio Playback", test_audio_playback),
        ("OpenAI API", test_openai_api),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"Test {test_name} failed with exception: {e}")
            results.append((test_name, False))
    
    print("\n" + "=" * 40)
    print("Test Results:")
    print("=" * 40)
    
    all_passed = True
    for test_name, result in results:
        status = "PASS" if result else "FAIL"
        print(f"{test_name}: {status}")
        if not result:
            all_passed = False
    
    print("\n" + "=" * 40)
    if all_passed:
        print("All tests passed! Audio system should work.")
    else:
        print("Some tests failed. Check the errors above.")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 