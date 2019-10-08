import unicodecsv

with open('enrollments.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)

with open('daily_engagement.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    daily_engagement = list(reader)

with open('project_submissions.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    project_submissions = list(reader)


print(enrollments[0])
print(daily_engagement[0])
print(project_submissions[0])
    
daily_engagement = None     # Replace this with your code
project_submissions = None  # Replace this with your cod