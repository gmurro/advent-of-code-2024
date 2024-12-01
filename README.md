# Advent of Code 2024 Solutions

Solutions to the Advent of Code 2024 challenges in python

## Table of Contents
1. [Introduction](#introduction)
2. [Repository Structure](#repository-structure)
3. [Running the Solutions](#running-the-solutions)
4. [Explanation of Solution Structure](#explanation-of-solution-structure)
5. [License](#license)

## Introduction
This repository contains my solutions to the [Advent of Code 2024 challenges](https://adventofcode.com/2024). Each day's solutions are organized in separate folders, and each part of the challenge has its own Python script.

## Repository Structure
- `day_01/`: Contains the solutions for Day 1.
  - `input.txt`: Input file for the day.
  - `part_1/`: Folder for the first part of the challenge.
    - `solution.py`: Python script for the solution.
  - `part_2/`: Folder for the second part of the challenge.
    - `solution.py`: Python script for the solution.
- `day_02/`: ...
- ...
- `day_25/`: ...

## Running the Solutions
### 1. Getting Started

1. Clone the repository to your desired directory:

    ```bash
    cd <directory_in_which_repo_should_be_created>
    git clone https://github.com/gmurro/advent-of-code-2024.git
    cd advent-of-code-2024
    ```

2. Install `uv` for dependency management following the [official guide](https://docs.astral.sh/uv/getting-started/installation/).

3. (Optional) Install the project dependencies and set up pre-commit hooks:

    ```bash
    make install
    ```

### 2. Run python code
To run a solution, execute the Python script of the relative day. For example:
```bash
uv run python aoc/day_01/part_1/solution.py
```

## Explanation of Solution Structure
- Each solution script is written in Python.
- The `input.txt` file contains the input data for the puzzle of respective day.
- The solutions are designed to be modular and well-commented for clarity.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
