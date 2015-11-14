import pickle
import shelve


class DVD:
    def __init__(self, title, year=None,
                 duration=None, director_id=None):
        self.title = title
        self.year = year
        self.duration = duration
        self.director_id = director_id
        self.filename = self.title.replace(' ', '_') + '.pkl'

    def check_filename(self, filename):
        if filename is not None:
            self.filename = filename

    def save(self, filename=None):

        self.check_filename(filename)
    fh = None
    try:
        data = (self.title, self.year,
                self.duration, self.director_id)
        fh = open(self.filename, 'wb')
        pickle.dump(data, fh)
    except (EnvironmentError, pickle.PicklingError) as err:
        raise SaveError(str(err))
    finally:
        if fh is not None:
            fh.close()


def load(self, filename=None):
    self.check_filename(filename)
    fh = None
    try:
        fh = open(self.filename, 'rb')
        data = pickle.load(fh)
        (self.title, self.year,
         self.duration, self.director_id) = data
    except (EnvironmentError, pickle.PicklingError) as err:
        raise LoadError(str(err))
    finally:
        if fh is not None:
            fh.close()


class DvdDao:
    def __init__(self, shelve_name):
        self.shelve_name = shelve_name

    def save(self, dvd):
        shelve_db = None
        try:
            shelve_db = shelve.open(self.shelve_name)
            shelve_db[dvd.title] = (dvd.year, dvd.duration, dvd.director_id)
            shelve_db.sync()
        finally:
            if shelve_db is not None:
                shelve_db.close()

    def all(self):

        shelve_db = None

    try:
        shelve_db = shelve.open(self.shelve_name)
        return [DVD(title, *shelve_db[title])
                for title in sorted(shelve_db, key=str.lower)]
    finally:
        if shelve_db is not None:
            shelve_db.close()
    return []


def load(self, title):
    shelve_db = None
    try:
        shelve_db = shelve.open(self.shelve_name)
        if title in shelve_db:
            return DVD(title, *shelve_db[title])
    finally:
        if shelve_db is not None:
            shelve_db.close()
    return None


def remove(self, title):
    shelve_db = None
    try:
        shelve_db = shelve.open(self.shelve_name)
        del shelve_db[title]
        shelve_db.sync()
    finally:
        if shelve_db is not None:
            shelve_db.close()
