from studentdb import StudentDB, stud, sub, perf
from result import res


def test_student_id():
    data = stud.get(1)
    assert data is not None

def test_subject_id():
    data = sub.get(9)
    assert data is not None

def test_one_subject_result():
    data = res.one_subject(4)
    print(data)
    for t_dict in data:
        print(t_dict)
        for t_dict2 in t_dict['sub_details']:
            if 'result' in t_dict2:
                t_dict3 = t_dict2
                assert t_dict3['result'] == "pass"
