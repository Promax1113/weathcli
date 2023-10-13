import os

import json
import keyboard
import time
from rich.console import Console

from .API import get_location, weather_info

is_cached = False
console = Console(soft_wrap=True)
if not os.path.isfile(f"{os.getcwd()}/loc_cache/loc.tmp"):
    if not os.path.isdir(f"{os.getcwd()}/loc_cache/"):
        os.mkdir(f"{os.getcwd()}/loc_cache/")
    coords = get_location()
    with open(f"{os.getcwd()}/loc_cache/loc.tmp", "w") as f:
        f.write(json.dumps(coords))
        city = coords['city']
        w_info = weather_info(coords)
else:
    if os.path.getmtime(f"{os.getcwd()}/loc_cache/loc.tmp") + 10000 < time.time():

        coords = get_location()
        with open(f"{os.getcwd()}/loc_cache/loc.tmp", 'w') as f:
            f.write(json.dumps(coords))
            w_info = weather_info(coords)
    else:
        with open(f"{os.getcwd()}/loc_cache/loc.tmp") as f:
            data = f.readline()
            city = json.loads(data)['city']
            w_info = weather_info(json.loads(data))
            is_cached = True

# Max, Min, Current, windspeed, wind dir, city


console.print(f'[bold]Weather in {city} (cached: {is_cached}):\n')
console.print(f"[green]Current temperature: {w_info['current_weather']['temperature']}°C")
console.print(f"[red]Max temperature: {max(w_info['hourly']['temperature_2m'])}°C")
console.print(f"[blue]Min temperature: {min(w_info['hourly']['temperature_2m'])}°C")

