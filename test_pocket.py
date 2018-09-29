import unittest
from typing import List

from pocket import dictionary


@dictionary
class Apple:
    a: str
    b: int


@dictionary(frozen=True)
class Banana:
    apples: List[Apple]


@dictionary
class Cat:
    pass


class TestPocket(unittest.TestCase):

    def test_dict(self):
        self.assertDictEqual(
            {'a': 'apple', 'b': 3},
            Apple('apple', 3).dict,
        )

        self.assertDictEqual(
            {
                'apples': [
                    {'a': '1', 'b': 2},
                    {'a': '3', 'b': 4},
                    {'a': '5', 'b': 6}
                ]
            },
            Banana([
                Apple('1', 2),
                Apple('3', 4),
                Apple('5', 6)
            ]).dict,
        )

        self.assertDictEqual(
            {},
            Cat().dict,
        )

    def test_json(self):
        self.assertEqual(
            '{"a": "abc", "b": 999}',
            Apple('abc', 999).json
        )

        self.assertEqual(
            '{"apples": [{"a": "1", "b": 2}, {"a": "3", "b": 4}]}',
            Banana([
                Apple('1', 2),
                Apple('3', 4)
            ]).json
        )

        self.assertEqual(
            '{}',
            Cat().json
        )
