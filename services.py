from models import Address, User


def create_users(db):
    users_to_add = [
        User(
            name="spongebob",
            fullname="Spongebob Squarepants",
            addresses=[Address(email_address="spongebob@sqlalchemy.org")],
        ),
        User(
            name="sandy",
            fullname="Sandy Cheeks",
            addresses=[
                Address(email_address="sandy@sqlalchemy.org"),
                Address(email_address="sandy@squirrelpower.org"),
            ],
        ),
        User(name="patrick", fullname="Patrick Star"),
    ]

    for user in users_to_add:
        if db.query(User).filter(User.name == user.name).first():
            print(f"user {user.name} is existed")
        else:
            db.add(user)
            print(f"user {user.name} is added")

    db.commit()


def create_user(db):
    user = User(
        name="new_user",
        fullname="New User",
        addresses=[],
    )
    is_existed = db.query(User).filter(User.name == user.name).first()
    if is_existed:
        print(f"user {user.name} is existed")
        return

    db.add(user)
    db.commit()
    print(f"user {user.name} is added")


def get_all_users(db):
    users = db.query(User).all()
    return users


def get_single_user(db, user_id):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db, user_id, new_name):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        print(f"user with id {user_id} does not exist")
        return

    user.name = new_name
    db.commit()
    print(f"user {user_id} is updated to {new_name}")


def delete_user(db, user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        print(f"user with id {user_id} does not exist")
        return

    db.delete(user)
    db.commit()
    print(f"user with id {user_id} is deleted")
