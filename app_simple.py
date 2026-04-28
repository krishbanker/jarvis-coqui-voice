#!/usr/bin/env python3
"""
Lightweight Coqui TTS Application
Simple, minimal version for quick voice generation
"""

import sys
import os
from pathlib import Path

# Check Python version
if sys.version_info < (3, 10):
    print(f"❌ Python 3.10+ required (you have {sys.version_info.major}.{sys.version_info.minor})")
    sys.exit(1)

try:
    from TTS.api import TTS
    import torch
    import subprocess
except ImportError as e:
    print(f"❌ Missing package: {e}")
    print("Install with: pip install TTS torch torchaudio soundfile librosa numpy scipy")
    sys.exit(1)

# Setup
device = "cuda" if torch.cuda.is_available() else "cpu"
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

print("🎤 Coqui TTS Voice Generator")
print(f"Device: {device.upper()}")
print("Type 'quit' to exit\n")

# Load TTS model
try:
    print("Loading TTS model (first run takes 1-2 minutes)...")
    tts = TTS(model_name="glow-tts", gpu=(device == "cuda"), verbose=False)
    print("✅ Ready!\n")
except Exception as e:
    print(f"❌ Failed to load model: {e}")
    sys.exit(1)

# Main loop
while True:
    try:
        text = input("Enter text: ").strip()
        
        if text.lower() in ["quit", "exit", "q"]:
            print("👋 Goodbye!")
            break
        
        if not text:
            continue
        
        # Generate speech
        output_file = output_dir / "output.wav"
        text = text[:500]  # Limit length
        
        print("Generating...")
        tts.tts_to_file(text=text, file_path=str(output_file))
        print(f"✅ Saved to {output_file}")
        
        # Try to play
        try:
            if sys.platform == "darwin":
                subprocess.run(["afplay", str(output_file)], timeout=60)
            elif sys.platform == "linux":
                for player in ["aplay", "paplay", "ffplay"]:
                    try:
                        subprocess.run([player, str(output_file)], timeout=60)
                        break
                    except:
                        pass
            elif sys.platform == "win32":
                os.startfile(str(output_file))
        except:
            print(f"(Audio saved, playback skipped)")
        
        print()
    
    except KeyboardInterrupt:
        print("\n👋 Interrupted!")
        break
    except Exception as e:
        print(f"❌ Error: {e}\n")
