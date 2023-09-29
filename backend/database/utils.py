from typing import Dict, List

from .models.users import Users


# TODO: check cpu-bound
def orm2dict(users: List[Users]) -> List[Dict[str, str | int]]:
    """Convert from orm to dict

    Args:
        users (List[Users]): list with orm objects

    Returns:
        List[Dict[str, str | int]]: list with dict, where dict consists info about users
    """
    columns = [c.key for c in users[0][0].__table__.columns]
    results = []

    for i, user in enumerate(users):
        user = user[0]  # need to unpack but user is tuple
        temp = {c: None for c in columns}

        for key in columns:
            temp[key] = getattr(user, key)

        results.append(temp)

    return results
