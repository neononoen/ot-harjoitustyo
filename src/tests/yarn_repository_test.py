import unittest
from repositories.yarn_repository import yarn_repository
from entities.yarn import Yarn

class TestYarnRepository(unittest.TestCase):
    def setUp(self):
        yarn_repository.delete_all()
        self.yarn_1 = Yarn("Villalanka", "keltainen", 200, 400, "dk")
        self.yarn_2 = Yarn("Mohairlanka", "sininen", 25, 225, "lace")
        self.yarn_3 = Yarn("Villalanka", "punainen", 100, 200, "dk")

    def test_add_yarn(self):
        yarn_repository.add(self.yarn_1)

        yarns = yarn_repository.get_all()

        self.assertEqual(len(yarns), 1)
        self.assertEqual(yarns[0].name, "Villalanka")

    def test_get_all_yarns(self):
        yarn_repository.add(self.yarn_1)
        yarn_repository.add(self.yarn_2)

        yarns = yarn_repository.get_all()

        self.assertEqual(len(yarns), 2)
        self.assertEqual(yarns[0].name, "Villalanka")
        self.assertEqual(yarns[1].name, "Mohairlanka")

    def test_delete_yarn(self):
        yarn_repository.add(self.yarn_1)
        yarn_repository.add(self.yarn_2)

        yarns = yarn_repository.get_all()

        self.assertEqual(len(yarns), 2)

        yarn_repository.delete(self.yarn_1.id)

        yarns = yarn_repository.get_all()

        self.assertEqual(len(yarns), 1)

    def test_find_by_name_colour_and_type(self):
        yarn_repository.add(self.yarn_1)
        yarn_repository.add(self.yarn_3)

        yarn = yarn_repository.find_by_name_colour_and_type("Villalanka", "punainen", "dk")

        self.assertEqual(yarn.name, "Villalanka")
        self.assertEqual(yarn.colour, "punainen")

    def test_find_by_name_colour_and_type_when_not_in_stash(self):
        yarn_repository.add(self.yarn_1)
        yarn_repository.add(self.yarn_3)

        yarn = yarn_repository.find_by_name_colour_and_type("Villalanka", "sininen", "dk")

        self.assertEqual(yarn, None)

    def test_update_yarn_amount(self):
        yarn_repository.add(self.yarn_1)

        yarns = yarn_repository.get_all()

        self.assertEqual(yarns[0].weight, 200)

        yarn_repository.update_yarn_amount(100, 200, yarns[0].id)

        yarns = yarn_repository.get_all()

        self.assertEqual(yarns[0].weight, 100)
        self.assertEqual(yarns[0].meters, 200)

    def test_get_yarn_by_id(self):
        yarn_repository.add(self.yarn_1)
        yarn_repository.add(self.yarn_2)

        yarn = yarn_repository.get_yarn_by_id(self.yarn_1.id)

        self.assertEqual(yarn.name, "Villalanka")
        self.assertEqual(yarn.colour, "keltainen")

    def test_get_yarn_by_invalid_id(self):
        yarn_repository.add(self.yarn_1)
        yarn_repository.add(self.yarn_2)

        yarn = yarn_repository.get_yarn_by_id("abc")

        self.assertEqual(yarn, None)

    def test_find_yarns_by_search_returns_all_yarns(self):
        yarn_repository.add(self.yarn_1)
        yarn_repository.add(self.yarn_2)
        yarn_repository.add(self.yarn_3)

        yarns = yarn_repository.find_by_search("", "", 0, "kaikki")

        self.assertEqual(len(yarns), 3)

    def test_find_yarns_by_search_returns_yarns_with_correct_name(self):
        yarn_repository.add(self.yarn_1)
        yarn_repository.add(self.yarn_2)
        yarn_repository.add(self.yarn_3)

        yarns = yarn_repository.find_by_search("mohair", "", 0, "kaikki")

        self.assertEqual(len(yarns), 1)
        self.assertEqual(yarns[0].name, "Mohairlanka")

    def test_find_by_search_returns_yarn_by_colour_and_type(self):
        yarn_repository.add(self.yarn_1)
        yarn_repository.add(self.yarn_2)
        yarn_repository.add(self.yarn_3)

        yarns = yarn_repository.find_by_search("", "punainen", 0, "dk")

        self.assertEqual(len(yarns), 1)
        self.assertEqual(yarns[0].colour, "punainen")
        self.assertEqual(yarns[0].yarn_type, "dk")

    def test_find_by_search_returns_no_yarns(self):
        yarn_repository.add(self.yarn_1)
        yarn_repository.add(self.yarn_2)
        yarn_repository.add(self.yarn_3)

        yarns = yarn_repository.find_by_search("", "", 600, "kaikki")

        self.assertEqual(len(yarns), 0)

    def test_get_total_weight_returns_sum_of_weights(self):
        yarn_repository.add(self.yarn_1)
        yarn_repository.add(self.yarn_2)

        total_weight = yarn_repository.get_total_weight()

        self.assertEqual(total_weight, 225)

    def test_get_total_weight_returns_none_if_no_yarns(self):
        total_weight = yarn_repository.get_total_weight()

        self.assertIsNone(total_weight)
    