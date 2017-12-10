import unittest

from .babble_sort_imple import BabbleSortImple
from .quick_sort_imple import QuickSortImple
from .timer_sort import TimerSort


class BredgeSortTest(unittest.TestCase):

    def test_bredge_babble_sort(self):
        implementor = BabbleSortImple()
        self.assertEqual(implementor.sort(), 'バブルソート')

    def test_bredge_quick_sort(self):
        implementor = QuickSortImple()
        self.assertEqual(implementor.sort(), 'クイックソート')

    def test_bredge_time_sort(self):
        implementor = QuickSortImple()
        timer_sort = TimerSort(implementor)
        self.assertEqual(timer_sort.timer_sort(), 'タイマーソート')
