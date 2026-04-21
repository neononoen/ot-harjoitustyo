import unittest
from repositories.yarn_repository import yarn_repository
from entities.yarn import Yarn

class TestYarnRepository(unittest.TestCase):
    def setUp(self):
        yarn_repository.delete_all()
        self.yarn_1 = Yarn("Villalanka", "keltainen", 200, 400, "dk")
        self.yarn_2 = Yarn("Mohairlanka", "sininen", 25, 225, "lace")

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

    def test_find_by_meterage(self):
        yarn_repository.add(self.yarn_1)
        yarn_repository.add(self.yarn_2)

        yarns = yarn_repository.find_by_meterage(300)

        self.assertEqual(len(yarns), 1)
        self.assertEqual(yarns[0].meters, 400)
