# Glossary

# Git

## Staging
- **Picture:** Putting items in a shipping box before sealing it.
- **In plain words:** Choosing which changes go into the next commit.
- **Used:** `git add requirements.txt`

## Commit
- **Picture:** Seals a shipping box and labels it.
- **In plain words:** Saves the added changes with a message of changes.
- **Used:** `git commit requirements.txt -m "Add requirements"`

## Status
- **In plain words:** Check for changes.
- **Used:** `git status`

## Diff
- **In plain words:** View changes.
- **Used:** `git diff`

## Log
- **In plain words:** List of saved points.
- **Used:** `git log --oneline`

## Push
- **In plain words:** Send changes to GitHub.
- **Used:** `git push`

## Clone
- **In plain words:** Copy a repository locally.
- **Used:** `git clone https://github.com/YOUR-USERNAME/api-test-practice.git`

# Python Environment

## Virtual Environment
- **In plain words:** A python project toolbox.
- **Used:** Create - python3 -m venv .venv
            Activate - `source .venv/bin/activate`

## pip
- **In plain words:** Handles python packages.
- **Used:** List All Packages - pip list
            Install Packages - pip install requests
            Write Packages - pip freeze > requirements.txt

## Dependency
- **Picture:** The recipe is your project, and the ingredients it can’t be made without
- **In plain words:** Items relying on other items.
- **Used:** Project uses requests (dependency), requests uses requirements.txt list (other dependencies)

# Python Data

## List
- **Picture:** []
- **In plain word:** A list of data or objects. A numbered shelf, items sit in order.You grab by position.
- **Used:** post[0] is a position, post[-1] starts from end

## Dict
- **Picture:** {}
- **In plain words:** A group of related keywords. A set of labeled drawers. Grab by label not position.
- **Used:** {"id": 1, "title": "Hello world", "userId": 1, "completed": False}

## JSON
- **In plain words:** A file with nested dictionaries and lists.
- **Used:** 
    One post, as an API would send it: a dict
    post = {
        "userId": 1,
        "id": 1,
        "title": "Hello world",
        "completed": False,
}

    Several posts: a list of dicts
    posts = [
        {"id": 1, "title": "First post", "userId": 1},
        {"id": 2, "title": "Second post", "userId": 1},
        {"id": 3, "title": "Third post", "userId": 2},
    ]
