# Quiz
score = 100
late_record = False
swim_good = False
basketball_good = False

if score >= 90 and not late_record:
    print("Group A")
elif swim_good or basketball_good:
    print("Group B")
else:
    print("Group C")
