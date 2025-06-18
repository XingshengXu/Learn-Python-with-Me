import os
import time
import pyautogui
from PIL import ImageGrab
from pynput import keyboard
from pynput.mouse import Listener

output_file = "output.gif"
frame_duration = 0.2

stop_recording = False
window = {'x': 0, 'y': 0, 'width': 0, 'height': 0}


def on_click(x, y, button, pressed):
    if pressed:
        click_positions.append((x, y))
    if len(click_positions) == 1:
        print('请点击窗口右下角来完成选区。')
    if len(click_positions) == 2:
        return False


def get_two_click_coordinates():
    global click_positions
    click_positions = []

    clicks = 0
    print('请点击窗口左上角以开始选区。')
    while clicks < 2:
        with Listener(on_click=on_click) as listener:
            listener.join()
        clicks += 1

    return click_positions


def calculate_rectangle_dimensions(coord1, coord2):
    global window

    width = abs(coord2[0] - coord1[0])
    height = abs(coord2[1] - coord1[1])

    window.update(x=int(coord1[0]), y=int(coord1[1]),
                  width=int(width), height=int(height))

    return width, height


def on_press(key):
    global stop_recording

    if key == keyboard.Key.esc:
        stop_recording = True


def record_gif(top_left, window, output_file, duration=0.1):
    frames = []

    print(f"录制中... 每帧间隔: {duration:.2f}s, 按 'q' 键结束录制。")

    with keyboard.Listener(on_press=on_press) as listener:
        while not stop_recording:
            screenshot = pyautogui.screenshot(
                region=(top_left[0], top_left[1], window['width'], window['height']))
            frames.append(screenshot)
            time.sleep(duration)

    if os.path.exists(output_file):
        print(f"警告：文件 '{output_file}' 已存在，将被覆盖。")

    print(f"正在保存 GIF 到 {output_file}")
    frames[0].save(
        output_file,
        save_all=True,
        append_images=frames[1:],
        duration=int(duration * 1000),
        loop=0,
    )
    print("GIF 已保存。")


def main():
    global window

    coordinates = get_two_click_coordinates()
    print(f"第一次点击: {coordinates[0]}, 第二次点击: {coordinates[1]}")

    width, height = calculate_rectangle_dimensions(
        coordinates[0], coordinates[1])
    print(f"选区尺寸: 宽 = {width}, 高 = {height}")

    virtual_screen_width, virtual_screen_height = pyautogui.size()
    screenshot = ImageGrab.grab()
    screen_width, screen_height = screenshot.size
    pixel_ratio = int(screen_width / virtual_screen_width)

    window.update(x=int(window['x'] * pixel_ratio), y=int(window['y'] * pixel_ratio),
                  width=int(window['width'] * pixel_ratio), height=int(window['height'] * pixel_ratio))

    print(
        f"位置: x={window['x']}, y={window['y']}, 宽={window['width']}, 高={window['height']}")

    top_left = (window['x'], window['y'])
    record_gif(top_left, window, output_file, frame_duration)


if __name__ == "__main__":
    main()
