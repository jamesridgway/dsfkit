from io import StringIO

from assertpy import assert_that

from dsfkit.csvjson import CsvJson


class TestCsvJson:
    def test_convert_respects_order_of_keys(self):
        assert_that(CsvJson().convert(StringIO("first_name,last_name\nJohn,Smith")))\
            .is_equal_to('[{"first_name": "John", "last_name": "Smith"}]')

        assert_that(CsvJson().convert(StringIO("last_name,first_name\nSmith,John"))) \
            .is_equal_to('[{"last_name": "Smith", "first_name": "John"}]')

    def test_sort_columns(self):
        csv_json = CsvJson(sort_columns=True)
        assert_that(csv_json.convert(StringIO("first_name,last_name\nJohn,Smith")))\
            .is_equal_to('[{"first_name": "John", "last_name": "Smith"}]')

        assert_that(csv_json.convert(StringIO("last_name,first_name\nSmith,John"))) \
            .is_equal_to('[{"first_name": "John", "last_name": "Smith"}]')
