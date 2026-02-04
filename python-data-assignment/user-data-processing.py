# Part 4: User Data Processing System

def calculate_average_scores(users):
    """
    Accepts the list of users.
    Iterates through each user.
    Calculates the average score for each user.
    Returns a dictionary mapping user names to their average score.
    """
    averages = {}
    for user in users:
        scores = user.get('scores', [])
        if scores:
            avg = sum(scores) / len(scores)
        else:
            avg = 0
        averages[user['name']] = avg
    return averages

def has_admin_access(roles):
    """
    Accepts a user's roles (set).
    Returns True if the user has 'admin' access, otherwise False.
    """
    return "admin" in roles

def main():
    # Example users (can be replaced with input logic if needed)
    users = [
        {
            "name": "Alice",
            "scores": [90, 75, 80, 85],
            "roles": {"editor", "admin"}
        },
        {
            "name": "Bob",
            "scores": [60, 70, 65, 55],
            "roles": {"viewer"}
        },
        {
            "name": "Charlie",
            "scores": [88, 92, 79, 85],
            "roles": {"admin", "viewer"}
        }
    ]

    avg_scores = calculate_average_scores(users)
    for user in users:
        name = user["name"]
        average = avg_scores[name]
        admin_access = has_admin_access(user["roles"])
        print(f"Name: {name}")
        print(f"Average Score: {average:.1f}")
        print(f"Admin Access: {admin_access}")
        print()  # Blank line between users

if __name__ == "__main__":
    main()