# 1. ASSESSMENT TASKS
print("\n" + "="*40)
print("ASSESSMENT TASKS GRADE COMPUTATION")
print("-" * 40)

print("\nAssignment 1")
assign1_noi = int(input("Number of Items: "))
assign1_score = int(input("Score: "))

print("\nQuiz 1")
quiz1_noi = int(input("Number of Items: "))
quiz1_score = int(input("Score: "))

print("\nActivity 1")
act1_noi = int(input("Number of Items: "))
act1_score = int(input("Score: "))

print("\nActivity 2")
act2_noi = int(input("Number of Items: "))
act2_score = int(input("Score: "))

print("\nActivity 3")
act3_noi = int(input("Number of Items: "))
act3_score = int(input("Score: "))

tot_noi1 = assign1_noi + quiz1_noi + act1_noi + act2_noi + act3_noi
tot_scores1 = assign1_score + quiz1_score + act1_score + act2_score + act3_score
at_average = (tot_scores1 / tot_noi1) * 100

print("\n" + "="*40)
print(f"{'Assessment Tasks':<25} {'NOI':>5} {'Scores':>8}")
print("-" * 40)
print(f"{'Assignment 1':<25} {assign1_noi:>5} {assign1_score:>8}")
print(f"{'Quiz 1':<25} {quiz1_noi:>5} {quiz1_score:>8}")
print(f"{'Activity 1':<25} {act1_noi:>5} {act1_score:>8}")
print(f"{'Activity 2':<25} {act2_noi:>5} {act2_score:>8}")
print(f"{'Activity 3':<25} {act3_noi:>5} {act3_score:>8}")
print("-" * 40)
print(f"{'Total':<25} {tot_noi1:>5} {tot_scores1:>8}")
print(f"{'AT Average':<25} {at_average:>13.2f}%")
print("="*40)


# 2. MAJOR EXAM
print("\n" + "="*40)
print("MAJOR EXAM GRADE COMPUTATION")
print("-" * 40)

print("\nLong Exam 1")
longex1_noi = int(input("Number of Items: "))
longex1_score = int(input("Score: "))

print("\nLong Exam 2")
longex2_noi = int(input("Number of Items: "))
longex2_score = int(input("Score: "))

tot_noi2 = longex1_noi + longex2_noi
tot_scores2 = longex1_score + longex2_score
lex_average = (tot_scores2 / tot_noi2) * 100

print("\n" + "="*40)
print(f"{'Major Exam':<25} {'NOI':>5} {'Scores':>8}")
print("-" * 40)
print(f"{'Long Exam 1':<25} {longex1_noi:>5} {longex1_score:>8}")
print(f"{'Long Exam 2':<25} {longex2_noi:>5} {longex2_score:>8}")
print("-" * 40)
# FIX: Changed tot_noi1/tot_scores1 to tot_noi2/tot_scores2 below
print(f"{'Total':<25} {tot_noi2:>5} {tot_scores2:>8}")
print(f"{'LEX Average':<25} {lex_average:>13.2f}%")
print("="*40)


# 3. DEPARTMENTAL EXAM
print("\n" + "="*40)
print("DEPARTMENTAL EXAM GRADE COMPUTATION")
print("-" * 40)

print("\nDepartmental Exam")
depex_noi = int(input("Number of Items: "))
depex_score = int(input("Score: "))

dexm_average = (depex_score / depex_noi) * 100

print("\n" + "="*40)
print(f"{'Departmental Exam':<25} {'NOI':>5} {'Scores':>8}")
print("-" * 40)
print(f"{'Departmental Exam':<25} {depex_noi:>5} {depex_score:>8}")
print("-" * 40)
print(f"{'Total':<25} {depex_noi:>5} {depex_score:>8}")
print(f"{'DEXM Average':<25} {dexm_average:>13.2f}%")
print("="*40)


# 4. FINAL GRADE
at_percentage = at_average * 0.40
lex_percentage = lex_average * 0.40
dexm_percentage = dexm_average * 0.20

final_grade = at_percentage + lex_percentage + dexm_percentage

print("\n" + "="*40)
print("FINAL GRADE SUMMARY")
print("-" * 40)
print(f"{'Assessment Tasks (40%)':<25} {at_percentage:>13.2f}%")
print(f"{'Major Exams (40%)':<25} {lex_percentage:>13.2f}%")
print(f"{'Departmental Exam (20%)':<25} {dexm_percentage:>13.2f}%")
print("-" * 40)
print(f"{'FINAL GRADE':<25} {final_grade:>13.2f}%")
print("="*40)
