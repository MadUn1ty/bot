import os
import sys
import ctypes
import subprocess

def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        # Windows-specific code
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

def run_as_admin():
    if is_admin():
        # Already running as admin
        print("Running as administrator")
        return
    else:
        # Re-run the script with admin privileges
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

if __name__ == "__main__":
    run_as_admin()

import pyautogui as ptg
import cv2
import numpy as np
import time
from PIL import ImageGrab
import pygetwindow as gw  # Библиотека для работы с окнами
import keyboard  # Для отслеживания нажатия клавиш

# Чтение изображений без преобразования в оттенки серого
accept = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\accept.png')
acceptcheast = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\acceptcheast.png')
arhday = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\arhday.png')
arhnight = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\arhnight.png')
back = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\back.png')
cavday = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\cavday.png')
cavnight = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\cavnight.png')
cheastcommon = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\cheastcommon.png')
cheastdon = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\cheastdon.png')
cheastnormal = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\cheastnormal.png')
cheastopen = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\cheastopen.png')
crystals = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\crystals.png')
day = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\day.png')
exits = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\exit.png')
food = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\food.png')
gemday0 = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\gemday0.png')
gemday1 = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\gemday1.png')
gemday2 = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\gemday2.png')
gemday3 = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\gemday3.png')
gemday4 = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\gemday4.png')
gemnight0 = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\gemnight0.png')
gemnight1 = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\gemnight1.png')
gemnight2 = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\gemnight2.png')
gemnight3 = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\gemnight3.png')
gold = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\gold.png')
helps = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\help.png')
infday = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\infday.png')
infnight = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\infnight.png')
joinsmithy = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\joinsmithy.png')
jointraining = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\jointraining.png')
night = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\night.png')
pickup = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\pickup.png')
skintap = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\skintap.png')
smithy = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\smithy.png')
smithyday = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\smithyday.png')
smithynight = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\smithynight.png')
smithyskin = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\smithyskin.png')
speedup = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\speedup.png')
stone = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\stone.png')
takeall = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\takeall.png')
wood = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\wood.png')

# Название окна, для которого будет происходить захват
window_title = "BlueStacks App Player"

