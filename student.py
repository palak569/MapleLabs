from config import data_file
from tinydb import TinyDB, Query
from studentdb import StudentDB, stud, sub, perf
import json


class Student:
    def __init__(self):
        self.__sdb = StudentDB()

    def post_personal_details(self, name, dob, phone):
        t_dict = {
            "name": name,
            "dob": dob,
            "phone": phone
        }
        print(t_dict)
        self.__sdb.post_student_details(t_dict)

    def post_academic_details(self, sub_name, passing_marks):
        t_dict = {
            "sub_name": sub_name,
            "passing_marks": passing_marks
        }
        print(t_dict)
        self.__sdb.post_subject_details(t_dict)

    def post_performance_details(self, id, sub_id, obtained_marks):
        item = self.__sdb.get_performance_details(id)
        print(item)
        t_dict = {
           "sub_id": sub_id,
           "obtained_marks": obtained_marks
        }
        if item:
            print(item)
            data = item['sub_details']
            print(data)
            data.append(t_dict)
            print(data)
            print(item)
            self.__sdb.update_performance_details(id, item)
        else:
            t_dict1 = {
                "sub_details": [{"sub_id": sub_id, "obtained_marks": obtained_marks}]
            }
            print(t_dict1)
            self.__sdb.post_performance_details(t_dict1)


std = Student()
#std.post_personal_details("palak", "28-09-2000", "9141009999")
#std.post_academic_details("Hindi", 35)
std.post_performance_details(4, 1, 20)
