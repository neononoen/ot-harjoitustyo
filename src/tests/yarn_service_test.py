import unittest
from services.yarn_service import YarnService, InvalidInputError, EmptyInputError 

class FakeYarnRepository:
    def __init__(self, yarns=None):
        self.yarns = yarns or []

    def get_all(self):
        return self.yarns

    def add(self, yarn):
        self.yarns.append(yarn)

    def delete(self, yarn_id):
        for yarn in self.yarns:
            if yarn.id == yarn_id:
                self.yarns.remove(yarn)

    def find_by_meterage(self, meters):
        results = []
        for yarn in self.yarns:
            if yarn.meters >= meters:
                results.append(yarn)

        return results

    def find_by_meterage_and_type(self, meters, yarn_type):
        results = []
        for yarn in self.yarns:
            if  yarn.meters >= meters and yarn.yarn_type == yarn_type:
                results.append(yarn)

        return results

    def find_by_name_colour_and_type(self, name, colour, yarn_type):
        for yarn in self.yarns:
            if yarn.name == name and yarn.colour == colour and yarn.yarn_type == yarn_type:
                return yarn
        return False
    
    def update_yarn_weight(self, weight, meters, yarn_id):
        for yarn in self.yarns:
            if yarn.id == yarn_id:
                yarn.weight = weight
                yarn.meters = meters


class TestYarnService(unittest.TestCase):
    def setUp(self):
        self.yarn_service = YarnService(FakeYarnRepository())
        self.yarn_service.add_yarn("Alpakkalanka", "sininen", "200", "100", "50", "dk")
        self.yarn_service.add_yarn("Puuvillalanka", "punainen", "10", "80", "50", "worsted")

    def test_add_yarn(self):
        yarns = self.yarn_service.get_all_yarns()

        self.assertEqual(len(yarns), 2)
        self.assertEqual(yarns[1].name, "Puuvillalanka")

    def test_delete_yarn(self):
        yarns = self.yarn_service.get_all_yarns()

        self.assertEqual(len(yarns), 2)

        yarn_id = yarns[0].id
        self.yarn_service.delete_yarn(yarn_id)

        yarns = self.yarn_service.get_all_yarns()

        self.assertEqual(len(yarns), 1)

    def test_find_by_meterage(self):
        yarns = self.yarn_service.get_yarns_by_search("90", "dk")

        self.assertEqual(len(yarns), 1)
        self.assertEqual(yarns[0].meters, 400)

    def test_add_yarn_with_invalid_weight_input(self):
        self.assertRaises(InvalidInputError,
                           lambda: self.yarn_service.add_yarn(
                               "Villalanka", "harmaa", "100 grammaa", "210", "50", "fingering"
                               ))

    def test_add_yarn_with_empty_input(self):

        self.assertRaises(EmptyInputError,
                           lambda: self.yarn_service.add_yarn(
                               "Villalanka", "harmaa", "100", "", "", "fingering"
                               ))
    def test_add_yarn_with_invalid_meters_input(self):
        self.assertRaises(InvalidInputError,
                           lambda: self.yarn_service.add_yarn(
                               "Villalanka", "vihreä", "200", "metri", "100", "dk"
                               ))

    def test_if_yarn_in_stash_weight_gets_updated(self):
        self.yarn_service.add_yarn("Alpakkalanka", "sininen", "100", "100", "50", "dk")

        yarns = self.yarn_service.get_all_yarns()

        self.assertEqual(yarns[0].weight, 300)
        self.assertEqual(yarns[0].meters, 600)
