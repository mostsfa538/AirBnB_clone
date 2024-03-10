#!/usr/bin/python3
"""testing file_storage engine"""

import unittest
from models.base_model import BaseModel


class test_base(unittest.TestCase):
    """temp doc class
    """

    def test_init(self):
        result = """[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {
        'my_number': 89, 'name': 'My First Model', 'updated_at'
        : datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id'
        : 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at'
        : datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        assertAlmostEqual(my_model.__str__(), result)


if __name__ == "__main__":
    unittest.main()
