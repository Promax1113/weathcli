from rich.console import Console
import os

import keyboard, inquirer


console = Console(soft_wrap=True)
lat, lo = 10.00, 11.12
if not os.path.isfile(f"{os.getcwd()}/loc_cache/loc.tmp"):
    if not os.path.isdir(f"{os.getcwd()}/loc_cache/"):
        os.mkdir(f"{os.getcwd()}/loc_cache/")
    with open(f"{os.getcwd()}/loc_cache/loc.tmp", "w+") as f:
        f.write(str(lat)+"\n")
        f.write(str(lo))
city = 'Barcelona'

# Max, Min, Current, windspeed, wind dir, city

max_temp, min_temp, current_temp, windsp, wind_dir = 30, 20, 26, 10, 225

console.print(f'[bold]Weather in {city}(cached):', justify='center')
console.print(f"[red]Max temperature: {max_temp}°C")
console.print(f"[green]Current temperature: {current_temp}°C")
console.print(f"[blue]Min temperature: {min_temp}°C")

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