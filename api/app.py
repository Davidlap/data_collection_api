import sqlalchemy as db


def main():

    engine = db.create_engine("sqlite:///foo.sqlite")
    connection = engine.connect()


if __name__ == "__main__":
    main()