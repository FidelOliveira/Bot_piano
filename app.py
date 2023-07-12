# Passos para criar um código python  que verifica se há um botão com a cor correspondente dentro do círculo daquela cor
# O jogo que foi utilizado como referência para o teste foi: https://www.crazygames.com/game/magic-piano-tiles


import pyautogui
import keyboard
from time import sleep

# Se for necessário clicar de forma rápida, basta instalar a biblioteca pywin32, tendo em vista que essa biblioteca clica mais rapidamente que o pyautogui
import win32api
import win32con

# Caso seja necessário algum click para que o jogo tenha inicio
# pyautogui.click(x, y, duration=2)

def click(x, y): 
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# O código vai funcionar até que se aperte '1'
while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(x, y, (0, 0, 0)): # Informar localização e a cor correspondente
        click(x, y)
    if pyautogui.pixelMatchesColor(x, y, (0, 0, 0)): # Informar localização e a cor correspondente
        click(x, y)
    if pyautogui.pixelMatchesColor(x, y, (0, 0, 0)): # Informar localização e a cor correspondente
        click(x, y)
    