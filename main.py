import flet as ft
import asyncio
import requests
import os
import subprocess
import zipfile
import json
from pypresence import Presence
import time
import shutil
import sys
from gd.api import save

version = "1.1.1"
temp_folder_path = "C:\\TempL"

if os.path.exists(temp_folder_path):
    shutil.rmtree(temp_folder_path)
    print("Папка TempL успешно удалена.")
else:
    print("TempL не найдена")

try:
    CLIENT_ID = "1144219121693757490"

    # Детали
    DETAILS = "Он играет в ReGDS"
    STATE = "Launcher"
    LARGE_IMAGE = "https://cdn.fruitspace.one/server_icons/gd_00kz.png"
    BUTTON = [
        {
            "label": "Скачать ReGDS", #Название кнопки
            "url": "https://gofruit.space/gdps/00kz" #ссылка
        },
        { #Если нужно несколько кнопок
            "label": "Наш Discord",
            "url": "https://discord.gg/HY6emWTRCv"
        }
    ]
except:
    drpc = True
try:
    RPC = Presence(CLIENT_ID)
except:
    drpc = True
    
def self_delete():
    script_path = os.path.abspath(__file__)
    try:
        os.remove(script_path)
        print("Скрипт успешно удален.")
    except Exception as e:
        print("Ошибка при удалении скрипта:", e)

