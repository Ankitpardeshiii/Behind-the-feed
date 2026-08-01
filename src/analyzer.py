def get_max_followers(users):
    if not users:
        return None

    return max(users, key=lambda user: user["no_of_followers"])


def get_max_following(users):
    if not users:
        return None

    return max(users, key=lambda user: user["no_of_following"])


def get_unique_categories(users):
    categories = set()

    for user in users:
        category = user.get("Category", "").strip()
        if category:
            categories.add(category)

    return categories


def get_category_count(users):
    categories = {}

    for user in users:
        category = user.get("Category", "").strip()

        if not category:
            category = "Unknown"

        categories[category] = categories.get(category, 0) + 1

    return categories


def get_total_users(users):
    return len(users)


def get_top_followers(users, n=10):
    return sorted(
        users,
        key=lambda user: user["no_of_followers"],
        reverse=True
    )[:n]


def get_top_following(users, n=10):
    return sorted(
        users,
        key=lambda user: user["no_of_following"],
        reverse=True
    )[:n]