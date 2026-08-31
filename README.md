# Growing Code — Python 0 (42 Barcelona)

*This repo was made by Adrian Fittipaldi (adrifitt / 42user)*

First Python project of 42's new Common Core. The goal is to discover Python's fundamental syntax and semantics — expressions, variables, functions, and control flow — by analyzing community garden data.

In this first project we only write one function per exercise, not a full program — it's just the introduction to Python, so the focus is on basic syntax, not on structuring a whole program.

## Project rules

- Your functions must be written in Python 3.10+.
- Your code must respect the flake8 linter standards.
- Each exercise must be in its own file.
- Each file should contain only the requested function.
- Function names must match exactly what is requested.
- You don't need to handle input validation or error cases unless explicitly mentioned.
- For negative numbers or invalid inputs, the behaviour is undefined (you don't need to handle these cases).
- Type hints are optional but recommended for learning purposes in exercises 0 to 6. They are required for exercise 7.

## Stack

- Python 3.10+
- flake8 (linter required by the project)
- mypy (type hint checking, required in exercise 7)

## How to run and test

```bash
git clone git@github.com:Adfitt/42cursus-Python0.git
cd 42cursus-Python0
```

Each function can be tested two ways:

1. With the `main.py` helper provided by 42 (imports and runs the functions automatically):
   ```bash
   # copy main.py (subject's helper) into the exercise folder you want to test
   python3 main.py
   ```

2. Manually, from the interpreter or in one line:
   ```bash
   python3 -c "from ft_hello_garden import ft_hello_garden; ft_hello_garden()"
   ```

Style and typing check (mandatory before submitting):
```bash
flake8 ex0/ft_hello_garden.py
```

`flake8` checks that the code follows the PEP8 standard (lines too long, extra whitespace, unused imports, etc). It doesn't run the function, it just reads the file. If everything is fine, it prints nothing; if there's an issue, it shows the file, the line, and the error code, for example:

```
ft_hello_garden.py:5:80: E501 line too long (85 > 79 characters)
```

```bash
mypy ex7/ft_seed_inventory.py
```

`mypy` does the same but for type hints: it checks that the declared types (`str`, `int`, `-> None`) match what the function actually uses. It only applies to ex7, since that's where the subject requires typing. If there's a mismatch, it shows something like:

```
ft_seed_inventory.py:3: error: Argument "quantity" has incompatible type "str"; expected "int"
```

Both are mandatory because the subject explicitly requires respecting the flake8 linter, and in ex7 it requires validating typing with mypy — it's not optional, it's part of the submission requirements.

## Project structure

**ex0 / ft_hello_garden.py**
Prints a fixed welcome message. No input.

**ex1 / ft_garden_name.py**
Asks for a garden name and displays it along with a fixed status message ("Status: Growing well!").

**ex2 / ft_plot_area.py**
Asks for length and width of a plot and calculates the area (length × width).

**ex3 / ft_harvest_total.py**
Asks for the harvest of 3 different days and calculates the total.

**ex4 / ft_plant_age.py**
Asks for a plant's age in days. If it's more than 60, it indicates the plant is ready to harvest; otherwise, that it needs more time.

**ex5 / ft_water_reminder.py**
Asks for the days since the last watering. If it's more than 2, it warns to water the plants; otherwise, that the plants are fine.

**ex6 / ft_count_harvest_iterative.py, ft_count_harvest_recursive.py**
Two versions (iterative and recursive) of the same function: they count from day 1 up to a given number, printing each day, and end with "Harvest time!". Both must produce identical output.

**ex7 / ft_seed_inventory.py**
First exercise with mandatory type hints. Receives seed type, quantity, and unit, and displays the info formatted according to the unit:
- "packets" → number of packets available
- "grams" → total in grams
- "area" → square meters covered
- any other unit → "Unknown unit type"