def get_icons(id):
    try:
        response = requests.get(f"http://217.18.62.111/icon.php?id={id}")
        response_data = json.loads(response.text)
        return f"https://gdbrowser.com/iconkit/premade/icon_{response_data['accIcon']}.png"
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def get_news():
    try:
        response = requests.get("http://217.18.62.111/new.php")
        response_data = response.json()

        # Получаем значения из ответа
        global topic
        global avatar
        global description
        avatar = response_data.get('avatar', '')
        description = response_data.get('description', '')
        topic = response_data.get('topic', '')

        # Выводим полученные данные
        print(f"Avatar: {avatar}")
        print(F"Topic: {topic}")
        print(f"Description: {description}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def folder_exists(folder_path):
    return os.path.exists(folder_path) and os.path.isdir(folder_path)

def top1():
    json_string = requests.get("http://217.18.62.111/leader_top.php?top=1")
    top = json.loads(json_string.text)
    for item in top:
        return item
    
def creator1():
    json_cp = requests.get("http://217.18.62.111/leader_creator.php?top=1")
    # Разбор JSON-строки в список словарей

    cp = json.loads(json_cp.text)
    # Теперь переменная 'data' содержит список словарей, которые вы можете обрабатывать
    for item in cp:
        return item
def on_launcher_update():
    ver = version
    url = "http://217.18.62.111/lanch_ver.txt"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            global new_version
            new_version = response.text

        else:
            print(f"Ошибка при запросе: {response.status_code}")
            return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return e
    if ver == new_version:
        return 0
    else:
        return 1
    

async def on_update():
    path = r"C:\Games\ReGDS\ver.txt"
    path_fold = r"C:\Games\ReGDS"

    if folder_exists(path_fold):
        print("ReGDS установлен")
    else:
        return 3
    with open(path, "r") as ver:
        version = ver.read()
        url = "http://217.18.62.111/version.txt"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                content = response.text
            else:
                print(f"Ошибка при запросе: {response.status_code}")
                return response.status_code
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return e
    if version == content:
        return 0
    else:
        return 1



class GD_User:
    account_id = None
    account = None

    def __init__(self) -> None:
        try:
            self.account = save.load()
            self.account_id = self.account.account_id
        except:
             self.account_id = -1
             
    def get_name(self):
        return self.account_id if self.account_id != -1 else None
    
    def if_login(self):
        return True if self.account_id != -1 else False

def main(page: ft.Page):
    global drpc
    descript_launcher_response = requests.get("http://217.18.62.111/regds_descript.txt", )
    descript_launcher = descript_launcher_response.content.decode('utf-8')
    page.title = "ReGDSL"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_height = 560
    page.window_width = 900
    page.window_resizable = False
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.bgcolor = "#1E1E1E"
    page.window_frameless = True
    page.on_scroll_interval = 1
    page.update()
    get_news()
    def p_text(text):
        text_prgs.value = text
        text_prgs.update()

    def dialog(text):
        dlg = ft.AlertDialog(
        title=ft.Text(text)
        )
        page.dialog = dlg
        dlg.open = True
        page.update()
        
    def open_regds(e):
        try:
            os.chdir("C:\Games\ReGDS")
        except:
            d_content.clear()
            d_content.append(d_check)
            download.update()

            upd = asyncio.run(on_update())
            time.sleep(1)         
            if upd == 0:
                d_content.clear()
                d_content.append(d_open)
                download.update()
                p_text("Произошла ошибка при открытии, обратитесь к Админестрации")
                return
            elif upd == 3:
                d_content.clear()
                d_content.append(d_con)
                download.update()
                return
            else:
                d_content.clear()
                d_content.append(d_upd)
                download.update()
                return
        app_path = r"C:\Games\ReGDS\ReGDS.exe"
        try:
            process = subprocess.Popen(app_path)
            return_code = process.wait()  # Ждем, пока приложение будет закрыто
            p_text(f"Приложение закрыто. Код завершения: {return_code}")
        except FileNotFoundError:
            d_content.clear()
            d_content.append(d_con)
            download.update()
        except Exception as e:
            p_text(e)
    def download_regds(e):
        folder_name = 'Games'
        target_directory = 'C:\\'  # Полный путь к целевой директории

        # Формируем полный путь к новой папке
        new_folder_path = os.path.join(target_directory, folder_name)

        # Проверяем, существует ли папка уже, чтобы избежать ошибок
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
            text_prgs.value = f"Папка '{new_folder_path}' успешно создана."
            text_prgs.update()
        else:
            text_prgs.value = f"Папка '{new_folder_path}' уже существует."
            text_prgs.update()

        
        download.padding = 0
        d_content.clear()
        d_content.append(d_progress)
        d_progress.color="#549FFF"
        url = "https://remeow.ru/drive/uploads/806215/ReGDS.zip"
        response = requests.get(url, stream=True)

        file_size = int(response.headers.get("content-length", 0))

        chunk_size = 1024
        downloaded = 0
        with open("C:\Games\ReGDS.zip", "wb") as f:
            for data in response.iter_content(chunk_size=chunk_size):
                downloaded += len(data)
                f.write(data)
                progress = int((downloaded / file_size) * 100)
                text_prgs.value = f"Прогресс: {progress:.2f}%"
                pbp = progress/100
                d_progress.value = pbp
                download.update()
                text_prgs.update()
                
        unzip()
        
        if asyncio.run(on_update()) == 0:
            d_content.clear()
            d_content.append(d_open)
            download.padding = 15
            # download.update()
            dialog("ReGDS Успешно устоновлен!")
            page.update()
        else:
            dialog("Произошла ошибка при установке, обратитесь к Админестрации!")
            page.update()

    def unzip():
        # Путь к архиву
        archive_path = 'C:/Games/ReGDS.zip'

        # Путь к папке, куда нужно распаковать
        extract_path = 'C:/Games/ReGDS/'

        # Создаем папку, если она не существует
        if not os.path.exists(extract_path):
            os.makedirs(extract_path)

        # Получаем информацию о количестве файлов в архиве
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            total_files = len(zip_ref.infolist())

        # Открываем архив
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            for idx, file_info in enumerate(zip_ref.infolist()):
                zip_ref.extract(file_info, extract_path)
                
                # Вычисляем и выводим текущий процент выполнения
                progress = (idx + 1) / total_files * 100
                
                text_prgs.value = f"Прогресс: {progress:.2f}%"
                pgs = progress/100
                d_progress.color = "#FFB900" 
                d_progress.value = pgs
                text_prgs.update()
                d_progress.update()
        p_text(f"Архив успешно распакован в {extract_path}")
        os.remove(archive_path)
    

    def news_view(e):
        page.controls.clear()
        page.auto_scroll = True
        page.scroll = True
        page.add(
        ft.Row(
                [
            ft.IconButton(ft.icons.ARROW_BACK, on_click=go_Main),
            ft.WindowDragArea(ft.Container(ft.Text(topic, size=20), padding=10), expand=True),
            ft.IconButton(ft.icons.CLOSE, on_click=lambda _: page.window_close()),
            
                ]
            )
        )
        page.add(
            ft.Image(avatar, border_radius=10)
        )
        page.add(ft.Text(description))
        
        page.update()








    def update_launcher(e):
        # Путь к папке Temp
        temp_folder_path = "C:\\TempL"

        # Проверяем, существует ли папка уже
        if not os.path.exists(temp_folder_path):
            os.mkdir(temp_folder_path)
            p_text("Временная папка созданна ✅")
        else:
            print("Временная папка уже существует")

        download.padding = 0
        d_content.clear()
        d_content.append(d_progress)
        d_progress.value = 0
        download.update()

        url = "https://remeow.ru/drive/uploads/806215/ReGDSL.exe"
        response = requests.get(url, stream=True)

        file_size = int(response.headers.get("content-length", 0))

        chunk_size = 1024
        downloaded = 0
        with open(r"C:\TempL\ReGDSL.exe", "wb") as f:
            for data in response.iter_content(chunk_size=chunk_size):
                downloaded += len(data)
                f.write(data)
                progress = int((downloaded / file_size) * 100)
                text_prgs.value = f"Загрузка новой версии: {progress:.2f}%"
                pbp = progress/100
                d_progress.value = pbp
                download.update()
                text_prgs.update()

        d_progress.value = 0
        d_progress.color = "#ff0000"
        download.update()

        url = "http://217.18.62.111/updater.exe"
        response = requests.get(url, stream=True)
        
        file_size = int(response.headers.get("content-length", 0))

        chunk_size = 1024
        downloaded = 0

        with open(r"C:\TempL\updater.exe", "wb") as f:
            for data in response.iter_content(chunk_size=chunk_size):
                downloaded += len(data)
                f.write(data)
                progress = int((downloaded / file_size) * 100)
                text_prgs.value = f"Загрузка обновителя: {progress:.2f}%"
                pbp = progress/100
                d_progress.value = pbp
                download.update()
                text_prgs.update()

        d_progress.value = 0
        d_progress.color = "#00ff00"
        download.update()

        url = "http://217.18.62.111/start.exe"
        response = requests.get(url, stream=True)
        
        file_size = int(response.headers.get("content-length", 0))

        chunk_size = 1024
        downloaded = 0

        with open(r"C:\TempL\start.exe", "wb") as f:
            for data in response.iter_content(chunk_size=chunk_size):
                downloaded += len(data)
                f.write(data)
                progress = int((downloaded / file_size) * 100)
                text_prgs.value = f"Запуск.. {progress:.2f}%"
                pbp = progress/100
                d_progress.value = pbp
                download.update()
                text_prgs.update()

        app_path = r"C:\TempL\start.exe"
        process = subprocess.Popen(app_path)
        page.window_close()
    
    def restart_update(e):
        p_text('🔄 Обновляется информация...')
        l_on = on_launcher_update()
        if l_on == 0:
            upd = asyncio.run(on_update())
            if upd == 0:
                d_content.clear()
                d_content.append(d_open)
                download.update()
            elif upd == 3:
                d_content.clear()
                d_content.append(d_con)
                download.update()
            else:
                d_content.clear()
                d_content.append(d_upd)
                download.update()
        else:
            d_content.clear()
            d_upd_launch.text = f"Обновить Лаунчер (v{new_version})"
            d_content.append(d_upd_launch)
            download.update()
        p_text('✅ Обновление завершенно')



        
        top_player = top1()
        top_skill_content.clear()
        creator1_content.clear()
        
        top1_skill = ft.Text(top_player['userName'])
        top1_skill_stars = ft.Text(top_player['stars'])
        top1_skill_icon_render = ft.Image(src=get_icons(top_player['userID']), height=40, width=40)

        top1_skill_column.controls.clear()
        top1_skill_column.controls.append(top1_skill)
        top1_skill_column.controls.append(ft.Row([
            ft.Image("https://gofruit.space/_next/static/media/star.29035264.png", height=15, width=15), top1_skill_stars], spacing=1))
        
        top_skill_content.append(top1_skill_icon_render)
        top_skill_content.append(top1_skill_column)

        top_creator = creator1()
        top1_creator = ft.Text(top_creator['userName'])
        top1_creator_point = ft.Text(top_creator['creatorpoints'])
        top1_creator_icon_render = ft.Image(src=get_icons(top_creator['userID']), height=40, width=40)

        creator1_column.controls.clear()
        creator1_column.controls.append(top1_creator)
        creator1_column.controls.append(ft.Row([
            ft.Image("https://gofruit.space/_next/static/media/cp.34939ca5.png", height=15, width=15), top1_creator_point], spacing=1))
        creator1_content.append(top1_creator_icon_render)
        creator1_content.append(creator1_column)
        
        top.update()

    
    
    def go_Main(e):
        page.controls.clear()
        page.auto_scroll = False
        page.scroll = False
        page.add(top_nav, MainPage)
        page.update()
        
    def go_Settings(e):
        page.controls.clear()
        page.add(uni_top_nav, SettingsPage)
        page.update()
        

    def news_test(news: ft.Page):
        news.add(ft.Image(avatar))
        news.title = topic
        news.add(ft.Text(description))


    gd_user = GD_User()
    
    if gd_user.if_login() == True:
        print(f"Пользователь: {gd_user.account.name}")



        
    uni_top_nav = ft.Row(
        [
            ft.IconButton(ft.icons.ARROW_BACK, on_click=go_Main),
            ft.WindowDragArea(ft.Container(ft.Text(f"Настройки", size=20), padding=10), expand=True),
            ft.IconButton(ft.icons.CLOSE, on_click=lambda _: page.window_close()),
            
        ]
    )
                
    top_nav = ft.Row(
        [
            ft.WindowDragArea(ft.Container(ft.Text(f"ReGDSLauncher v{version}", size=20), padding=10), expand=True),
            # ft.IconButton(ft.icons.REMOVE, on_click=close),
            # ft.IconButton(ft.icons.SETTINGS, on_click=go_Settings),
            ft.IconButton(ft.icons.RESTART_ALT, on_click=restart_update),
            ft.IconButton(ft.icons.CLOSE, on_click=lambda _: page.window_close()),
            
        ]
    )


    news = ft.Container(content=ft.Column([
        ft.Image(src=avatar, border_radius=8, scale=1),
        ft.Container(ft.Text(topic, scale=1.2), alignment=ft.alignment.center),
        ft.Text(""),
        ft.Container(ft.Text(description, selectable=True), margin=5)
        
        ], alignment=ft.alignment.top_center, spacing=1), height=350, width=229, bgcolor="#2F2F2F", border_radius=7, padding=10, on_click=news_view)
    

    gds = ft.Container(content=ft.Column([
        ft.Row([
        ft.Image(src="https://cdn.fruitspace.one/server_icons/gd_00kz.png", height=150, width=150, border_radius=9),
        ft.Column( [ ft.Text("ReGDS", size=30), ft.Container(ft.Text("By ReMeow", color=ft.colors.BLACK), bgcolor=ft.colors.WHITE, padding=5, border_radius=5) ], alignment=ft.alignment.center_left)
    ]),
    ft.Container(content=ft.Text(descript_launcher, selectable = True), width=601, height=165, border_radius=11, bgcolor="#252525", padding=15)
    ]), height=350, width=625, bgcolor="#2F2F2F", border_radius=7, padding=10)


    top1_skill_column = ft.Column([
                    ft.Text("Updating"),
                    ft.Row([ft.ProgressRing(height=10, width=10)], spacing=1)
                ], spacing=1)
    creator1_column = ft.Column([
                    ft.Text("Updating"),
                    ft.Row([ft.ProgressRing(height=10, width=10)], spacing=1)
                ], spacing=1)
    
    top1_skill_icon_render = ft.Row([ft.ProgressRing(height=40, width=40)], spacing=1)

    top1_creator_icon_render = ft.Row([ft.ProgressRing(height=40, width=40)], spacing=1)

    top_skill_content = []
    top_skill_content.append(top1_skill_icon_render)
    top_skill_content.append(top1_skill_column)
    top1_skill_row = ft.Row(top_skill_content)
    

    creator1_content = []
    creator1_content.append(top1_creator_icon_render)
    creator1_content.append(creator1_column)

    creator1_row = ft.Row(creator1_content)
    top = ft.Container(content=(
        ft.Column(
        [
            ft.Container(top1_skill_row, width=215, height=45, bgcolor="#555555", margin=5, padding=3, border_radius=4),


                ft.Container(creator1_row, width=215, height=45, bgcolor="#555555", margin=5, padding=3, border_radius=4)
        ], spacing=1)), width=229, height=115, border_radius=7, bgcolor="#2F2F2F", border=ft.border.all(1, ft.colors.BLUE_300))
    
    d_progress = ft.ProgressBar(width=625, value=0.5, animate_size=10, bar_height=70, color="#549FFF", bgcolor="#2f2f2f")
    d_con = ft.FilledButton(text="Скачать", width=600, height=40,on_click=download_regds)
    d_upd = ft.FilledButton(text="Обновить", width=600, height=40,on_click=download_regds)
    d_upd_launch = ft.FilledButton(text="Обновить Лаунчер", width=600, height=40,on_click=update_launcher)
    d_open = ft.FilledButton(text="Открыть", width=600, height=40, on_click=open_regds)
    d_check = ft.Row([ft.ProgressRing(height=40, width=40, stroke_width=5)], spacing=1, alignment=ft.MainAxisAlignment.CENTER)
    d_content = []
    d_content.append(d_check)
    text_prgs = ft.Text("", selectable=True)
    download = ft.Container(ft.Column(d_content), width=625, height=66, bgcolor="#2F2F2F", padding=15, alignment=ft.alignment.bottom_center, border_radius=7)
    MainPage = ft.Column([
        ft.Row([news, gds]),
        ft.Row([top,
                ft.Column([text_prgs, download]), 
                ])
        ])

    
    def settings_texture_on(e):
        changed = on_texture.value
        print(changed)
        if changed:
            textur_self.disabled = False
            
        else:
            textur_self.disabled = True
            textur_self.value = False
            upload_texture. disabled = True
        
        texture.update()

    def settings_self_texture(e):
        changed = textur_self.value
        if changed:
            upload_texture.disabled = False
        else:
            upload_texture.disabled = True
        texture.update()


    mhv6 = ft.Checkbox(label="MegaHack v6", value=False)
    gdhm = ft.Checkbox(label="GDHM + TASBOT", value=True)
    rh = ft.Checkbox(label="Rainix Hack", value=False)
    Hack = ft.Container(ft.RadioGroup(ft.Column([
        ft.Text("Читы"),
        mhv6,
        gdhm,
        rh

    ])), padding=10, bgcolor="#3e3e3e", width=300, height=170, border_radius=7)


    Mods = ft.Container(ft.Column([
        ft.Text("Моды"),
        ft.Checkbox(label="Custom Rate", value=True),
        ft.Checkbox(label="Main Levels Customizer", value=True, disabled=True),
        ft.Checkbox(label="Dev Panel", value=True),
        ft.Checkbox(label="Social Buttons", value=True),
        ft.Checkbox(label="Custom BG", value=True),
        ft.OutlinedButton("Открыть браузер модов (Скоро)", width=290, disabled=True)
    ]), padding=10, bgcolor="#3e3e3e", width=300, height=295, border_radius=7)

    on_texture = ft.Switch(label="Текстурпак", value=True, on_change=settings_texture_on)
    textur_self = ft.Checkbox(label="Свой текстурпак", value=False, on_change=settings_self_texture)
    upload_texture = ft.OutlinedButton("Загрузить свой", width=290, disabled=True)


    texture = ft.Container(ft.Column([
        ft.Text("Текстуры"),
        on_texture,
        textur_self,
        upload_texture
    ]), padding=10, bgcolor="#3e3e3e", width=300, height=200, border_radius=7)

    volume_texture_bottom = ft.Container(bgcolor=ft.colors.AMBER, height=260, width=300)

    settings_column1 = ft.Column([Hack, Mods])
    settings_column2 = ft.Column([texture, volume_texture_bottom])
    settings_row = ft.Row([settings_column1, settings_column2])

    SettingsPage = ft.Column([
        settings_row
    ])

    page.add(top_nav, MainPage)
    page.window_center()

    try:
        p_text("[LOG] Активность запустилась")
        #Запуск активности
        RPC.connect()
        RPC.update(
            details = DETAILS,
            state = STATE,
            large_image = LARGE_IMAGE,
            buttons = BUTTON
        )
    except:
        text_prgs.value = "Discord не найден"
        drpc = True
             
    restart_update("heh")

ft.app(main)