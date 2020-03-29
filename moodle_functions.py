import requests
import json

key = "d60e03e078e538a5f7c52688a48fed8f"

def get_courses_list():
    request_URL = "http://192.168.2.224/moodle/webservice/rest/server.php?wsfunction=core_course_get_courses_by_field&wstoken={0}&moodlewsrestformat=json".format(key)
    resp = requests.get(request_URL)
    resp = json.loads(resp.text)

    course_list = resp["courses"][1:]

    data = []
    for c in course_list:
        c_entry = {}
        c_entry["id"] = c["id"]
        c_entry["name"] = c["fullname"]
        data.append(c_entry)

    return data

def get_course(c_id):

    request_URL = "http://192.168.2.224/moodle/webservice/rest/server.php?wstoken={0}&moodlewsrestformat=json&wsfunction=core_course_get_contents&courseid={1}".format(key, c_id)
    resp = requests.get(request_URL)
    resp = json.loads(resp.text)
    

    return {
        "overall": 1.2,
        "general":
        {
            "creator": "Галиаскаров Эдуард Геннадьевич",
            "cocreators": ["Ситанов Сергей Вячеславович", "Бобков Сергей Петрович"],
            "last_changes": "20.03.2020",
            "creators_access_freq": 10,
            "students": 16,
            "students_access_freq": 4
        },
        "content":
        {
            "short": "есть",
            "empty_modules": 0,
            "schedule": "есть",
            "plan": "есть",
            "books": "есть",
            "books_count": 5,
            "booklet": "есть",
            "booklet_count": 3,
            "lecture_notes": "есть",
            "lecture_notes_count": 18,
            "presentation": "есть",
            "presentation_count": 20,
            "final_questions": "есть",
            "hometask": "есть",
            "hometask_count": 3,
            "forum": "есть",
            "forum_posts": 3,
            "forum_comments": 14,
            "chat": "есть",
            "chat_messages": 37,
            "test": "есть",
            "test_count": 6
        }
    }
    