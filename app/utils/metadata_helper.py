import json

def fetch_metadata():
    f = open("app/metadata/courses.json")
    courses = json.load(f)
    f.close()
    return courses

def fetch_course_data(code):
    courses = fetch_metadata()
    course = courses.get(code)
    if course:
        return course
    raise ValueError("No Course Found!")