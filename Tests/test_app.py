import unittest

from app import popular_stop, year_count


class TestApp(unittest.TestCase):
    def test_year_count(self):
        """Test that year count works correctly for existing bird"""
        year_count_2018 = year_count("American Goldfinch", 2018)
        self.assertEqual(
            year_count_2018,
            "There were 11 sightings of the American Goldfinch in 2018.",
        )

    def test_year_count_no_bird(self):
        """Test that year count works correctly for a bird that does not exist"""
        year_count_none = year_count("American Goldfinch", 2018)
        self.assertEqual(
            year_count_none,
            "There were 0 sightings of the American Goldfinch in 2018.",
        )

    def test_year_count_no_sightings(self):
        """Test that year count works correctly for a bird with no sightings"""
        year_count_zero = year_count("Brown Thrasher", 2004)
        self.assertEqual(
            year_count_zero,
            "There were 0 sightings of the Brown Thrasher in 2004.",
        )

    def test_popular_stop(self):
        """Test a popular stop"""
        popular_stop_2010 = popular_stop(2010)
        self.assertEqual(
            popular_stop_2010,
            "The most birds were seen at stop 7 in 2010 out of all stops that year.",
        )

    def test_popular_stop_no_year(self):
        """Test a popular stop for a year with no data"""
        popular_stop_2026 = popular_stop(2026)
        self.assertEqual(
            popular_stop_2026,
            "The most birds were seen at stop -1 in 2026 out of all stops that year.",
        )


if __name__ == "__main__":
    unittest.main()
