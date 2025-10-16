# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def print_star_names(targets):
    for star in targets:
        print(star)

print_star_names(targets)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_star_spectral_types(targets):
    for star, info in targets.items():
        print(f"{star}: {info['Spectral Type']}")

print_star_spectral_types(targets)

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def find_bright_stars(targets):
    bright_stars = []
    for star, info in targets.items():
        if info["Magnitude"] > 0.1:
            bright_stars.append(star)
    return bright_stars

find_bright_stars(targets)

# 4) Look up another target, add all the necessary information to the targets list. 
targets["Altair"] = {
    "RA": "19h 50m 47.0s",
    "Dec": "+08° 52′ 06″",
    "Magnitude": 0.77,
    "Spectral Type": "A7V"
}
print(targets)

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def declination_to_float(dec_str):
    sign = 1 if dec_str[0] == '+' else -1
    parts = dec_str[1:].replace('°', '').replace('′', '').replace('″', '').split()
    degrees = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    return sign * (degrees + minutes / 60 + seconds / 3600)

def find_brightest_near_20(targets):
    closest_star = None
    closest_diff = float('inf')
    best_magnitude = float('inf')
    
    for star, info in targets.items():
        dec_deg = declination_to_float(info["Dec"])
        diff = abs(dec_deg - 20)
        
        if diff < closest_diff or (diff == closest_diff and info["Magnitude"] < best_magnitude):
            closest_star = star
            closest_diff = diff
            best_magnitude = info["Magnitude"]
    return closest_star

print(find_brightest_near_20(targets))


# 6) What is your favorite constellation?
print("Orion")
