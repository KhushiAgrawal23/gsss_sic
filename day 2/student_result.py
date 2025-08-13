'''
accept the average score of the student and print the result as follows:
0 to 59 Fail
60 to 84 second class
85 to 95 first class
96 to 100 excellent
also check for invalid score. No negative marking
'''

average_score = int(input('enter your average score to print the result:'))
if average_score <0 or average_score > 100:
    print('Invalid score')
elif average_score >=0 and average_score <=59:#when checking for particular range then and
     print('result is fail')
elif average_score >= 60 and average_score <= 84:
     print('result is second class')
elif average_score >= 85 and average_score <= 95:
     print('result is first class')
else:
     print('result is excellent')