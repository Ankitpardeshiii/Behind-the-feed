from collections import Counter


def total_users(users):
    return len(users)


def unique_categories(users):
    return len({
        user["Category"]
        for user in users
        if user["Category"]
    })


def category_counts(users):
    return Counter(
        user["Category"]
        for user in users
        if user["Category"]
    )


def average_followers(users):
    if not users:
        return 0

    return sum(
        user["no_of_followers"]
        for user in users
    ) / len(users)


def average_following(users):
    if not users:
        return 0

    return sum(
        user["no_of_following"]
        for user in users
    ) / len(users)