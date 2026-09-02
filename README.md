# Car Gear & Speed Simulator

A simple Python program that simulates a car's gearbox and speed behavior — starting the engine, shifting through gears 1–5, and applying brakes with a basic speed-limit safety check.

## Features
- Start/stop the car engine
- Shift through gears 1 to 5, each increasing speed
- Braking logic with a "safe" vs "dangerous" speed threshold
- Displays final speed in a simple report format

## How It Works
The `car_simulator` class models a car with:
- `start()` – turns the engine on
- `gear1()` to `gear5()` – shifts gears, increasing speed by 30 km/h each time
- `brake()` – slows the car down, warns if speed exceeds a safe limit
- `display_speed()` – prints a summary of the final speed

## Usage
```
python car_simulator.py
```

Example output:
car is started
car in first gear:0km/h
car in second gear:30km/h
car in third gear:60km/h
car in fourth gear:90km/h
Nice Going:90 km/h