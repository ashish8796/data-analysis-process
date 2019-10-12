import unicodecsv

def open_file(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)


enrollments = open_file('enrollments.csv')
daily_engagement = open_file('daily_engagement.csv')
project_submissions = open_file('project_submissions.csv')


def get_unique_student(data):
    unique_student = set()
    for data_point in data:
        unique_student.add(data_point['account_key'])
    return unique_student

len(enrollments)
unique_enrolled_students = get_unique_student(enrollments)
len(unique_enrolled_students)

len(daily_engagement)
unique_engagement_students = get_unique_student(daily_engagement)
len(unique_engagement_students)

len(project_submissions)
unique_project_submitters = get_unique_student(project_submissions)
len(unique_project_submitters)
