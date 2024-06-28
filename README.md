# 🎭 Theatrical Player Refactoring Kata 🎭

[![Python](https://img.shields.io/badge/Python-3.12+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)

## Resources

These instructions where extracted from Emily Bache GitHub. The link to the original instructions can be found in the link bellow.

[![Web](https://img.shields.io/badge/GitHub-Emily_Bache-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/emilybache/Theatrical-Players-Refactoring-Kata)

## Description

This is exercise is the starting point of an exercise extracted from the book "Refactoring" by Martin Fowler. 

The code is a program fo calculating the customer statement for a troop of theatrical players. If you go to see a play you can earn volume
credits that gives you discounts on future plays.

The idea of the kata is to go through the code and refactor it step by step to improve readability and maintainability. Originally, the exercise
in the book didn't have tests, but in this version we are working with [python approval testing library](https://github.com/approvals/ApprovalTests.Python).

There are some test data:
- plays.json: contains the plays that the troop can perform
- invoice.json: contains details recent performances with information about the play and the audience
- new_plays.json: contains new plays that the program do not support
- invoice_new_plays.json: 

## Objective

The main objective is to:
- Practice refactoring legacy code
- Identify code smells
- Try to apply object calisthenics

## Configuration

The project can be configured with `pdm`.

1. Install pdm:
    ```bash
    pip install pdm
    ```
2. Install required python version:
    ```bash
    pdm python install 3.12
    ```
3. Create a virtual environment and install dependencies:
    ```bash
    pdm install
    ```
   It will create the .venv folder inside the project automatically.
4. You can activate the virtual environment manually running `source .venv/bin/activate` on Unix systems or `source .venv/Scripts/activate` on Windows.

## Running the tests

To run the tests, execute one of the following commands:

```bash
pytest
```

or

```bash
pdm run pytest
```

## Learnings

### Visit my GitHub profile to see all solved katas 🚀

[![Web](https://img.shields.io/badge/GitHub-Dimanu.py-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/dimanu-py/code-katas)
