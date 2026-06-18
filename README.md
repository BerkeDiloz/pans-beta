# mpl — example scripts and notebooks

This folder contains example Python scripts and Jupyter Notebooks used for plotting, simple utilities and demos. Below is a list of files, the language used, and a short description for each.

## Scripts (.py)
- basic_math.py — Python: simple arithmetic functions and example prints (add, multiply, divide).
- basic_math_dup.py — Python: duplicate of arithmetic examples.
- km_to_miles.py — Python: convert kilometers to miles (two formulas) and print results.
- cm_to_feet_inches.py — Python: convert cm to feet and inches.
- banknote_stack_value.py — Python: estimate number and value of banknotes in 1m stack.
- banknote_utils.py — Python: helper functions for banknote count and column value.
- quadrilateral_check.py — Python: check if four sides can form a quadrilateral (triangle-inequality-like check).
- city_scores_average.py — Python: compute average scores for two city sample lists.
- average_list.py, average_list_dup.py — Python: compute average of a list of numbers.
- random_numbers_demo.py — Python: demo generating & filtering random numbers (contains syntax to review).
- list_access_example.py — Python: simple list access example.
- range_iteration.py — Python: simple range/iteration demo (contains index usage to review).
- remove_chars.py — Python: function `remove_chars(word, n)` returning substring.
- remove_chars_demo.py — Python: calls to `remove_chars`.
- sort_names_demo.py — Python: sorting a list of names example.
- list_operations.py — Python: list append/pop demo.
- dice_roll.py, dice_roll_dup.py — Python: simple dice roll random choice examples.
- dice_game_average.py — Python: simulate N dice rolls and print average winner.
- password_generator.py — Python: generate random password from character list.
- print_alphabet.py — Python: print ASCII uppercase and lowercase letters.
- ord_turkish_chars.py — Python: print `ord()` of Turkish characters.
- count_letter_a.py — Python: count occurrences of letter 'a' in a string.
- swap_example.py — Python: example swap code (contains logic error to review).
- factorial.py — Python: compute factorial of a number.
- fruits_ops.py — Python: list operations using `fruits`.

## Notebooks (.ipynb)
- random_stats.ipynb — Jupyter Notebook (Python): generate random numbers and print stats.
- random_plots.ipynb — Jupyter Notebook (Python): three plotting examples of random data.
- temps_death_valley.ipynb — Jupyter Notebook (Python): plot max/min temps (reads remote CSV).
- lesson_difficulty_barchart.ipynb — Jupyter Notebook (Python): categorical bar chart demo.
- sine_cosine_plot.ipynb — Jupyter Notebook (Python): plot sine and cosine waves.
- monthly_budget_pie.ipynb — Jupyter Notebook (Python): pie chart of budget breakdown.
- parabola_plot.ipynb — Jupyter Notebook (Python): plot a parabola (matplotlib).
- penguin_attributes.ipynb, penguin_attributes_dup.ipynb — Jupyter Notebooks (Python): bar charts using penguin sample data.
- income_structure_groups.ipynb — Jupyter Notebook (Python): stacked bar chart example.
- random_bars_12.ipynb — Jupyter Notebook (Python): bar chart with 12 random values.
- gdp_sectors_pie.ipynb — Jupyter Notebook (Python): two pie charts (GDP and sectors).
- sales_data_pie.ipynb — Jupyter Notebook (Python): pie chart from CSV sales data.
- tourist_visits_by_country.ipynb — Jupyter Notebook (Python): bar chart reading `data.csv`.
- visited_bar_chart_cities.ipynb — Jupyter Notebook (Python): bar chart of visited counts.
- visited_countries_bar.ipynb — Jupyter Notebook (Python): bar chart of visited countries.
- fruit_supply_by_color.ipynb — Jupyter Notebook (Python): horizontal bar chart with colors.

---

How to add this `mpl` folder to your GitHub repository `https://github.com/BerkeDiloz/pans-beta` (PowerShell):

1. Clone the repo locally (if not already):

```powershell
git clone https://github.com/BerkeDiloz/pans-beta.git
cd pans-beta
```

2. Copy the `mpl` folder into the cloned repo and commit:

```powershell
# from your machine -- adjust path if different
robocopy "C:\Users\mberk\OneDrive\Desktop\mpl" .\mpl /E
git add mpl
git commit -m "Add mpl folder: scripts and notebooks with README"
git push origin main
```

Notes:
- You will need push access to `pans-beta` and valid Git credentials.
- If your default branch is not `main` use the repository's default branch name.
- I did not push to the remote (no credentials available here). If you want, I can generate a patch or prepare a zip of the `mpl` folder.

If you want, I can also:
- Add inline header comments to each `.py` file indicating language and description, or
- Try to commit & push directly from this environment if you provide a Git remote and credentials (not recommended to share secrets here).

