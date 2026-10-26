# Data protection exercise

In this exercise you will practice pseudonymization, anonymization, and masking in Python. By the end, you should be able to explain the difference between these concepts and implement them in code.

The project structure is
```
/
├── dataprotection/
│   ├── __init__.py
│   ├── pseudonymization.py   # TODOs
│   ├── anonymization.py      # TODOs
│   ├── masking.py            # TODOs
├── main.py
├── tests/
│   ├── test_pseudonymization.py
│   ├── test_anonymization.py
│   ├── test_masking.py
├── requirements.txt
└── README.md
```

## Instructions
1. Clone this repository.
2. Create and activate a virtual environment and install requirements

in [Visual Studio Code](https://code.visualstudio.com/docs/python/environments#_creating-environments), select the requirements.txt file when prompted for dependecies

OR

in cmd:
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

3. Open dataprotection files, instructions in the comments.

4. To test and run your code, just run the `main.py`. Make sure that you have the correct Python environment in use.

5. You can run the tests in the cmd in the project root with:
`pytest`

7. Commit and push your changes to this repository.

## Note

👉 In main.py, the `“if __name__ == "__main__":` makes sure code only runs when the file is executed directly, not when it’s imported for testing.
