from src.converter import convert_to_json
from src.analyzer import (
    get_max_followers,
    get_max_following,
    get_top_followers,
    get_top_following,
)
from src.statistics import (
    total_users,
    unique_categories,
    category_counts,
    average_followers,
    average_following,
)


def main():
    users = convert_to_json(
        "data/initialdata.txt",
        "data/Punedata.json"
    )

    print("=" * 60)
    print("INSTAGRAM DATA ANALYSIS")
    print("=" * 60)

    print(f"Total Users          : {total_users(users)}")
    print(f"Unique Categories    : {unique_categories(users)}")
    print(f"Average Followers    : {average_followers(users):,.2f}")
    print(f"Average Following    : {average_following(users):,.2f}")

    print("\nCategory Counts")
    print("-" * 60)
    for category, count in category_counts(users).items():
        print(f"{category:<25} {count}")

    max_followers = get_max_followers(users)

    print("\nMost Followed Account")
    print("-" * 60)
    print(f"Username   : {max_followers['Username']}")
    print(f"Name       : {max_followers['Name']}")
    print(f"Followers  : {max_followers['no_of_followers']:,}")
    print(f"Following  : {max_followers['no_of_following']:,}")
    print(f"Category   : {max_followers['Category']}")

    max_following = get_max_following(users)

    print("\nMost Following Account")
    print("-" * 60)
    print(f"Username   : {max_following['Username']}")
    print(f"Name       : {max_following['Name']}")
    print(f"Followers  : {max_following['no_of_followers']:,}")
    print(f"Following  : {max_following['no_of_following']:,}")
    print(f"Category   : {max_following['Category']}")

    print("\nTop 10 Accounts by Followers")
    print("-" * 60)

    for i, user in enumerate(get_top_followers(users), start=1):
        print(
            f"{i:2}. "
            f"{user['Username']:<25}"
            f"{user['no_of_followers']:,} Followers"
        )

    print("\nTop 10 Accounts by Following")
    print("-" * 60)

    for i, user in enumerate(get_top_following(users), start=1):
        print(
            f"{i:2}. "
            f"{user['Username']:<25}"
            f"{user['no_of_following']:,} Following"
        )


if __name__ == "__main__":
    main()