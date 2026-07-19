"""Generate the game's original, loopable cinematic score with no external samples.

The synthesis is intentionally deterministic so the repository owns the exact
masters and anyone can rebuild them with Python + NumPy.
"""

from __future__ import annotations

import math
import wave
from pathlib import Path

import numpy as np


SR = 22_050
BARS = 12


def note(midi: float) -> float:
    return 440.0 * (2.0 ** ((midi - 69.0) / 12.0))


def pan(signal: np.ndarray, position: float) -> np.ndarray:
    angle = (position + 1.0) * math.pi / 4.0
    return np.column_stack((signal * math.cos(angle), signal * math.sin(angle)))


def envelope(length: int, attack: float, release: float) -> np.ndarray:
    env = np.ones(length, dtype=np.float32)
    a = min(length, max(1, int(attack * SR)))
    r = min(length, max(1, int(release * SR)))
    env[:a] = np.linspace(0.0, 1.0, a, dtype=np.float32)
    env[-r:] *= np.linspace(1.0, 0.0, r, dtype=np.float32)
    return env


def tone(freq: float, duration: float, timbre: str = "strings") -> np.ndarray:
    count = max(1, int(duration * SR))
    t = np.arange(count, dtype=np.float32) / SR
    phase = 2.0 * math.pi * freq * t
    if timbre == "strings":
        result = np.sin(phase) + 0.31 * np.sin(phase * 2.0 + 0.2) + 0.13 * np.sin(phase * 3.0)
        result *= 0.69 + 0.05 * np.sin(2.0 * math.pi * 5.1 * t)
        return result * envelope(count, 0.18, 0.35)
    if timbre == "horn":
        result = np.sin(phase) + 0.46 * np.sin(phase * 2.0) + 0.19 * np.sin(phase * 3.0)
        return np.tanh(result * 0.8) * envelope(count, 0.12, 0.45)
    if timbre == "pluck":
        result = np.sin(phase) + 0.42 * np.sin(phase * 2.0) + 0.18 * np.sin(phase * 4.0)
        return result * np.exp(-t * 4.5) * envelope(count, 0.008, 0.06)
    result = np.sin(phase) + 0.2 * np.sin(phase * 0.5)
    return result * envelope(count, 0.02, 0.16)


def add_voice(track: np.ndarray, start: float, duration: float, midi: float, gain: float, timbre: str, stereo: float = 0.0) -> None:
    begin = int(start * SR)
    signal = tone(note(midi), duration, timbre) * gain
    end = min(len(track), begin + len(signal))
    if begin >= len(track) or end <= begin:
        return
    track[begin:end] += pan(signal[: end - begin], stereo)


def add_drum(track: np.ndarray, start: float, gain: float, seed: int, low: bool = True) -> None:
    rng = np.random.default_rng(seed)
    duration = 0.34 if low else 0.12
    count = int(duration * SR)
    t = np.arange(count, dtype=np.float32) / SR
    noise = rng.normal(0.0, 1.0, count).astype(np.float32)
    if low:
        body = np.sin(2.0 * math.pi * (72.0 - 35.0 * t) * t)
        signal = (body * 0.84 + noise * 0.12) * np.exp(-t * 10.0)
    else:
        signal = np.concatenate(([0.0], np.diff(noise))) * np.exp(-t * 31.0)
    begin = int(start * SR)
    end = min(len(track), begin + count)
    if end > begin:
        track[begin:end] += pan(signal[: end - begin] * gain, -0.12 if low else 0.22)


def reverb(track: np.ndarray, amount: float) -> np.ndarray:
    wet = track.copy()
    for delay, gain in ((0.11, 0.17), (0.19, 0.12), (0.31, 0.08), (0.47, 0.05)):
        samples = int(delay * SR)
        wet[samples:] += track[:-samples] * gain * amount
    return wet


