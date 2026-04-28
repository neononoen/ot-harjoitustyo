from entities.yarn import Yarn
from database_connection import get_database_connection

class YarnRepository:
    """Luokka, joka vastaa tietokantaoperaatioista"""
    def __init__(self, connection):
        """Luokan konstruktori.
        
        Args:
            connection: Tietokantayhteyden Connection-olio.
        """
        self._connection = connection

    def get_all(self):
        """Palauttaa kaikki langat.
        
        Returns:
            Yarn-olioita sisältävä lista kaikista langoista.
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from yarns")
        rows = cursor.fetchall()

        return [Yarn(row["name"], row["colour"], row["weight"], row["meters"],
                     row["type"], row["id"]) for row in rows]

    def add(self, yarn):
        """Tallentaa uuden langan tietokantaan.
        
        Args:
            yarn: Yarn-olio tallenettavasta langasta.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into yarns (name, colour, weight, meters, type, id) values (?, ?, ?, ?, ?, ?)",
            (yarn.name, yarn.colour, yarn.weight, yarn.meters, yarn.yarn_type, yarn.id)
        )

        self._connection.commit()

    def delete(self, yarn_id):
        """Poistaa langan.
        
        Args:
            yarn_id: Merkkijonoarvo, joka kuvaa poistettavan langan id:tä.
        """
        cursor = self._connection.cursor()
        cursor.execute("delete from yarns where id = ?", (yarn_id, ))

        self._connection.commit()

    def delete_all(self):
        """Poistaa kaikki langat."""
        cursor = self._connection.cursor()
        cursor.execute("delete from yarns")

        self._connection.commit()

    def find_by_meterage_and_type(self, meters, yarn_type):
        """Palauttaa hakuehtoja vastaavat langat.
        
        Args:
            meters: Kokonaislukuarvo, joka kuvaa langan vähimmäismetrimäärää.
            yarn_type: Merkkijonoarvo, joka kuvaa langan vahvuutta.
        Returns:
            Yarn-olioita sisältävä lista hakuehtoja vastaavista langoista.
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from yarns where meters >= ? and type = ?", (meters, yarn_type ))

        rows = cursor.fetchall()

        return [Yarn(row["name"], row["colour"], row["weight"], row["meters"],
                     row["type"], row["id"]) for row in rows]

    def find_by_meterage(self, meters):
        """Palauttaa hakuehtoa vastaavat langat
        
        Args:
            meters: Kokonaislukuarvo, joka kuvaa langan vähimmäismetrimäärää.
        Returns:
            Yarn-olioita sisältävä lista hakuehtoa vastaavista langoista.
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from yarns where meters >= ?", (meters, ))

        rows = cursor.fetchall()

        return [Yarn(row["name"], row["colour"], row["weight"], row["meters"],
                     row["type"], row["id"]) for row in rows]

    def find_by_name_colour_and_type(self, name, colour, yarn_type):
        cursor = self._connection.cursor()
        cursor.execute("select * from yarns where name = ? and colour = ? and type = ?",
                        (name, colour, yarn_type))

        row = cursor.fetchone()

        return Yarn(row["name"], row["colour"], row["weight"],
                     row["meters"], row["type"], row["id"]) if row else None


    def update_yarn_weight(self, weight, meters, yarn_id):
        cursor = self._connection.cursor()
        cursor.execute("update yarns set weight = ?, meters = ? where id = ?",
                        (weight, meters, yarn_id))

        self._connection.commit()

    def get_yarn_by_id(self, yarn_id):
        cursor = self._connection.cursor()
        cursor.execute("select * from yarns where id = ?", (yarn_id, ))

        row = cursor.fetchone()

        return Yarn(row["name"], row["colour"], row["weight"],
                     row["meters"], row["type"], row["id"]) if row else None


yarn_repository = YarnRepository(get_database_connection())
