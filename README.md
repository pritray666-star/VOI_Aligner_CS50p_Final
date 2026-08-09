# VOI Volume Aligner — CS50P Final Project

#### Video Demo: <https://youtu.be/T9S8eN9aeX4>

## Description

This is my final project for CS50's Introduction to Programming with Python.
It's a restructured, test-covered version of a tool I originally built and
deployed for MS MRI research in Dr. Bagnato's neuroimaging lab at Vanderbilt
(the live version my lab actually uses is here:
[voi-volume-aligner](https://github.com/pritray666-star/voi-volume-aligner)).

The tool aligns user VOI volumes (imported from MIPAV) into the correct
order based on Baseline reference cell positions, for every sheet/subject in
an Excel workbook. Before this tool existed, this reorganization was done
entirely by hand, subject by subject — this replaces that manual process
with a single script run.

## How it works

For each sheet (subject) in the input workbook, the tool:

- Reads the Baseline column (column B) to determine the correct order.
- Reads the user's VOI titles/volumes (columns D and E).
- Matches each VOI to its Baseline position by the leading number in its
  name (e.g. `"8_PR"` matches Baseline entry `8`).
- Writes the aligned titles and volumes into columns G and H, in Baseline
  order.
- Marks any VOI without a matching Baseline number as `N/V`.
- Appends any new VOI numbers not present in the Baseline after the last
  existing row.

## Files

- **`project.py`** — contains `main` and five additional functions:
  - `extract_leading_number(value)` — pulls the leading number out of a VOI
    name (e.g. `"18_adjusYR1_PR"` → `18`).
  - `parse_baseline_column(sheet, first_row, last_row)` — reads the Baseline
    column into an ordered list.
  - `parse_user_column(sheet, first_row, last_row)` — reads the user's VOI
    titles/volumes into a dictionary keyed by extracted number.
  - `align_voi_data(baseline, user_extracted)` — matches user VOIs to
    Baseline order, filling unmatched positions with `"N/V"`.
  - `find_new_entries(user_extracted, used_numbers)` — finds VOIs with no
    matching Baseline number.
  - `write_results(...)` — writes the aligned and new VOI data back into the
    worksheet.
  - `main(input_path, output_path)` — loads the workbook, runs the above for
    every sheet, and saves the result.
- **`test_project.py`** — pytest tests for `extract_leading_number`,
  `align_voi_data`, and `find_new_entries`.
- **`requirements.txt`** — lists `openpyxl` and `pytest`.
- **`CS50p_VOI_template.xlsx`** — example input file showing the expected
  format.

## Design choices

The original version of this tool had all of this logic inside a single
`main()` function. For this project I split it into five smaller functions,
each handling one step of the pipeline (reading the baseline, reading the
user data, aligning them, finding leftovers, writing output). This made the
logic much easier to test in isolation — `align_voi_data` and
`find_new_entries` in particular are pure functions that take plain lists
and dictionaries and return plain lists and dictionaries, so they can be
tested without needing a real Excel file at all.

## How to run it
\```
pip install -r requirements.txt
python project.py
\```

By default this reads `CS50p_VOI_template.xlsx` and writes
`CS50p_VOI_output.xlsx`.

## How to run the tests

\```
pytest test_project.py
\```