def compose(name: str, bpm: int, progression: list[tuple[int, int, int]], melody: list[int], color: str) -> np.ndarray:
    beat = 60.0 / bpm
    bar = beat * 4.0
    duration = BARS * bar
    track = np.zeros((int(duration * SR), 2), dtype=np.float32)

    for bar_index in range(BARS):
        chord = progression[bar_index % len(progression)]
        start = bar_index * bar
        # Sustained low strings and a moving inner voice establish each district.
        for voice_index, midi in enumerate(chord):
            add_voice(track, start, bar * 1.03, midi, 0.075 if voice_index else 0.11, "strings", -0.42 + voice_index * 0.42)
            if voice_index == 0:
                add_voice(track, start, bar * 0.98, midi - 12, 0.08, "strings", -0.08)
        # Eight-note ostinato alternates chord tones without copying any existing score.
        for step in range(8):
            pitch = chord[(step * 2 + bar_index) % len(chord)] + (12 if step in (3, 6) else 0)
            add_voice(track, start + step * beat * 0.5, beat * 0.46, pitch, 0.075, "pluck", -0.48 + (step % 3) * 0.48)
        # Original recurring theme, phrased differently by district.
        for step, interval in enumerate(melody):
            pitch = chord[0] + 12 + interval
            instrument = "horn" if color in ("nereu", "cistern") and bar_index >= 4 else "strings"
            add_voice(track, start + step * beat * 0.5, beat * (0.88 if step % 2 == 0 else 0.46), pitch, 0.055, instrument, 0.24)
        add_drum(track, start, 0.15 if color != "cistern" else 0.10, bar_index * 7 + 1, True)
        add_drum(track, start + beat * 2.0, 0.11, bar_index * 7 + 2, True)
        for step in (1, 3, 5, 7):
            add_drum(track, start + step * beat * 0.5, 0.022 if color == "cistern" else 0.036, bar_index * 31 + step, False)

    # A quiet district-specific countermelody adds identity without overpowering dialogue.
    root = progression[0][0]
    countermelody = {
        "harbor": [0, 2, 5, 7, 5, 2],
        "agora": [0, 3, 2, 7, 5, 3],
        "nereu": [0, 1, 5, 8, 7, 5],
        "cistern": [0, 1, 6, 5, 1, -1],
    }[color]
    for bar_index in range(2, BARS, 3):
        for step, interval in enumerate(countermelody):
            add_voice(track, bar_index * bar + step * beat * 0.66, beat * 0.55, root + 24 + interval, 0.038, "pluck", 0.58)

    track = reverb(track, 0.85 if color in ("nereu", "cistern") else 0.58)
    # Crossfade the final half-second into the opening for a clean imported loop.
    fade = min(int(0.55 * SR), len(track) // 8)
    ramp = np.linspace(0.0, 1.0, fade, dtype=np.float32)[:, None]
    track[-fade:] = track[-fade:] * (1.0 - ramp) + track[:fade] * ramp
    peak = float(np.max(np.abs(track))) or 1.0
    return np.clip(track / peak * 0.82, -1.0, 1.0)


def write_wav(path: Path, audio: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pcm = (audio * 32767.0).astype("<i2")
    with wave.open(str(path), "wb") as handle:
        handle.setnchannels(2)
        handle.setsampwidth(2)
        handle.setframerate(SR)
        handle.writeframes(pcm.tobytes())


def main() -> None:
    output = Path(__file__).resolve().parents[1] / "assets" / "audio" / "original"
    pieces = [
        ("kallipolis_harbor.wav", 84, [(50, 53, 57), (48, 52, 55), (43, 50, 55), (50, 53, 57)], [0, 2, 5, 7, 5, 9, 7, 2], "harbor"),
        ("agora_of_columns.wav", 98, [(45, 48, 52), (46, 50, 53), (43, 47, 50), (45, 48, 52)], [0, 3, 7, 5, 3, 10, 7, 5], "agora"),
        ("nereu_blue_sails.wav", 72, [(52, 55, 59), (53, 57, 60), (48, 52, 55), (52, 55, 59)], [0, 1, 5, 8, 7, 5, 3, 1], "nereu"),
        ("cistern_forgotten_echoes.wav", 66, [(40, 41, 47), (38, 43, 46), (41, 46, 48), (40, 41, 47)], [0, 1, 6, 5, 1, 8, 6, -1], "cistern"),
    ]
    for filename, bpm, progression, melody, color in pieces:
        write_wav(output / filename, compose(filename, bpm, progression, melody, color))
        print(f"wrote {output / filename}")


if __name__ == "__main__":
    main()
