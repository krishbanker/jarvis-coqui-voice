# Coqui TTS Voice Generator - Troubleshooting Guide

## ✅ Quick Start

### Option 1: Virtual Environment (Recommended)
```bash
chmod +x setup.sh
bash setup.sh
source venv/bin/activate
python3 app.py
```

### Option 2: Direct Installation (Fastest)
```bash
chmod +x setup_simple.sh
bash setup_simple.sh
python3 app_simple.py
```

### Option 3: One-Line Installation
```bash
pip install TTS torch torchaudio soundfile librosa numpy scipy && python3 app_simple.py
```

---

## 🔧 Common Issues & Solutions

### 1. **Python Version Error**
```
Error: Python 3.10+ required
```
**Solution:**
```bash
python3 --version  # Check your version
python3.10 app.py  # Or specify Python 3.10+
```

### 2. **ModuleNotFoundError: No module named 'TTS'**
```
Solution: Install TTS package
```bash
pip install TTS==0.22.0
```

### 3. **No CUDA/GPU Support**
```
Using device: CPU
(This is normal - will work but slower)
```
**Solution:** Install GPU drivers if you have NVIDIA GPU
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### 4. **Audio Playback Not Working**
The audio file is still generated and saved to `output/output.wav`

**Linux:** Install audio player
```bash
sudo apt-get install alsa-utils  # For aplay
# or
sudo apt-get install pulseaudio-utils  # For paplay
```

**macOS:** Should work automatically with `afplay`

**Windows:** Should work automatically

### 5. **Model Download Fails**
```
Solution: Try again (first run downloads ~380MB model)
Wait for 2-5 minutes on slow internet
```

### 6. **Out of Memory Error**
```
RuntimeError: CUDA out of memory
```
**Solution:** Use CPU instead
```bash
# Edit app.py or app_simple.py and set:
device = "cpu"
```

### 7. **Permission Denied on setup.sh**
```bash
chmod +x setup.sh setup_simple.sh
```

### 8. **torch/torchaudio Installation Issues**
```bash
# Try this for CPU version
pip install torch==2.0.1 torchvision torchaudio==2.0.2

# Or for GPU
pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 torchaudio==2.0.2+cu118 -f https://download.pytorch.org/whl/torch_stable.html
```

---

## 🚀 Force Installation (Works Anywhere)

```bash
# Step 1: Upgrade pip
python3 -m pip install --upgrade pip

# Step 2: Install PyTorch
pip install torch==2.0.1 torchaudio==2.0.2

# Step 3: Install TTS
pip install TTS==0.22.0

# Step 4: Install audio libraries
pip install soundfile librosa numpy scipy

# Step 5: Run it
python3 app_simple.py
```

---

## ✨ Features Explained

- **glow-tts**: Fast, stable, production-ready model
- **CPU Fallback**: Works with or without GPU
- **Auto-save**: Audio saved to `output/output.wav`
- **Error Handling**: Graceful recovery from errors
- **Lightweight**: Minimal dependencies

---

## 📝 Text Input Tips

- Maximum 500 characters per generation
- Works with any language TTS supports
- Output saved with timestamp if needed
- Press Ctrl+C to exit safely

---

## 💾 Output Files

All generated audio is saved to:
```
jarvis-coqui-voice/output/output.wav
```

---

## 🆘 Still Having Issues?

1. Check Python version: `python3 --version`
2. Check TTS installation: `python3 -c "from TTS.api import TTS; print('TTS OK')"`
3. Check PyTorch: `python3 -c "import torch; print(torch.__version__)"`
4. Run with verbose: `python3 app.py` (shows detailed errors)

**Last resort:** Fresh installation
```bash
pip install --upgrade --force-reinstall TTS torch torchaudio
python3 app_simple.py
```

---

## 🎉 You're All Set!

Try one of the three options above and Coqui TTS will be running! 🎤
