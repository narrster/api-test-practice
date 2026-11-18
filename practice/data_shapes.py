# One post, as an API would send it: a dict
post = {
    "userId": 1,
    "id": 1,
    "title": "Hello world",
    "completed": False,
}

# Several Posts: a list of dicts
posts = [
    {"id": 1, "title": "First Post", "userId": 1, "completed": False},
    {"id": 2, "title": "Second Post", "userId": 1},
    {"id": 3, "title": "Third Post", "userId": 2},
]

# Digging In
print(post["title"])    # grab one drawer
print(posts[0])          # first item on the shelf
print(posts[0]["title"]) # first item and its title
print(len(posts))       # how many items

# Looping through the shelf
for p in posts:
    print(p["id"], p["title"])

# Filtering post by user 1
user_one_posts = [p for p in posts if p["userId"] == 1]
print(len(user_one_posts))

# Print title of last post in posts
print(posts[-1]["title"])

# Print new key completed from First Post
print(posts[0]["completed"])

# Build a list of titles from posts
list_of_titles = []
for t in posts:
    list_of_titles.append(t["title"])
print(list_of_titles)
