from entities.yarn import Yarn
from database_connection import get_database_connection

class YarnRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from yarns")
        rows = cursor.fetchall()

        return [Yarn(row["name"], row["colour"], row["weight"], row["meters"],
                     row["type"], row["id"]) for row in rows]

    def add(self, yarn):
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into yarns (name, colour, weight, meters, type, id) values (?, ?, ?, ?, ?, ?)",
            (yarn.name, yarn.colour, yarn.weight, yarn.meters, yarn.type, yarn.id)
        )

        self._connection.commit()

        return yarn

    def delete(self, yarn_id):
        cursor = self._connection.cursor()
        cursor.execute("delete from yarns where id = ?", (yarn_id, ))

        self._connection.commit()

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from yarns")

        self._connection.commit()

    def find_by_meterage(self, meters):
        cursor = self._connection.cursor()
        cursor.execute("select * from yarns where meters >= ?", (meters, ))

        rows = cursor.fetchall()

        return [Yarn(row["name"], row["colour"], row["weight"], row["meters"],
                     row["type"], row["id"]) for row in rows]

yarn_repository = YarnRepository(get_database_connection())
