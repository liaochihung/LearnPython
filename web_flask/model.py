import peewee

database = peewee.SqliteDatabase("event_log.db")


class ActionHistory(peewee.Model):
    # date time format will be cause problem when conver to json
    # created = peewee.DateTimeField()
    created = peewee.CharField()
    board_num = peewee.IntegerField()
    mark = peewee.BooleanField(default=False)

    # Need Analog Input record ?

    class Meta:
        database = database


if __name__ == "__main__":
    try:
        ActionHistory.create_table()
    except peewee.OperationalError:
        print("Artist table already exists!")
