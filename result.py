import json
from config import data_file
from tinydb import TinyDB, Query
from studentdb import StudentDB, stud, sub, perf


class Result:
    def __init__(self):
        self.__sdb = StudentDB()

    def one_student(self, id):
        item = self.__sdb.get_performance_details(id)
        #print(item)
        for data in item['sub_details']:
            #print(data)
            sub_data = sub.get(data['sub_id'])
            #print(sub_data)
            if data['obtained_marks'] > sub_data['passing_marks']:
                data.update(result="pass")
            else:
                data.update(result="fail")

        #print(item)
        return item

    def one_subject(self, id):
        item = perf.db.all()
        p_marks = sub.get(id)
        #print(p_marks)
        for data in item:
            for data2 in data['sub_details']:
                #print(data2)
                if data2['sub_id'] == id:
                    if data2['obtained_marks']>p_marks['passing_marks']:
                        data2.update(result="pass")
                    else:
                        data2.update(result="fail")
        #print(item)
        return item



res = Result()
res.one_student(2)
res.one_subject(4)
