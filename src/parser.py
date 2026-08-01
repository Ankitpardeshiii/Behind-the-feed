def parse_chunk(chunk):
    chunk = chunk.strip()
    sep_chunk = chunk.split("\n")

    username = sep_chunk[0]

    no_of_post = int(
        sep_chunk[1].split("post")[0].replace(",", "")
    )

    no_of_followers = float(
        sep_chunk[2]
        .split("followers")[0]
        .replace(",", "")
        .replace("K", "")
        .replace("M", "")
    )

    if "K" in sep_chunk[2]:
        no_of_followers = int(no_of_followers * 1000)
    elif "M" in sep_chunk[2]:
        no_of_followers = int(no_of_followers * 1000000)
    else:
        no_of_followers = int(no_of_followers)

    no_of_following = float(
        sep_chunk[3]
        .split("following")[0]
        .replace(",", "")
        .replace("K", "")
        .replace("M", "")
    )

    if "K" in sep_chunk[3]:
        no_of_following = int(no_of_following * 1000)
    elif "M" in sep_chunk[3]:
        no_of_following = int(no_of_following * 1000000)
    else:
        no_of_following = int(no_of_following)

    name = sep_chunk[4]

    if len(sep_chunk) > 5:
        category = sep_chunk[5]
        bio = "\n".join(sep_chunk[6:])
    else:
        category = "unknown"
        bio = ""

    return {
        "Username": username,
        "no_of_post": no_of_post,
        "no_of_followers": no_of_followers,
        "no_of_following": no_of_following,
        "Name": name,
        "Category": category,
        "Bio": bio
    }