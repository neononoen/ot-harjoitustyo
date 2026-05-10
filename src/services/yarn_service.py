from entities.yarn import Yarn
from repositories.yarn_repository import yarn_repository as default_yarn_repository

class InvalidInputError(Exception):
    pass

class EmptyInputError(Exception):
    pass

class InputZeroError(Exception):
    pass

class ZeroMetersError(Exception):
    pass

class InvalidYarnTypeError(Exception):
    pass

class YarnService:
    """Luokka, joka vastaa sovelluslogiikasta."""
    def __init__(self, yarn_repository=default_yarn_repository):
        """Luokan konstruktori, joka luo uuden sovelluslogiikasta vastaavan palvelun.
        
        Args:
        yarn_repository: 
            Oletusarvoltaan YarnRepository-olio.
            Olio, jolla on YarnRepository-luokan metodit.
        """
        self._yarn_repository = yarn_repository
        self._yarn_types = ["lace", "fingering", "sport", "dk", "aran", "worsted", "bulky"]

    def add_yarn(self, name, colour, weight, meters, grams, yarn_type):
        """Luo uuden langan.
        
        Args:
            name: Merkkijonoarvo, joka kertoo langan nimen.
            colour: Merkkijonoarvo, joka kuvaa langan väriä.
            weight: Merkkijonoarvo, joka kertoo langan kokonaismäärän grammoina.
            meters: Merkkijonoarvo, joka kertoo kerässä olevan langan määrän metreinä.
            grams: Merkkijonoarvo, joka kertoo kerässä olevan langan määrän grammoina
            yarn_type: Merkkijonoarvo, joka kuvaa langan vahvuutta/paksuutta.
        Raises:
            EmptyInputError:
                Virhe, joka tapahtuu, jos jokin argumentti on tyhjä merkkijono.
            InvalidInputError:
                Virhe, joka tapahtuu, jos kokonaispaino, kerän metrimäärä tai grammamäärä 
                sisältää muita merkkejä kuin numeroita.
            InputZeroError:
                Virhe, joka tapahtuu, jos kokonaispaino, kerän metrimäärä tai grammamäärä on 0.
            InvalidYarnTypeError:
            Virhe, joka tapahtuu, jos langan vahvuus ei ole valittu annetusta listasta.
        """
        if "" in (name, colour, weight, meters, grams, yarn_type):
            raise EmptyInputError
        if not weight.isdigit():
            raise InvalidInputError
        if not meters.isdigit():
            raise InvalidInputError
        if not grams.isdigit():
            raise InvalidInputError
        if "0" in (weight, meters, grams):
            raise InputZeroError
        if yarn_type not in self._yarn_types:
            raise InvalidYarnTypeError

        meters_total = (int(weight)/int(grams)*int(meters))

        yarn = self.check_if_yarn_in_stash(name, colour, yarn_type)

        if yarn:
            new_weight = int(weight) + yarn.weight
            new_meters = meters_total + yarn.meters

            self._yarn_repository.update_yarn_amount(new_weight, new_meters, yarn.id)
        else:
            yarn = Yarn(name, colour, int(weight), int(meters_total), yarn_type)

            self._yarn_repository.add(yarn)

    def get_all_yarns(self):
        """Palauttaa kaikki langat.
        
        Returns:
            Yarn-olioita sisältävä lista kaikista langoista.
        """
        return self._yarn_repository.get_all()

    def delete_yarn(self, yarn_id):
        """Poistaa langan.
        
        Args:
            yarn_id: Merkkijonoarvo, joka kuvaa poistettavan langan id:tä.
        """
        self._yarn_repository.delete(yarn_id)

    def get_yarns_by_search(self, name, colour, meters, yarn_type):
        """Palauttaa hakua vastaavat langat.
        
        Args:
            name: Merkkijonoarvo, joka kertoo haettavan langan nimen.
            colour: Merkkijonoarvo, joka kuvaa langan väriä.
            meters: Merkkijonoarvo, joka kuvaa langan vähimmäismetrimäärää.
            yarn_type: Merkkijonoarvo, joka kuvaa langan vahvuutta.
        Returns:
            Yarn-olioita sisältävä lista hakuehtoja vastaavista langoista.
        Raises:
            InvalidInputError:
                Virhe, joka tapahtuu, jos metrimäärä sisältää muita merkkejä kuin numeroita.
            InvalidYarnTypeError:
                Virhe, joka tapahtuu, jos langan vahvuus ei ole valittu annetuista vaihtoehdoista.
        """
        if meters == "":
            meters = "0"
        if not meters.isdigit():
            raise InvalidInputError
        if yarn_type not in self.get_yarn_types_for_search():
            raise InvalidYarnTypeError

        return self._yarn_repository.find_by_search(name, colour, int(meters), yarn_type)

    def check_if_yarn_in_stash(self, name, colour, yarn_type):
        """Tarkistaa onko sama lanka jo lisätty varastoon.

        Args:
            name: Merkkijonoarvo, joka kertoo langan nimen.
            colour: Merkkijonoarvo, joka kuvaa langan väriä.
            yarn_type: Merkkijonoarvo, joka kertoo langan vahvuuden.
        Returns:
            Yarn-olion, jos lanka löytyy varastosta.
            False, jos lankaa ei löydy.
        """
        yarn = self._yarn_repository.find_by_name_colour_and_type(name, colour, yarn_type)

        if not yarn:
            return False
        return yarn

    def change_yarn_total_weight(self, weight, yarn_id):
        """Muuttaa langan määrän.
        
        Args:
            weight: Merkkijonoarvo, joka kertoo langan uuden painon.
            yarn_id: Merkkijonoarvo, joka kertoo langan id-tunnisteen.
        Raises:
            EmptyInputError:
                Virhe, joka tapahtuu, jos paino on tyhjä merkkijono.
            InvalidInputError:
                Virhe, joka tapahtuu, jos paino sisältää muita merkkejä kuin numeroita.
            ZeroMetersError:
                Virhe, joka tapahtuu, jos uusi langan määrä metreissä on vähemmän kuin 1.
        """
        if weight == "":
            raise EmptyInputError
        if not weight.isdigit():
            raise InvalidInputError

        yarn = self._yarn_repository.get_yarn_by_id(yarn_id)

        new_meters = (int(weight)/yarn.weight)*yarn.meters
        if int(new_meters) < 1:
            raise ZeroMetersError

        self._yarn_repository.update_yarn_amount(int(weight), int(new_meters), yarn.id)

    def get_total_yarn_weight(self):
        if self._yarn_repository.get_total_weight():
            return self._yarn_repository.get_total_weight()
        return 0

    def get_total_yarn_meterage(self):
        if self._yarn_repository.get_total_meters():
            return self._yarn_repository.get_total_meters()
        return 0

    def get_number_of_yarns_in_stash(self):
        return len(self._yarn_repository.get_all())

    def get_total_weight_by_yarn_type(self):
        total_weights = {}

        for yarn_type in self._yarn_types:
            total_weight = self._yarn_repository.get_total_weight_by_yarn_type(yarn_type)
            total_weights[yarn_type] = total_weight if total_weight else 0

        return total_weights

    def get_yarn_types(self):
        return self._yarn_types

    def get_yarn_types_for_search(self):
        yarn_types = self._yarn_types.copy()
        yarn_types.insert(0, "kaikki")

        return yarn_types

yarn_service = YarnService()
