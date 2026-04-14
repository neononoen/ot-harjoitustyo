import unittest
from entities.yarn import Yarn
from services.yarn_service import YarnService

class FakeYarnRepository:
    def __init__(self, yarns=None):
        self.yarns = yarns or []

    def get_all(self):
        return self.yarns

    def add(self, yarn):
        self.yarns.append(yarn)

        return yarn

class TestYarnService(unittest.TestCase):
    def setUp(self):
        self.yarn_service = YarnService(FakeYarnRepository())

    def test_add_yarn(self):
        self.yarn_service.add_yarn("Alpakkalanka", "sininen", 50, 100, "dk")
        self.yarn_service.add_yarn("Puuvillalanka", "punainen", 50, 80, "worsted")

        yarns = self.yarn_service.get_all_yarns()

        self.assertEqual(len(yarns), 2)
        self.assertEqual(yarns[1].name, "Puuvillalanka")
