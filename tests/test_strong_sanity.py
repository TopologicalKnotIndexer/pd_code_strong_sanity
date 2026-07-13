import unittest
from unittest.mock import patch

from pd_code_strong_sanity import sanity


class StrongSanityTests(unittest.TestCase):
    @patch("pd_code_strong_sanity.main.pd_code_to_diagram.get_diagram_from_pd_code")
    def test_returns_true_when_layout_succeeds(self, layout):
        layout.return_value = [[0, 0], [0, 0]]
        self.assertTrue(sanity([[1, 1, 2, 2]]))

    @patch("pd_code_strong_sanity.main.pd_code_to_diagram.get_diagram_from_pd_code")
    def test_returns_false_for_ordinary_layout_failure(self, layout):
        layout.side_effect = RuntimeError("no layout")
        self.assertFalse(sanity([[1, 1, 2, 2]]))

    @patch("pd_code_strong_sanity.main.pd_code_to_diagram.get_diagram_from_pd_code")
    def test_does_not_swallow_keyboard_interrupt(self, layout):
        layout.side_effect = KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):
            sanity([[1, 1, 2, 2]])


if __name__ == "__main__":
    unittest.main()
