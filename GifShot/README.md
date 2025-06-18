# Python Window GIF Recorder

A lightweight Python script that allows you to **record a specific area of your screen and save it as an animated GIF**. Ideal for quick tutorials, UI demonstrations, or sharing bugs visually.

## Features

- Interactive area selection with mouse
- Records selected screen region as an animated GIF
- Press `ESC` to stop recording at any time
- Adjustable frame duration
- High-DPI screen compatible
- Minimal dependencies

## Requirements

- Python 3.10+
- Dependencies:
  - `pyautogui`
  - `pillow`
  - `pynput`

Recommended: Initialize the project with uv — just install uv and run `uv sync`.

## Steps:
1. Run the script.

2. Click the top-left corner of the window or area you want to record.

3. Click the bottom-right corner.

4. Press ESC to stop recording.

5. Your GIF will be saved as output.gif.