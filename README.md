# Quiz Application

This quiz application is for the NSE4 v7.2 certificate and presents a set of questions to the user, collects responses, and then displays the user's score. It reads questions from a CSV file, randomly selects 30 questions (out of a pool of 171 Knowledge Check questions), and shows a bar graph with the results, including category-wise percentages and a list of incorrect questions.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have a Windows machine.
* You have Python 3.8 or newer installed.

If you don't have Python installed, you can download it from the [Python official website](https://www.python.org/downloads/windows/). Look for the "Latest Python 3 Release" and download the executable installer.

1. Run the installer and make sure to check the "Add Python to PATH" option during installation.
2. Follow the rest of the prompts to install Python.

## Installation

To install the Quiz Application, follow these steps:

1. Clone the repository:

```git clone https://github.com/JohnnyNovacane/FortiGate-NSE4-v7.2-Quizzes.git```


2.	Navigate to the cloned repository:
```cd FortiGate-NSE4-v7.2-Quizzes```

3.	Install Flask, a web framework used by the application via CMD:
```pip install flask```

Usage
To use the Quiz Application:
1.	Start the Flask server by running:
```python Quiz.py```

2.	Open your web browser and navigate to ```http://127.0.0.1:5000/```

3.	Take the quiz and submit your answers to see your score and a breakdown of your results.


## Contributing to Quiz Application
To contribute to the Quiz Application, follow these steps:
1.	Fork this repository.
This creates a copy of the repository in your GitHub account.

2.	Clone your fork.
```git clone https://github.com/yourusername/FortiGate-NSE4-v7.2-Quizzes.git```

  Replace yourusername with your GitHub username.

3. Create a branch:
Navigate into the cloned repository: ```cd FortiGate-NSE4-v7.2-Quizzes```

Then create a new branch using: ```git checkout -b <branch_name>```
  Replace <branch_name> with a descriptive name for your branch.

4. Make your changes and commit them: ```git commit -am '<commit_message>'```

  Replace <commit_message> with a meaningful message that describes your changes.


5. Push to your fork: ```git push origin <branch_name>```
  This pushes your changes to your fork of the repository on GitHub.

6. Create the pull request:
  Go to your fork on GitHub, and you'll see a Compare & pull request button. Click on it to create a pull request for your changes.
  Alternatively, see the GitHub documentation on creating a pull request. [creating a pull request]([https://www.python.org/downloads/windows/](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request))

## Contributors
Thanks to the following people who have contributed to this project:
•	@JohnnyNovacane

## License

This project is licensed under the MIT License.

