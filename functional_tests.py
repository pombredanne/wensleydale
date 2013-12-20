import unittest
from datetime import datetime
from sqlalchemy import create_engine
import wensleydale
import wensleydale.sources

class TestSources(unittest.TestCase):
    """Check functionality of data sources"""

    def test_standard_sources(self):
        """The null and pypi sources should exist"""
        self.assertNotEqual(wensleydale.sources.null, None)
        self.assertNotEqual(wensleydale.sources.pypi, None)

    def test_null_source(self):
        """THe null source should respond to all standard queries with no data"""
        self.assertEqual(wensleydale.null_source.packages(), [])
        self.assertEqual(wensleydale.null_source.versions('foo', include_hidden=True), [])
        self.assertEqual(wensleydale.null_source.changes_since(date=datetime.now()), [])
        self.assertEqual(wensleydale.null_source.changes_since(serial=100), [])


class TestDatabase(unittest.TestCase):
    """Basic database management tests"""

    def setUp(self):
        self.engine = create_engine('sqlite://')
        self.db = wensleydale.DB(self.engine)
    def tearDown(self):
        self.engine.dispose()

    def test_init(self):
        """The init method should create the schema"""
        self.db.init()
        # TODO: Needs a bit of work, obviously
        # self.assertEqual(self.db.tables, [...])

if __name__ == '__main__':
    unittest.main()
