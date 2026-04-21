import unittest
from services.yarn_service import YarnService

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

class TestYarnService(unittest.TestCase):
    def setUp(self):
        self.yarn_service = YarnService(FakeYarnRepository())
        self.yarn_service.add_yarn("Alpakkalanka", "sininen", 50, 100, "dk")
        self.yarn_service.add_yarn("Puuvillalanka", "punainen", 50, 80, "worsted")

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
        yarns = self.yarn_service.get_yarns_by_meterage(90)

        self.assertEqual(len(yarns), 1)
        self.assertEqual(yarns[0].meters, 100)
