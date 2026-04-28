from uuid import uuid4

class Yarn:
    """Luokka, joka kuvaa yksittäistä lankaa.

    Attributes:
        name: Merkkijonoarvo, joka kertoo langan nimen.
        colour: Merkkijonoarvo, joka kuvaa langan väriä.
        weight: Kokonaislukuarvo, joka kertoo langan määrän grammoina.
        meters: Kokonaislukuarvo, joka kertoo langan määrän metreinä.
        yarn_type: Merkkijonoarvo, joka kuvaa langan vahvuutta/paksuutta.
        yarn_id: Merkkijonoarvo, joka kertoo langan id-tunnisteen.
    """
    def __init__(self, name, colour, weight, meters, yarn_type, yarn_id=None):
        """Luokan konstruktori, joka luo uuden langan.

        Args:
            name: Merkkijonoarvo, joka kertoo langan nimen.
            colour: Merkkijonoarvo, joka kuvaa langan väriä.
            weight: Kokonaislukuarvo, joka kertoo langan määrän grammoina.
            meters: Kokonaislukuarvo, joka kertoo langan määrän metreinä.
            yarn_type: Merkkijonoarvo, joka kuvaa langan vahvuutta/paksuutta.
            yarn_id: 
                Oletusarvoltaan generoitu uuid.
                Merkkijonoarvo, joka kertoo langan id-tunnisteen.
        """
        self.name = name
        self.colour = colour
        self.weight = weight
        self.meters = meters
        self.yarn_type = yarn_type
        self.id = yarn_id if yarn_id else str(uuid4())
