from tqdm import tqdm
import time
from colorama import init,Fore
from faker import Faker
from random import choice
from datetime import date,datetime
import os
import requests
import webbrowser
from pathlib import Path

init(autoreset=True)

text = f"Hidlow{Fore.MAGENTA}OS"
print(text.center(70, " "))

desc_text = Fore.GREEN + "downloading"

for _ in tqdm(range(100), desc=desc_text, ncols=80):
    time.sleep(0.1)

print("Initialization", end='', flush=True)
time.sleep(0.3)
print(".", end='', flush=True)
time.sleep(0.5)
print(".", end='', flush=True)
time.sleep(0.4)
print(".", end='', flush=True)
time.sleep(0.2)
print(".")
time.sleep(1)

print(f"{Fore.GREEN}Initialization completed")

name = input("Enter your First name: ")
name1 = input("Enter your last name: ")

time1 = datetime.now().strftime("%H:%M:%S")
data = date.today()

time.sleep(0.5)
while True:
    lang_choice = input(f"Hello! {name} {name1}, choice language: ru/eng: ").lower()

    if lang_choice == "ru":

        print("Initialization", end='', flush=True)
        time.sleep(0.5)
        print(".", end='', flush=True)
        time.sleep(0.8)
        print(".", end='', flush=True)
        time.sleep(0.8)
        print(".", end='', flush=True)
        time.sleep(0.6)
        print(".")
        time.sleep(2)
        print("Download language..")
        time.sleep(3)
        print(Fore.GREEN + "Language download complete")
        time.sleep(0.3)
        print("Parsing language")
        time.sleep(1)
        print(Fore.GREEN + "Русский язык установлен!")
        input("Для продолжения нажмите Enter: ")
        print(f"Инициализация hidlow{Fore.MAGENTA}OS")
        time.sleep(2)
        print(Fore.CYAN + "Проверка сетевого подключения..")
        time.sleep(1.3)
        print(Fore.CYAN + "Сетевое подключение установлено.")
        time.sleep(0.7)
        print("Проверка драйверов...")
        time.sleep(4)
        print(Fore.GREEN + "Видеодрайверы [GPU]")
        time.sleep(1)
        print(Fore.GREEN + "Аудиодрайверы [звуковые карты]")
        time.sleep(1)
        print(Fore.GREEN + "Сетевые драйверы [Ethernet, Wi-Fi]")
        time.sleep(1)
        print(Fore.RED + "чипсетные драйверы [Motherboard]")
        time.sleep(1.3)
        print("инициализация загрузки", end='', flush=True)
        time.sleep(1)
        print(".", end='', flush=True)
        time.sleep(0.5)
        print(".", end='', flush=True)
        time.sleep(0.8)
        print(".", end='', flush=True)
        time.sleep(0.7)
        print(".")


        desc_text1 = Fore.WHITE + "downloading"

        for _ in tqdm(range(25), desc=desc_text1, ncols=50):
            time.sleep(0.1)

        print(f"Чипсетный драйвер {Fore.GREEN}установлен!")
        time.sleep(0.5)
        print(Fore.GREEN + "Драйверы устройств ввода [keyboard, mouse]")
        time.sleep(1)
        print(Fore.GREEN + "Драйвера накопители [HDD, SSD, RAID]")
        time.sleep(2)

        print(f"Проверка прошла{Fore.GREEN} успешно!")
        time.sleep(1)


        print(f"Установка display.service..")
        time.sleep(3)
        print("System startup...")
        time.sleep(0.5)
        print(data, end='', flush=True)
        time2 = Fore.CYAN + time1

        print(time2.center(20, " "))

        print(f"Новое уведомление!: {Fore.GREEN}отчет о системе готов!")
        while True:
            msg_sys = input("просмотреть? (y/n): ")
            if msg_sys == "y":
                html_path = Path(__file__).parent / "index1.html"
                webbrowser.open_new_tab(html_path.resolve().as_uri())

                break
            elif msg_sys == "n":
                print("сообщение скрыто.")
                break
            else:
                print("сообщение скрыто.")
                break

        time.sleep(3)

        fake = Faker('Ru_ru')

        while True:
            print("""
        1 - калькулятор🌐     2 - проводник🌐     3 - faker🌐

        4 - paint🌐           5 - блокнот🌐       6 - btc🌐    
        """)
            exe_fl = input("> ")
            if exe_fl == "1":
                os.system("calc")

            elif exe_fl == "2":
                os.system("explorer")

            elif exe_fl == "4":
                os.system("mspaint")

            elif exe_fl == "3":
                print(f"""{Fore.RED}
                > Имя: {fake.first_name()}
                > Фамилия: {fake.last_name()}
                > Адрес: {fake.address()}
                > Тел: {fake.phone_number()}
                > Почта: {fake.email()}
                > Снилс: {fake.ssn()}
                > Пароль: {fake.password()}
                """)
            elif exe_fl == "5":
                os.system("notepad")
            elif exe_fl == "6":
                url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,rub"
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                    btc_usd = data["bitcoin"]["usd"]
                    btc_rub = data["bitcoin"]["rub"]

                    print(f"Курс BTC/RUB: ₽{Fore.GREEN}{btc_rub}")
                    print(f"Курс BTC/USD: ${Fore.GREEN}{btc_usd}")

            else:
                print("выберите из доступных приложений: ")
        break

    elif lang_choice == "eng":
        print(Fore.GREEN + "english language Already installed")
        input("Press Enter to continue: ")
        print(f"Initialization hidlow{Fore.MAGENTA}OS")
        time.sleep(2)
        print(Fore.CYAN + "Network connection check..")
        time.sleep(1.3)
        print(Fore.CYAN + "Network connection established")
        time.sleep(0.7)
        print("checking drivers...")
        time.sleep(4)
        print(Fore.GREEN + "Graphics drivers [GPU]")
        time.sleep(1)
        print(Fore.GREEN + "Audio drivers [sound cards]")
        time.sleep(1)
        print(Fore.GREEN + "Network drivers [Ethernet, Wi-Fi]")
        time.sleep(1)
        print(Fore.RED + "Chipset drivers [Motherboard]")
        time.sleep(1.3)
        print("Initialization of loading", end='', flush=True)
        time.sleep(1)
        print(".", end='', flush=True)
        time.sleep(0.5)
        print(".", end='', flush=True)
        time.sleep(0.8)
        print(".", end='', flush=True)
        time.sleep(0.7)
        print(".")

        desc_text1 = Fore.WHITE + "downloading"

        for _ in tqdm(range(25), desc=desc_text1, ncols=50):
            time.sleep(0.1)

        print(f"Chipset driver{Fore.GREEN} installed!")
        time.sleep(0.5)
        print(Fore.GREEN + "Input device drivers [keyboard, mouse]")
        time.sleep(1)
        print(Fore.GREEN + "Storage drivers [HDD, SSD, RAID]")
        time.sleep(2)

        print(f"Check completed{Fore.GREEN} successfully!")
        time.sleep(1)

        print(f"Installing display.service..")
        time.sleep(3)
        print("System startup...")
        time.sleep(0.5)

        print(f"""
{name} {name1}, please wait, the device is preparing to start..
        """)

        time.sleep(3)
        print(data, end='', flush=True)
        time2 = Fore.CYAN + time1

        print(time2.center(20, " "))

        print(f"New message!: {Fore.GREEN}System report is ready!")
        while True:
            msg_sys = input("show? (y/n): ")
            if msg_sys == "y":
                html_path = Path(__file__).parent / "index2.html"
                webbrowser.open_new_tab(html_path.resolve().as_uri())

                break
            elif msg_sys == "n":
                print("Message hidden.")
                break
            else:
                print("Message hidden.")
                break

        time.sleep(3)

        fake = Faker()

        while True:
            print("""
               1 - calculator🌐     2 - explorer🌐     3 - faker🌐

               4 - paint🌐           5 - notepad🌐       6 - btc🌐    
               """)
            exe_fl = input("> ")
            if exe_fl == "1":
                os.system("calc")

            elif exe_fl == "2":
                os.system("explorer")

            elif exe_fl == "4":
                os.system("mspaint")

            elif exe_fl == "3":
                print(f"""{Fore.RED}
                       > F.Name: {fake.first_name()}
                       > L.name: {fake.last_name()}
                       > address: {fake.address()}
                       > phone number: {fake.phone_number()}
                       > email: {fake.email()}
                       > SSN: {fake.ssn()}
                       > password: {fake.password()}
                       """)
            elif exe_fl == "5":
                os.system("notepad")
            elif exe_fl == "6":
                url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,rub"
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                    btc_usd = data["bitcoin"]["usd"]
                    btc_rub = data["bitcoin"]["rub"]

                    print(f"Курс BTC/RUB: ₽{Fore.GREEN}{btc_rub}")
                    print(f"Курс BTC/USD: ${Fore.GREEN}{btc_usd}")

            else:
                print("Choose from available applications: ")
        break
    else:
        print("Invalid choice (ru/eng)")
