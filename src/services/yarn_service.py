from entities.yarn import Yarn
from repositories.yarn_repository import yarn_repository as default_yarn_repository

class YarnService:
    def __init__(self, yarn_repository=default_yarn_repository):
        self._yarn_repository = yarn_repository

    def add_yarn(self, name, colour, weight, meters, type):
        yarn = Yarn(name, colour, weight, meters, type)

        return self._yarn_repository.add(yarn)

    def get_all_yarns(self):
        return self._yarn_repository.get_all()

    def delete_yarn(self, yarn_id):
        self._yarn_repository.delete(yarn_id)

    def get_yarns_by_meterage(self, meters):
        return self._yarn_repository.find_by_meterage(meters)

yarn_service = YarnService()
