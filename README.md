# The Madness Adventure

We are eager to introduce you with our **Madness Adventure Game** for our git workshop!

In this project you will collaborately build a small text-based adventure game using Python,
applying the git commands you learned.

---

## How the game works

The game is a simple, randomized, interactive story that only requires the terminal.

When the game starts:
  - The player is presented with a situation
  - They have to choose an option by typing in the terminal
  - The story unfolds based on their choice

The story is made up of small pieces of logic (functions and print statements) that are connected together.

### Run the game
To play the game, just execute the run file:

```python
python run.py
```

---

## Your mission

You will have to add new elements to the story

  - Create new story paths
  - Expand the existing ones
  - Add choices, characters, and outcomes

---

## How will we collaborate?

A simple workflow for including new features to the game

  - Create a branch (`feature/my_new_path`)
  - Work in your branch
  - Test that your version works properly
  - Create a pull-request to the `devel` branch

Similarly, you can fix bugs that you find in the game

  - Create a branch (`fix/issue_to_solve`)
  - Make the essential changes to fix the issue
  - Test the corrected version
  - Create a pull-request to the `devel` branch

Always keep the changes small and clear, writing meaningful and clear commit messages!

### Merge conflicts (part of collaborating)

Since we might encounter conflicts while collaborating, we should be able to properly fix them.

When you find a conflict in a story step you will have to decide on **how to combine them**.
Our method will consist in always try to merge the conflicting ideas, into a new funnier one!

### Handling the Pull Request

  - Describe properly what you added, keep it short but explain everything that might be necessary
  - Be aware of replies, questions and feedback
  - Make changes or improvements that may be requested by other developers
