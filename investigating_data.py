import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')
    
### For each of these three tables, find the number of rows in the table and
### the number of unique students in the table. To find the number of unique
### students, you might want to create a set of the account keys in each table.

enrollment_num_rows = len(enrollments)            # Replace this with your code
unique_enrollment = set()
for enrollment in enrollments:
    unique_enrollment.add(enrollment['account_key'])
enrollment_num_unique_students = len(unique_enrollment)

print(enrollment_num_rows)
print(enrollment_num_unique_students)
    
engagement_num_rows = len(daily_engagement)          # Replace this with your code
unique_engament = set()                              # Replace this with your code
for engagement in daily_engagement:
    unique_engament.add(engagement['acct'])
engagement_num_unique_students = len(unique_engament)

print(engagement_num_rows)
print(engagement_num_unique_students)

submission_num_rows = len(project_submissions)             # Replace this with your code
unique_submission = set()                               # Replace this with your code
for submission in project_submissions:
    unique_submission.add(submission["account_key"])
submission_num_unique_students =  len(unique_submission)

print(submission_num_rows)
print(submission_num_unique_students)
 