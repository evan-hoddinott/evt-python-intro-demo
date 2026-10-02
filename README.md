# EVT intro to Python

A small follow-along exercise: run a script, change a value, fix a speed
conversion, and test it. Allow about 45 minutes, with Python, Git, VS Code,
and GitHub sign-in already set up. There are no extra Python packages to install.
All speeds in this lesson are made-up examples.

## 1. Make your class repository and open it in VS Code

1. On this repository's GitHub page, choose **Use this template > Create a new repository**.
2. Select your personal account as Owner. Name it `evt-python-intro` and choose Public.
3. Leave **Include all branches** off. Select **Create repository**.
4. In your new repository, select **Code > Local > HTTPS** and copy the URL.
5. Open VS Code. Open the Command Palette with `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`).
6. Run **Git: Clone**, paste your repository URL, and press Enter.
7. Choose a parent folder you can find again, such as Documents. Select **Select Repository Location**.
8. When cloning finishes, choose **Open**. If prompted, trust this known classroom repository.
9. Open **Terminal > New Terminal**.

Use `python --version` on Windows or `python3 --version` on macOS/Linux.
Use Python 3.11 or newer. The commands below use `python`; substitute `python3`
if that is your working command. No extra packages are needed.

The starter deliberately contains a bug. Its first GitHub Actions run may fail:
that is expected. Your finished version should pass four tests.

No GitHub access yet? Download the student ZIP, extract it, and open the folder
containing `intro.py` in VS Code. You can complete all Python steps locally.

## 2. Run and change a script

Run:

```sh
python intro.py
```

Expected output:

```text
EVT
10
```

In `intro.py`, change `speed_mps = 10` to `speed_mps = 5`, save, and run again.
The second line should now be `5`.

`team` holds text (a string). `speed_mps` holds a number. `print()` shows a value.
The `mps` in the name tells us the unit: metres per second.

## 3. Calculate a speed

Add these lines at the end of `intro.py`:

```python
speed_kmh = speed_mps * 3.6
print("Speed in km/h:", speed_kmh)
```

Save and run. With `speed_mps = 5`, the final line should be:

```text
Speed in km/h: 18.0
```

Python uses `*` for multiplication and `/` for division.
One metre per second is 3.6 kilometres per hour.

## 4. Use a function

Open `speed.py`. A function names a calculation so we can reuse it:
`def` defines the function, `speed_mps` is its input, and `return` gives back
its result. Keep four spaces before the `return` line. The starting formula
contains an intentional bug.

Replace the contents of `intro.py` with:

```python
from speed import to_kmh

speed_mps = 10
speed_kmh = to_kmh(speed_mps)
print("Speed in km/h:", speed_kmh)
```

Save both files and run `python intro.py`. The result is about 2.78, but
10 m/s should be 36 km/h. We will use tests to find and fix this.

## 5. Run the tests, then fix the bug

From the same folder, run:

```sh
python -m unittest -v
```

Expect **3 tests and 2 failures** before the fix. The zero-speed test passes
because both multiplying and dividing zero give zero.

In `speed.py`, fix the calculation. Keep the function name and its input.
Save and rerun the tests. You should see **3 tests, OK**.
Run `python intro.py` again; it should print `Speed in km/h: 36.0`.

## 6. Add one test

Inside `class SpeedTests`, add this method below the existing methods:

```python
    def test_fractional_speed(self):
        self.assertAlmostEqual(to_kmh(2.5), 9)
```

Use four spaces before `def` and eight before `self`. `assertAlmostEqual`
compares decimal results while allowing tiny floating-point rounding differences.
You do not need to learn classes today; follow the supplied test pattern.

Run `python -m unittest -v`. Expect **4 tests, OK**.
Do not change the expected numbers in the existing tests to make the bug pass.

## 7. Commit and push your work

If you followed the template-and-clone steps above:

1. In VS Code, open **Source Control** (`Ctrl+Shift+G`; macOS: `Ctrl+Shift+G`).
2. Select each changed Python file to review the diff.
3. Stage `intro.py`, `speed.py`, and `test_speed.py` with the **+** beside each file.
4. Enter `Complete Python speed exercise` in the message box and select **Commit**.
5. Select **Sync Changes** or use the **Git: Push** command. Confirm the sync if asked.
6. Open your personal repository on GitHub. Select **Actions > Python practice**.
7. Open the newest run, then **test > Run the Python exercise tests**.
8. Confirm four tests ran and passed. Share your repository link with the instructor.

If you started from the ZIP, use **Source Control > Initialize Repository**, stage
all supplied lesson files including `.github/workflows/python.yml`, commit, and
run **Publish to GitHub** from the Command Palette. Publish a public repository
under your personal account. Do not initialize a second repository inside an
existing clone.

If Actions are disabled, enable them and use **Run workflow**. The workflow is
provided; students do not need to write YAML. The instructor's completed example
is at [evt-python-intro-demo](https://github.com/evan-hoddinott/evt-python-intro-demo).
Try the exercise before looking at the answer.

## Finished when

- Your script prints `Speed in km/h: 36.0` for `speed_mps = 10`.
- All four tests pass locally.
- Your latest GitHub Actions run passes.
- You can explain the input, return value, and why `/` was wrong.

## Common problems

| Problem | What to check |
| --- | --- |
| `python` not found | Try `python3` on macOS/Linux or check your Python installation. |
| Cannot open `intro.py` | Open a terminal in the extracted folder containing that file. |
| `ModuleNotFoundError: speed` | Keep `intro.py`, `speed.py`, and the tests together. |
| `IndentationError` | Use four spaces inside a function; do not mix tabs and spaces. |
| `SyntaxError` | Check quotes, parentheses, and the colon after the function definition. |
| Old output after a change | Save the file, then run it again. |
| Tests still fail | Read the named test and compare actual and expected values. |
| No Actions run | Confirm `.github/workflows/python.yml` reached GitHub. |
| GitHub fails but local passes | Save, commit, and push the latest files; check the newest run. |

## Optional: make a decision

After finishing, add this below the print in `intro.py`:

```python
if speed_kmh > 20:
    print("Above our practice threshold")
else:
    print("At or below our practice threshold")
```

Try inputs of 5 and 10 m/s. The 20 km/h threshold is only for this exercise;
it is not a vehicle operating limit.