while True:
    # Проверка, была ли нажата клавиша Esc
    if keyboard.is_pressed('esc'):
        print("Остановка программы по нажатию клавиши Esc.")
        break

    # Поиск окна по названию
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
    except IndexError:
        print(f"Окно с названием '{window_title}' не найдено.")
        continue

    # Получение координат окна
    left, top, right, bottom = window.left, window.top, window.right, window.bottom

    # Захват экрана по координатам окна
    base_screen = ImageGrab.grab(bbox=(left, top, right, bottom))
    base_screen.save(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\base_screen.png')

    # Чтение захваченного экрана (оставляем в цвете)
    base = cv2.imread(r'C:\Users\rusbo\PycharmProjects\bot for RoK\image\base_screen.png')

    # Проверка всех цветных изображений
    result1 = cv2.matchTemplate(base, accept, cv2.TM_CCOEFF_NORMED)
    loc1 = np.where(result1 >= 0.8)

    result41 = cv2.matchTemplate(base, acceptcheast, cv2.TM_CCOEFF_NORMED)
    loc41 = np.where(result41 >= 0.7)

    result2 = cv2.matchTemplate(base, arhday, cv2.TM_CCOEFF_NORMED)
    loc2 = np.where(result2 >= 0.8)

    result3 = cv2.matchTemplate(base, arhnight, cv2.TM_CCOEFF_NORMED)
    loc3 = np.where(result3 >= 0.8)

    result38 = cv2.matchTemplate(base, back, cv2.TM_CCOEFF_NORMED)
    loc38 = np.where(result38 >= 0.8)

    result4 = cv2.matchTemplate(base, cavday, cv2.TM_CCOEFF_NORMED)
    loc4 = np.where(result4 >= 0.8)

    result5 = cv2.matchTemplate(base, cavnight, cv2.TM_CCOEFF_NORMED)
    loc5 = np.where(result5 >= 0.8)

    result6 = cv2.matchTemplate(base, cheastcommon, cv2.TM_CCOEFF_NORMED)
    loc6 = np.where(result6 >= 0.8)

    result7 = cv2.matchTemplate(base, cheastdon, cv2.TM_CCOEFF_NORMED)
    loc7 = np.where(result7 >= 0.8)

    result8 = cv2.matchTemplate(base, cheastnormal, cv2.TM_CCOEFF_NORMED)
    loc8 = np.where(result8 >= 0.8)

    result39 = cv2.matchTemplate(base, cheastopen, cv2.TM_CCOEFF_NORMED)
    loc39 = np.where(result39 >= 0.8)

    result9 = cv2.matchTemplate(base, crystals, cv2.TM_CCOEFF_NORMED)
    loc9 = np.where(result9 >= 0.8)

    result10 = cv2.matchTemplate(base, day, cv2.TM_CCOEFF_NORMED)
    loc10 = np.where(result10 >= 0.8)

    result11 = cv2.matchTemplate(base, exits, cv2.TM_CCOEFF_NORMED)
    loc11 = np.where(result11 >= 0.8)

    result12 = cv2.matchTemplate(base, food, cv2.TM_CCOEFF_NORMED)
    loc12 = np.where(result12 >= 0.8)

    result13 = cv2.matchTemplate(base, gemday0, cv2.TM_CCOEFF_NORMED)
    loc13 = np.where(result13 >= 0.8)

    result14 = cv2.matchTemplate(base, gemday1, cv2.TM_CCOEFF_NORMED)
    loc14 = np.where(result14 >= 0.8)

    result15 = cv2.matchTemplate(base, gemday2, cv2.TM_CCOEFF_NORMED)
    loc15 = np.where(result15 >= 0.8)

    result16 = cv2.matchTemplate(base, gemday3, cv2.TM_CCOEFF_NORMED)
    loc16 = np.where(result16 >= 0.8)

    result17 = cv2.matchTemplate(base, gemday4, cv2.TM_CCOEFF_NORMED)
    loc17 = np.where(result17 >= 0.8)

    result18 = cv2.matchTemplate(base, gemnight0, cv2.TM_CCOEFF_NORMED)
    loc18 = np.where(result18 >= 0.8)

    result19 = cv2.matchTemplate(base, gemnight1, cv2.TM_CCOEFF_NORMED)
    loc19 = np.where(result19 >= 0.8)

    result20 = cv2.matchTemplate(base, gemnight2, cv2.TM_CCOEFF_NORMED)
    loc20 = np.where(result20 >= 0.8)

    result21 = cv2.matchTemplate(base, gemnight3, cv2.TM_CCOEFF_NORMED)
    loc21 = np.where(result21 >= 0.8)

    result22 = cv2.matchTemplate(base, gold, cv2.TM_CCOEFF_NORMED)
    loc22 = np.where(result22 >= 0.8)

    result23 = cv2.matchTemplate(base, helps, cv2.TM_CCOEFF_NORMED)
    loc23 = np.where(result23 >= 0.8)

    result24 = cv2.matchTemplate(base, infday, cv2.TM_CCOEFF_NORMED)
    loc24 = np.where(result24 >= 0.8)

    result25 = cv2.matchTemplate(base, infnight, cv2.TM_CCOEFF_NORMED)
    loc25 = np.where(result25 >= 0.8)

    result26 = cv2.matchTemplate(base, joinsmithy, cv2.TM_CCOEFF_NORMED)
    loc26 = np.where(result26 >= 0.8)

    result27 = cv2.matchTemplate(base, jointraining, cv2.TM_CCOEFF_NORMED)
    loc27 = np.where(result27 >= 0.8)

    result28 = cv2.matchTemplate(base, night, cv2.TM_CCOEFF_NORMED)
    loc28 = np.where(result28 >= 0.8)

    result29 = cv2.matchTemplate(base, pickup, cv2.TM_CCOEFF_NORMED)
    loc29 = np.where(result29 >= 0.8)

    result30 = cv2.matchTemplate(base, skintap, cv2.TM_CCOEFF_NORMED)
    loc30 = np.where(result30 >= 0.8)

    result31 = cv2.matchTemplate(base, smithy, cv2.TM_CCOEFF_NORMED)
    loc31 = np.where(result31 >= 0.8)

    result32 = cv2.matchTemplate(base, smithyday, cv2.TM_CCOEFF_NORMED)
    loc32 = np.where(result32 >= 0.8)

    result40 = cv2.matchTemplate(base, smithynight, cv2.TM_CCOEFF_NORMED)
    loc40 = np.where(result40 >= 0.8)

    result33 = cv2.matchTemplate(base, smithyskin, cv2.TM_CCOEFF_NORMED)
    loc33 = np.where(result33 >= 0.8)

    result34 = cv2.matchTemplate(base, speedup, cv2.TM_CCOEFF_NORMED)
    loc34 = np.where(result34 >= 0.8)

    result35 = cv2.matchTemplate(base, stone, cv2.TM_CCOEFF_NORMED)
    loc35 = np.where(result35 >= 0.8)

    result36 = cv2.matchTemplate(base, takeall, cv2.TM_CCOEFF_NORMED)
    loc36 = np.where(result36 >= 0.8)

    result37 = cv2.matchTemplate(base, wood, cv2.TM_CCOEFF_NORMED)
    loc37 = np.where(result37 >= 0.8)

    # Проверка наличия совпадений хотя бы для одного изображения
    if len(loc23[0]) > 0:
        pt23 = list(zip(*loc23[::-1]))[0]
        click_x = left + pt23[0] + helps.shape[1] // 2
        click_y = top + pt23[1] + helps.shape[0] // 2
        ptg.click(click_x, click_y)
        print(f"Помощь прожата: ({click_x}, {click_y})")
    elif len(loc12[0]) > 0:
        pt12 = list(zip(*loc12[::-1]))[0]
        click_x = left + pt12[0] + food.shape[1] // 2
        click_y = top + pt12[1] + food.shape[0] // 2
        ptg.click(click_x, click_y)
        print(f"Еда собрана: ({click_x}, {click_y})")
    elif len(loc37[0]) > 0:
        pt37 = list(zip(*loc37[::-1]))[0]
        click_x = left + pt37[0] + wood.shape[1] // 2
        click_y = top + pt37[1] + wood.shape[0] // 2
        ptg.click(click_x, click_y)
        print(f"Дерево собрано: ({click_x}, {click_y})")
    elif len(loc22[0]) > 0:
        pt22 = list(zip(*loc22[::-1]))[0]
        click_x = left + pt22[0] + gold.shape[1] // 2
        click_y = top + pt22[1] + gold.shape[0] // 2
        ptg.click(click_x, click_y)
        print(f"Золото собрано: ({click_x}, {click_y})")
    elif len(loc35[0]) > 0:
        pt35 = list(zip(*loc35[::-1]))[0]
        click_x = left + pt35[0] + stone.shape[1] // 2
        click_y = top + pt35[1] + stone.shape[0] // 2
        ptg.click(click_x, click_y)
        print(f"Камень собран: ({click_x}, {click_y})")
    elif len(loc9[0]) > 0:
        pt9 = list(zip(*loc9[::-1]))[0]
        click_x = left + pt9[0] + crystals.shape[1] // 2
        click_y = top + pt9[1] + crystals.shape[0] // 2
        ptg.click(click_x, click_y)
        print(f"Кристалл собран: ({click_x}, {click_y})")
    # elif len(loc31[0]) > 0:
    #     pt31 = list(zip(*loc31[::-1]))[0]
    #     click_x = left + pt31[0] + smithy.shape[1] // 2
    #     click_y = top + pt31[1] + smithy.shape[0] // 2
    #     ptg.click(click_x, click_y)
    #     print(f"Кожа собрана: ({click_x}, {click_y})")
    #     if len(loc32[0]) > 0:
    #         pt32 = list(zip(*loc32[::-1]))[0]
    #         click_x = left + pt32[0] + smithyday.shape[1] // 2
    #         click_y = top + pt32[1] + smithyday.shape[0] // 2
    #         ptg.click(click_x, click_y)
    #         print(f"Кузня найдена: ({click_x}, {click_y})")
    #         if len(loc26[0]) > 0:
    #             pt26 = list(zip(*loc26[::-1]))[0]
    #             click_x = left + pt26[0] + joinsmithy.shape[1] // 2
    #             click_y = top + pt26[1] + joinsmithy.shape[0] // 2
    #             ptg.click(click_x, click_y)
    #             print(f"Вошел в кузню: ({click_x}, {click_y})")
    #             if len(loc33[0]) > 0:
    #                 pt30 = list(zip(*loc30[::-1]))[0]
    #                 click_x = left + pt30[0] + skintap.shape[1] // 2
    #                 click_y = top + pt30[1] + skintap.shape[0] // 2
    #                 ptg.click(click_x, click_y)
    #                 print(f"Добавил кожу: ({click_x}, {click_y})")
    #             else:
    #                 pt11 = list(zip(*loc11[::-1]))[0]
    #                 click_x = left + pt11[0] + exits.shape[1] // 2
    #                 click_y = top + pt11[1] + exits.shape[0] // 2
    #                 ptg.click(click_x, click_y)
    #                 print(f"Вышел из кузни: ({click_x}, {click_y})")

    elif len(loc6[0]) > 0:
        pt6 = list(zip(*loc6[::-1]))[0]
        click_x = left + pt6[0] + cheastcommon.shape[1] // 2
        click_y = top + pt6[1] + cheastcommon.shape[0] // 2
        ptg.click(click_x, click_y)
        print(f"Можно открыть сундук: ({click_x}, {click_y})")
        if len(loc39[0]) > 0:
            pt39 = list(zip(*loc39[::-1]))[0]
            click_x = left + pt39[0] + cheastopen.shape[1] // 2
            click_y = top + pt39[1] + cheastopen.shape[0] // 2
            ptg.click(click_x, click_y)
            print(f"Открыл сундук: ({click_x}, {click_y})")
            if len(loc41[0]) > 0:
                pt41 = list(zip(*loc41[::-1]))[0]
                click_x = left + pt41[0] + acceptcheast.shape[1] // 2
                click_y = top + pt41[1] + acceptcheast.shape[0] // 2
                ptg.click(click_x, click_y)
                print(f"Подтвердил: ({click_x}, {click_y})")
                if len(loc38[0]) > 0:
                    pt38 = list(zip(*loc38[::-1]))[0]
                    click_x = left + pt38[0] + back.shape[1] // 2
                    click_y = top + pt38[1] + back.shape[0] // 2
                    ptg.click(click_x, click_y)
                    print(f"Вышел из таверны: ({click_x}, {click_y})")
    else:
        print("Совпадений ни для одного изображения не найдено")

    # Пауза перед следующей проверкой
    time.sleep(2)  # Пауза 2 секунды (можно изменить по необходимости)
