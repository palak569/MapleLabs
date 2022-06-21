import pytest
from result import res
from studentdb import stud, sub, std


def test_student_id():
    data = stud.get(1)
    assert data is not None


def test_subject_id():
    data = sub.get(9)
    assert data is not None


@pytest.mark.parametrize('sub_id', [1, 2, 3, 4])
def test_one_subject_result(sub_id):
    data = res.one_subject(sub_id)
    print(data)
    for t_dict in data:
        print(t_dict)
        for t_dict2 in t_dict['sub_details']:
            if 'result' in t_dict2:
                t_dict3 = t_dict2
                assert t_dict3['result'] == "pass"


@pytest.mark.parametrize('stud_id', [1, 2, 3, 4])
def test_one_student_result(stud_id):
    data = res.one_student(stud_id)
    print(data)
    for t_dict in data['sub_details']:
        print(t_dict)
        if 'result' in t_dict:
            assert t_dict['result'] == "pass"
            print("-----------------------------")


def test_update_pmarks():
    std.update_subject_details(1, {"passing_marks": 30})
    data = sub.get(1)
    print(data)
    assert data['passing_marks'] == 30


def test_post_subject():
    data = std.post_subject_details({'name': 'Sociology', 'passing_marks': 35})
    t_data = sub.get(data)
    assert t_data['name'] == "Sociology"
    assert t_data['passing_marks'] == 35
