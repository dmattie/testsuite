import unittest


def add_course(current_course_list, new_courses):
    if len(current_course_list)+len(new_courses)>5:
        raise ValueError("Cannot register for more than 5 courses")
    return current_course_list+new_courses


class TestAddCourse(unittest.TestCase):
    def test_add_course_to_empty_list(self):
        my_courses=add_course(current_course_list=[],new_courses=["BSAD123","BSAD234","BSAD456","BSAD678"])
        expected=["BSAD123","BSAD234","BSAD456","BSAD678"]

        self.assertEqual(my_courses,expected)
    def test_add_course_to_full_list(self):
        current_courses = ["BSAD123","BSAD234","BSAD456","BSAD678"]     
        with self.assertRaises(ValueError):
            my_courses=add_course(current_courses,new_courses=["ECON123","ECON234"])

unittest.main()