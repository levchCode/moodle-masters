import requests
import json
import datetime

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

    info_URL = "http://192.168.2.224/moodle/webservice/rest/server.php?wstoken={0}&moodlewsrestformat=json&wsfunction=core_course_get_courses_by_field&field=id&value={1}".format(key, c_id)
    info = requests.get(info_URL)
    info = json.loads(info.text)

    

    content_URL = "http://192.168.2.224/moodle/webservice/rest/server.php?wstoken={0}&moodlewsrestformat=json&wsfunction=core_course_get_contents&courseid={1}".format(key, c_id)
    resp = requests.get(content_URL)
    resp = json.loads(resp.text)

    enrolled_url = "http://192.168.2.224/moodle/webservice/rest/server.php?wstoken={0}&moodlewsrestformat=json&wsfunction=core_enrol_get_enrolled_users&courseid={1}".format(key, c_id)
    enrolled = requests.get(enrolled_url)
    enrolled = json.loads(enrolled.text)
    num_enrolled = len(enrolled)

    assigns = 0
    empty_blocks = 0
    tests = 0
    forums = 0
    num_topics = 0
    num_replies = 0
    chats = 0
    presentations = 0
    
    for i in resp:
        if len(i["modules"]) == 0:
            empty_blocks = empty_blocks + 1
        else:

            for j in i["modules"]:
                if j["modname"] == "forum":
                    forum_URL = "http://192.168.2.224/moodle/webservice/rest/server.php?wstoken={0}&moodlewsrestformat=json&wsfunction=mod_forum_get_forum_discussions_paginated&forumid={1}".format(key, j["id"])
                    resp = requests.get(forum_URL)
                    resp = json.loads(resp.text)
                    num_topics = num_topics + len(resp["discussions"])
                    for i in resp["discussions"]:
                        num_replies = num_replies + int(i["numreplies"]) 
                    forums = forums + 1

                if j["modname"] == "chat":
                    chats = chats + 1
                if j["modname"] == "assign":
                    assigns = assigns + 1
                if j["modname"] == "quiz":
                    tests = tests + 1
                if j["modname"] == "resource":
                    for k in j["contents"]:
                        if ".ppt" in k["filename"] or ".pptx" in k["filename"]:
                            presentations = presentations + 1
                

    return {
        "overall": 1.2,
        "general":
        {
            "creator": "Не реализованно",
            "cocreators": ["Не реализованно", "Не реализованно"],
            "last_changes": datetime.datetime.fromtimestamp(info["courses"][0]["timemodified"]).strftime('%d-%m-%Y %H:%M:%S'),
            "creators_access_freq": "не реализованно",
            "students": num_enrolled,
            "students_access_freq": "не реализованно"
        },
        "content":
        {
            "short": "есть" if info["courses"][0]["summary"] != "" else "не найдено",
            "empty_modules": empty_blocks,
            "schedule": "не реализованно",
            "plan": "не реализованно",
            "books": "не реализованно",
            "books_count": "не реализованно",
            "booklet": "не реализованно",
            "booklet_count": "не реализованно",
            "lecture_notes": "не реализованно",
            "lecture_notes_count": "не реализованно",
            "presentation": "есть" if presentations !=0 else "не найдено",
            "presentation_count": presentations,
            "final_questions": "не реализованно",
            "hometask": "есть" if assigns !=0 else "не найдено",
            "hometask_count": assigns,
            "forum": "есть" if forums !=0 else "не найдено",
            "forum_posts": num_topics,
            "forum_comments": num_replies,
            "chat": "есть" if chats !=0 else "не найдено",
            "chat_messages": "не реализовано",
            "test": "есть" if tests !=0 else "не найдено",
            "test_count": tests
        }
    }
    