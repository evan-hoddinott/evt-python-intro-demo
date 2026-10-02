# EVT Python completed instructor demo

This is the **completed answer**, recorded during the native VS Code and GitHub walkthrough. Students should begin with the [EVT starter template](https://github.com/KSU-Electric-Vehicle-Team/evt-python-intro), which intentionally has one calculation bug.

[Class PowerPoint and screenshot walkthrough](https://github.com/KSU-Electric-Vehicle-Team/evt-python-intro/releases/latest)

## Run the completed demo

1. Select **Code > HTTPS** and copy this repository’s clone URL.
2. In VS Code, run **Git: Clone**, paste the URL, select a parent folder, and open the clone.
3. Open **Terminal: Create New Terminal** from the Command Palette.
4. Run `python3 intro.py` on Linux/macOS, or `py -3 intro.py` on Windows. Expected: `Speed in km/h: 36.0`.
5. Run `python3 -m unittest -v` or `py -3 -m unittest -v`. Expected: **4 tests, OK**.

Python 3.11 or later and Git are sufficient. No third-party Python packages are needed. If your Python 3 command is `python`, use that prefix consistently.

## What changed during class

- `intro.py` imports and calls the conversion function with 10 m/s.
- `speed.py` multiplies by 3.6 instead of dividing.
- `test_speed.py` adds a 2.5 m/s to 9 km/h test.

The recorded classroom commit is [`c2683ee`](https://github.com/evan-hoddinott/evt-python-intro-demo/commit/c2683eeca144972e6b910485f57e9c2a2a77609e). Its [GitHub Actions run](https://github.com/evan-hoddinott/evt-python-intro-demo/actions/runs/37033875579) passed all four tests. The initial commit failed two tests by design.

All speeds are synthetic classroom examples, not recorded kart telemetry. This repository is a standalone teaching demo and does not control vehicle hardware.
