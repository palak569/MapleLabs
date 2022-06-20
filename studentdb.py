
from config import data_file
from tinydb import TinyDB, Query


class Table:
    def __init__(self, path_file):
        self.db = TinyDB(path_file)
        # self.db2 = TinyDB(data_file)
        # self.db3 = TinyDB(data_file)
        self.query = Query()
        # self.table = self.db.table()
        # self.table1 = self.db.table('Student')
        # self.table2 = self.db.table('Subject')
        # self.db1.default_table_name = 'Student'
        # self.db2.default_table_name = 'Subject'
        # self.db3.default_table_name = 'Performance'

    def table_name(self, name):
        self.db.default_table_name = name

    def get(self, id):
        items = self.db.get(doc_id=id)
        if items:
            return items
        else:
            print("id do not exist")
            return None

    def insert(self, data):
        self.db.insert(data)
        #print(self.db)

    def update(self, id, data):
        items = self.db.update(data, doc_ids=[id])
        print(items)

    def delete(self, id):
        items = self.db.remove(doc_ids=[id])
        print(items)


stud = Table(data_file)
stud.table_name('Student')
sub = Table(data_file)
sub.table_name('Subject')
perf = Table(data_file)
perf.table_name('Performance')


class StudentDB:
    def get_student_details(self, id):
        return stud.get(id)

    def get_subject_details(self, id):
        return sub.get(id)

    def get_performance_details(self, id):
        return perf.get(id)

    def post_student_details(self, data):
        stud.insert(data)

    def post_subject_details(self, data):
        sub.insert(data)

    def post_performance_details(self, data):
        perf.insert(data)

    def update_student_details(self, id, data):
        stud.update(id, data)

    def update_subject_details(self, id, data):
        sub.update(id, data)

    def update_performance_details(self, id, data):
        perf.update(id, data)


# std = StudentDB()

# std.post_student_details({'name': 'smith', 'dob': '10-05-2002', 'phone': '9448171526'})
# std.post_subject_details({'name': 'Science', 'passing_marks': 35})
# std.post_performance_details({'sub_details': [{'sub_id': 1, 'obtained_marks': 45}]})
# std.get_student_details(2)
# std.get_subject_details(2)
# std.get_performance_details(1)
# std.update_subject_details(2, {'name': 'maths'})
# Table.insert({'name': "palak", 'age': 15})
# Table2.insert({'name2': [{'n': "palak"}], 'age2': 15})
# Table2.insert({'name2': [{'n': "palak"}], 'age2': 15}, doc_id=10)
# sub.insert()
# std.update_performance_details(1, {'s_id': 2, 'obtained_marks': 39})
