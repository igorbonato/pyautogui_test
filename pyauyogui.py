import pyautogui
import time
import pyperclip

pyautogui.alert(
    'nao mexa no seu pc enquanto o programa roda!!!')

time.sleep(5)
pyautogui.hotkey('winleft', 'r')
pyautogui.write('msedge')
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(985, 37, clicks=2)

pyautogui.PAUSE = 0.5
# pyautogui.hotkey('ctrl', 't')
url = 'outlook.live.com'
pyperclip.copy(url)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(8)

pyautogui.click(113, 140, clicks=2)
time.sleep(8)
pyautogui.write('igorbonato99@hotmail.com')
time.sleep(2)
pyautogui.press('tab', presses=4)
time.sleep(1)
pyautogui.write('testando 123')
time.sleep(2)
pyautogui.click(458, 338)
time.sleep(1)
pyautogui.write('código funcionando, que belezinha!')
time.sleep(1)
pyautogui.click(244, 633, clicks=2)

pyautogui.alert(
    'programa acabou!\npode voltar a usar o pc!')
