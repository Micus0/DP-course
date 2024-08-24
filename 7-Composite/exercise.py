from unittest import TestCase
from abc import ABC
from collections.abc import Iterable


class ValueContainer(Iterable, ABC):
    @property
    def sum(self):
        result = 0

        for c in self:
            if isinstance(c, list):
                result += c.sum
            elif isinstance(c, int):
                result += c
            else:
                result += c.value
            # for i in c:
            #     if isinstance(i, list):
            #         result += i.sum
            #     elif not isinstance(i, int):
            #         i = i.value
            #     result += i

        return result


class SingleValue(ValueContainer):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, ValueContainer):
    pass


class Evaluate(TestCase):
    def test_exercise(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum, 66)

    def test_SingleValue_obj_sum(self):
        single_value = SingleValue(11)
        self.assertEqual(single_value.sum, 11)

    def test_ManyValues_obj_sum(self):
        other_values = ManyValues()
        single_value = SingleValue(1)

        other_values.append(22)
        other_values.append(33)
        other_values.append(single_value)
        self.assertEqual(other_values.sum, 56)

    def test_hierarchy_Many_Values(self):
        sv_1 = SingleValue(1)
        mv_1 = ManyValues()
        mv_2 = ManyValues()
        mv_3 = ManyValues()

        mv_1.append(sv_1)
        mv_1.append(1)

        mv_2.append(mv_1)
        mv_2.append(sv_1)
        mv_2.append(1)

        mv_3.append(1)
        mv_3.append(mv_2)
        mv_3.append(sv_1)
        mv_3.append(sv_1)
        mv_3.append(1)

        self.assertEqual(mv_3.sum, 8)
