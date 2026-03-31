
# 🚀 Kinematics Simulator

A Python-based kinematics simulator that models multi-segment 1D motion and produces live animated visualizations of an object's journey — complete with real-time plots for displacement, distance, velocity, and speed.

---

## 📖 Overview

Kinematics Simulator lets you define a journey in multiple segments (each with its own distance, direction, and duration), computes the core physics quantities, and then animates the entire trip using **Matplotlib**. It is a great tool for physics students, educators, or anyone who wants to visualize 1D motion concepts interactively.

---s

## ✨ Features

- **Multi-segment journey support** — break any trip into as many legs as needed, each with independent distance, time, and direction
- **Physics calculations** — computes displacement, distance, average velocity, and average speed for the full journey
- **Live animation** — animates a moving dot along a number line in real time
- **Five simultaneous plots** — Object Motion, Displacement vs Time, Distance vs Time, Velocity vs Time, Speed vs Time
- **Real-time stats overlay** — displays current time, position, instantaneous velocity, running averages, and flags when the object returns near the origin
- **Pause / Play control** — interactive button to freeze and resume the animation
- **Dark-themed UI** — clean black-background charts with white axes for clarity

---

## 🗂️ Project Structure

```
Kinematics-Simulator/
│
├── motion.py          # Core physics class (Motion) — displacement, velocity, speed calculations
├── simulation.py      # Simulation orchestrator — collects user input, builds segments, runs the sim
├── visualizer.py      # Matplotlib animation engine — renders all plots and the interactive UI
├── requirements.txt   # Python dependencies
└── LICENSE            # MIT License
```

### Module Responsibilities

| File | Role |
|------|------|
| `motion.py` | Defines the `Motion` class with methods for `get_displacement()`, `get_delta_time()`, `get_average_velocity()`, `get_average_speed()`, and `summary()`. Can also be run standalone for single-segment calculations. |
| `simulation.py` | Defines the `Simulation` class to accumulate journey segments. Handles user input, computes totals, creates a `Motion` object from the aggregated data, and calls the visualizer. |
| `visualizer.py` | Implements `animate_journey()` using `FuncAnimation`. Builds a 3×2 grid of subplots, tracks position/distance/velocity/speed across 100 time steps, and renders the Pause/Play button. |

---

## ⚙️ Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`:

```
matplotlib==3.10.8
numpy==2.4.3
pillow==12.1.1
```

> All other entries in `requirements.txt` are transitive dependencies of matplotlib.

---

## 🛠️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/Pragatisource08/Kinematics-Simulator.git
cd Kinematics-Simulator
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the main simulation script:

```bash
python simulation.py
```

You will be prompted interactively:

```
How many parts does your journey have ? 3

Enter the distance: 50
Enter the time: 10
Enter -1 for backward direction & +1 for forward direction: 1

Enter the distance: 30
Enter the time: 5
Enter -1 for backward direction & +1 for forward direction: -1

Enter the distance: 20
Enter the time: 8
Enter -1 for backward direction & +1 for forward direction: 1
```

After entering all segments, the terminal prints a summary:

```
Average Velocity: 1.74 m/s
Average Speed: 4.35 m/s
```

…and a Matplotlib window opens with the full animated simulation.

### Standalone Mode (Single Segment)

`motion.py` can also be run on its own for quick single-segment calculations:

```bash
python motion.py
```

---

## 🎬 Animation Controls

| Control | Action |
|---------|--------|
| **Pause** button | Freezes the animation |
| **Play** button | Resumes the animation |

The stats bar at the bottom of the window updates every frame, showing:
- Current time (s)
- Current position (m)
- Instantaneous velocity (m/s)
- Running average velocity and speed
- A ⚡ flag when the object returns near its starting position

---

## 📐 Physics Reference

| Quantity | Formula |
|----------|---------|
| Displacement | `Δx = x_final − x_initial` |
| Average Velocity | `v_avg = Δx / Δt` |
| Average Speed | `s_avg = total distance / total time` |

Direction convention: **+1** = forward, **−1** = backward.

---



## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Pragati** — [@Pragatisource08](https://github.com/Pragatisource08)
