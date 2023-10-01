from rich.console import Console
import time
console = Console(soft_wrap=True)

# Max, Min, Current, windspeed, wind dir, city

city = 'Manresa'
max_temp, min_temp, current_temp, windsp, wind_dir = 30, 20, 26, 10, 225

console.print(f'[bold]Weather in {city}:', justify='center')
console.print(f"[red]Max temperature: {max_temp}°C")
console.print(f"[green]Current temperature: {current_temp}°C")
console.print(f"[blue]Min temperature: {min_temp}°C")
