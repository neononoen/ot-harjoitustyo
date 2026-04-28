from entities.yarn import Yarn
from repositories.yarn_repository import yarn_repository as default_yarn_repository

class InvalidInputError(Exception):
    pass

class EmptyInputError(Exception):
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
        """
        if "" in (name, colour, weight, meters, grams, yarn_type):
            raise EmptyInputError
        if not weight.isdigit():
            raise InvalidInputError
        if not meters.isdigit():
            raise InvalidInputError
        if not grams.isdigit():
            raise InvalidInputError

        meters_total = (int(weight)/int(grams)*int(meters))

        yarn = self.check_if_yarn_in_stash(name, colour, yarn_type)

        if yarn:
            new_weight = int(weight) + yarn.weight
            new_meters = meters_total + yarn.meters

            self._yarn_repository.update_yarn_weight(new_weight, new_meters, yarn.id)
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

    def get_yarns_by_search(self, meters, yarn_type):
        """Palauttaa hakua vastaavat langat.
        
        Args:
            meters: Merkkijonoarvo, joka kuvaa langan vähimmäismetrimäärää.
            yarn_type: Merkkijonoarvo, joka kuvaa langan vahvuutta.
        Returns:
            Yarn-olioita sisältävä lista hakuehtoja vastaavista langoista.
        Raises:
            InvalidInputError:
                Virhe, joka tapahtuu, jos metrimäärä sisältää muita merkkejä kuin numeroita.

        """
        if not meters.isdigit():
            raise InvalidInputError

        if yarn_type == "kaikki":
            return self._yarn_repository.find_by_meterage(int(meters))

        return self._yarn_repository.find_by_meterage_and_type(int(meters), yarn_type)

    def check_if_yarn_in_stash(self, name, colour, yarn_type):
        yarn = self._yarn_repository.find_by_name_colour_and_type(name, colour, yarn_type)

        if not yarn:
            return False
        return yarn

    def change_yarn_total_weight(self, weight, yarn_id):
        if weight == "":
            raise EmptyInputError
        if not weight.isdigit():
            raise InvalidInputError

        yarn = self._yarn_repository.get_yarn_by_id(yarn_id)

        new_meters = (int(weight)/yarn.weight)*yarn.meters

        self._yarn_repository.update_yarn_weight(int(weight), int(new_meters), yarn.id)

yarn_service = YarnService()
