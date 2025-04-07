from database import get_db
from services import (
    create_user,
    create_users,
    delete_user,
    get_all_users,
    get_single_user,
    update_user,
)


def main():
    print("Hello from sqlalchemy-demo!")

    db = next(get_db())

    create_users(db)
    print()
    print(get_all_users(db))

    create_user(db)
    print()
    print(get_all_users(db))

    print()
    print(get_single_user(db, 7))

    update_user(db, 7, "updated name")
    print()
    print(get_single_user(db, 7))

    delete_user(db, 7)
    print()
    print(get_single_user(db, 7))


if __name__ == "__main__":
    main()
