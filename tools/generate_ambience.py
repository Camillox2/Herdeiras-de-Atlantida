"""Generate small original ambience loops for the Ren'Py build.

The sounds are intentionally unobtrusive layers: existing music remains the
melodic score, while these loops make locations feel occupied.
"""
from __future__ import annotations

import math
import random
import wave
from pathlib import Path


RATE = 22050
DURATION = 24
OUT = Path(__file__).resolve().parents[1] / "renpy" / "game" / "audio"


def clamp(value: float) -> int:
    return max(-32767, min(32767, int(value * 32767)))


def write_loop(name: str, sample) -> None:
    target = OUT / "ambience" / name
    target.parent.mkdir(parents=True, exist_ok=True)
    frames = bytearray()
    for index in range(RATE * DURATION):
        frames += clamp(sample(index / RATE)).to_bytes(2, "little", signed=True)
    with wave.open(str(target), "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(RATE)
        output.writeframes(bytes(frames))


def harbor(t: float) -> float:
    tide = 0.018 * math.sin(2 * math.pi * 0.14 * t)
    foam = random.uniform(-0.030, 0.030) * (0.5 + 0.5 * math.sin(2 * math.pi * 0.07 * t))
    bell = 0.012 * math.sin(2 * math.pi * 392 * t) * max(0, math.sin(2 * math.pi * 0.025 * t)) ** 14
    gull = 0.004 * math.sin(2 * math.pi * (880 + 120 * math.sin(t * 2)) * t) * max(0, math.sin(t * 0.33)) ** 22
    return tide + foam + bell + gull


def storm(t: float) -> float:
    gust = (0.02 + 0.035 * max(0, math.sin(2 * math.pi * 0.055 * t))) * random.uniform(-1, 1)
    rain = 0.020 * random.uniform(-1, 1)
    thunder = 0.025 * math.sin(2 * math.pi * 48 * t) * max(0, math.sin(2 * math.pi * 0.021 * t)) ** 40
    return gust + rain + thunder


def observatory(t: float) -> float:
    drone = 0.017 * math.sin(2 * math.pi * 55 * t) + 0.011 * math.sin(2 * math.pi * 82.5 * t)
    shimmer = 0.006 * math.sin(2 * math.pi * (330 + 20 * math.sin(t * 0.3)) * t)
    tick = 0.022 * math.sin(2 * math.pi * 1240 * t) * max(0, math.sin(2 * math.pi * 0.125 * t)) ** 55
    return drone + shimmer + tick


def chime(t: float) -> float:
    if t > 1.2:
        return 0.0
    envelope = math.exp(-3.8 * t)
    return envelope * (0.20 * math.sin(2 * math.pi * 660 * t) + 0.12 * math.sin(2 * math.pi * 990 * t))


def write_sfx() -> None:
    target = OUT / "sfx" / "moiras_chime.wav"
    target.parent.mkdir(parents=True, exist_ok=True)
    frames = bytearray()
    for index in range(int(RATE * 1.25)):
        frames += clamp(chime(index / RATE)).to_bytes(2, "little", signed=True)
    with wave.open(str(target), "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(RATE)
        output.writeframes(bytes(frames))


if __name__ == "__main__":
    random.seed(1964)
    write_loop("harbor_night.wav", harbor)
    write_loop("storm_city.wav", storm)
    write_loop("observatory_stars.wav", observatory)
    write_sfx()
