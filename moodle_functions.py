import requests

def get_courses_list():
    #Черная магия с мудлом
    return [
        {"id": 1, "name": "Инженерия ИС", "score": 1.2},
        {"id": 2, "name": "Формальные языки и грамматики", "score": 4},
    ]

def get_course(c_id):
    #Черная магия с мудлом

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
    