import peewee

database = peewee.SqliteDatabase("wee.db")


class ActionHistory(peewee.Model):
    create = peewee.DateTimeField()
    board_num = peewee.IntegerField()

    # Need Analog Input record ?

    class Meta:
        database = database


if __name__ == "__main__":
    try:
        ActionHistory.create_table()
    except peewee.OperationalError:
        print("Artist table already exists!")
