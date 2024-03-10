#!/usr/bin/python3
"""testing file_storage engine"""

import unittest
from models.engine.file_storage import FileStorage
from models import storage


class test_storage(unittest.TestCase):
    """temp doc class
    """

    def test_init(self):
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
        assertAlmostEqual(obj, "")


if __name__ == "__main__":
    unittest.main()
