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

    def find_by_name_colour_and_type(self, name, colour, yarn_type):
        for yarn in self.yarns:
            if yarn.name == name and yarn.colour == colour and yarn.yarn_type == yarn_type:
                return yarn
        return False

    def update_yarn_amount(self, weight, meters, yarn_id):
        for yarn in self.yarns:
            if yarn.id == yarn_id:
                yarn.weight = weight
                yarn.meters = meters

    def get_total_weight(self):
        weights = [yarn.weight for yarn in self.yarns]

        return sum(weights)

    def get_total_weight_by_yarn_type(self, yarn_type):
        weights = [yarn.weight for yarn in self.yarns if yarn.yarn_type == yarn_type]

        return sum(weights)

class TestYarnService(unittest.TestCase):
    def setUp(self):
        self.yarn_service = YarnService(FakeYarnRepository())

    def test_add_yarn(self):
        self.yarn_service.add_yarn("Alpakkalanka", "sininen", "200", "100", "50", "dk")
        self.yarn_service.add_yarn("Puuvillalanka", "punainen", "10", "80", "50", "worsted")

        yarns = self.yarn_service.get_all_yarns()

        self.assertEqual(len(yarns), 2)
        self.assertEqual(yarns[1].name, "Puuvillalanka")

    def test_delete_yarn(self):
        self.yarn_service.add_yarn("Alpakkalanka", "sininen", "200", "100", "50", "dk")
        self.yarn_service.add_yarn("Puuvillalanka", "punainen", "10", "80", "50", "worsted")

        yarns = self.yarn_service.get_all_yarns()

        self.assertEqual(len(yarns), 2)

        yarn_id = yarns[0].id
        self.yarn_service.delete_yarn(yarn_id)

        yarns = self.yarn_service.get_all_yarns()

        self.assertEqual(len(yarns), 1)

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
        self.yarn_service.add_yarn("Alpakkalanka", "sininen", "200", "100", "50", "dk")
        self.yarn_service.add_yarn("Puuvillalanka", "punainen", "10", "80", "50", "worsted")

        self.yarn_service.add_yarn("Alpakkalanka", "sininen", "100", "100", "50", "dk")

        yarns = self.yarn_service.get_all_yarns()

        self.assertEqual(yarns[0].weight, 300)
        self.assertEqual(yarns[0].meters, 600)

    def test_get_total_yarn_weight_returns_total_weight(self):
        self.yarn_service.add_yarn("Alpakkalanka", "sininen", "200", "100", "50", "dk")
        self.yarn_service.add_yarn("Puuvillalanka", "punainen", "10", "80", "50", "worsted")

        total_weight = self.yarn_service.get_total_yarn_weight()

        self.assertEqual(total_weight, 210)

    def test_get_total_yarn_weight_returns_zero_if_no_yarns(self):
        total_weight = self.yarn_service.get_total_yarn_weight()

        self.assertEqual(total_weight, 0)

    def test_get_total_weight_by_type(self):
        self.yarn_service.add_yarn("Alpakkalanka", "sininen", "200", "100", "50", "dk")
        self.yarn_service.add_yarn("Puuvillalanka", "punainen", "10", "80", "50", "worsted")
        self.yarn_service.add_yarn("Villalanka", "keltainen", "100", "100", "50", "dk")

        total_weights = self.yarn_service.get_total_weight_by_yarn_type()

        self.assertEqual(total_weights["dk"], 300)
        self.assertEqual(total_weights["lace"], 0)

    def test_get_number_of_yarns_in_stash(self):
        self.yarn_service.add_yarn("Alpakkalanka", "sininen", "200", "100", "50", "dk")
        self.yarn_service.add_yarn("Puuvillalanka", "punainen", "10", "80", "50", "worsted")
        self.yarn_service.add_yarn("Villalanka", "keltainen", "100", "100", "50", "dk")

        number_of_yarns = self.yarn_service.get_number_of_yarns_in_stash()

        self.assertEqual(number_of_yarns, 3)
