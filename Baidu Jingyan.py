import webview
import os

DIR = os.path.abspath(os.path.dirname(__file__))
"""
This example demonstrates how to create a webview window.
"""
icon_path = os.path.join(DIR, 'icon.jpg')
if __name__ == '__main__':
    # Create a standard webview window
    window = webview.create_window('百度经验', 'https://jingyan.baidu.com')
    webview.start()
