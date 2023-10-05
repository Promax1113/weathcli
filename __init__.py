from rich.console import Console
import os
from .API import get_location, weather_info
import keyboard, inquirer, json


console = Console(soft_wrap=True)
if not os.path.isfile(f"{os.getcwd()}/loc_cache/loc.tmp"):
    if os.path.getmtime(f"{os.getcwd()}/loc_cache/loc.tmp"):
    if not os.path.isdir(f"{os.getcwd()}/loc_cache/"):
        os.mkdir(f"{os.getcwd()}/loc_cache/")
    with open(f"{os.getcwd()}/loc_cache/loc.tmp", "w+") as f:
        f.write(json.dumps(loc))
if os.path.isfile:
    # WIP Caching system
    pass

# Max, Min, Current, windspeed, wind dir, city

w_info = weather_info()

console.print(f'[bold]Weather in {loc["city"]}(cached: {}):', justify='center')
console.print(f"[green]Current temperature: {w_info['current_weather']['temperature']}°C")

while True:
    if keyboard.is_pressed('q'):
        choices = ['Search for city', 'Your city', 'Exit']
        choice = inquirer.prompt([
            inquirer.List("main_menu",message='\nChoose from list', choices=choices)
        ])
        match choice['main_menu']:
            case 'Search for city':
                pass
            case 'Your city':
                pass
            case 'Exit':
                exit(0)