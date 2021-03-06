import unicodecsv

def open_file(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)
enrollments = open_file('enrollments.csv')
daily_engagement = open_file('daily_engagement.csv')
project_submissions = open_file('project_submissions.csv')
print(enrollments[1])
print(daily_engagement[1])
print(project_submissions[1])