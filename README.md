# 🚀 Kinematics Simulator — Phase 1

> **Part of an ongoing Physics Simulation Platform** | Built with Python

A modular, extensible kinematics engine that calculates and visualizes motion in real time. This is **Phase 1** of a larger physics simulation platform I'm building — focused on the core motion engine and animated trajectory visualization.

---

## 📌 What it does

- Calculates **displacement**, **average velocity**, and **average speed**
- Supports **multi-segment journeys** (forward & backward motion)
- Generates an **animated visualization** of the journey using matplotlib
- Clean modular architecture — physics core, simulation logic, and visualizer are all separate

---

## 🗂️ Project Structure
```
Kinematics-Simulator/
│
├── motion.py        # Physics core — Motion class, calculations
├── simulation.py    # Simulation engine — multi-segment journey handler
├── visualizer.py    # Animated trajectory visualizer (matplotlib)
└── requirements.txt
```

---

## ⚙️ Setup & Run
```bash
# Clone the repo
git clone https://github.com/Pragatisource08/Kinematics-Simulator.git
cd Kinematics-Simulator

# Install dependencies
pip install -r requirements.txt

# Run the simulation
python simulation.py
```

---

## 🧪 Example
```
How many parts does your journey have? 2
Enter the distance: 50
Enter the time: 10
Enter -1 for backward & +1 for forward: 1

Enter the distance: 20
Enter the time: 5
Enter -1 for backward & +1 for forward: -1

Average Velocity: 2.00 m/s
Average Speed: 4.67 m/s
```

---

## 🛣️ Roadmap

- [x] **Phase 1** — Kinematics core (displacement, velocity, speed, animation)
- [ ] **Phase 2** — Projectile motion & acceleration models
- [ ] **Phase 3** — GUI interface
- [ ] **Phase 4** — Dynamics, waves & more physics modules

---

## 🛠️ Built With

- Python 3
- Matplotlib
- NumPy

---

## 📄 License

MIT License — feel free to use and build on this.
