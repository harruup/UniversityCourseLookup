import re

#Previously offered and PRIOR to summer can be taken care of by removing the matching 4101etc
courses = []
prereqs = []
coursedesc = 'Amortized and worst-case analysis of data structures. Data structuring paradigms: self-adjustment and persistence. Lists: self-adjustment with the move-to-front heuristic. Search trees: splay trees, finger search trees. Heaps: skew heaps, Fibonacci heaps. Union-find trees. Link-and-cut trees. Multidimensional data structures and dynamization. Integrated with: GS/CSE 5101 3.00. Prerequisites: cumulative GPA of 4.50 or better over all major EECS courses (without second digit "5"); LE/EECS 2030 3.00 or LE/EECS 1030 3.00; LE/EECS 2001 3.00, LE/EECS 3101 3.00. Previously offered as: LE/CSE 4101 3.00. PRIOR TO SUMMER 2013: SC/CSE 4101 3.00.'
coursecode = "LE/EECS 4101"
if re.search("Corequisite:|Corequisites:", coursedesc):
    descsplit = re.split("(Corequisite:|Corequisites:)(?i)", coursedesc)
else:
    descsplit = re.split("(Course Credit (Exclusion:|Exclusions:))(?i)", coursedesc)
if re.search("Integrated with: [A-Z][A-Z]/[A-Z][A-Z][A-Z]* *[0-9][0-9][0-9][0-9]", descsplit[0]):
    descsplit = re.split("Integrated with: [A-Z][A-Z]/[A-Z][A-Z][A-Z]* *[0-9][0-9][0-9][0-9]", descsplit[0])
    prereq = re.findall("[A-Z][A-Z]/[A-Z][A-Z][A-Z]* *[0-9][0-9][0-9][0-9]", descsplit[1])
elif re.search("(Prerequisite:|Prerequisites:)", descsplit[0]):
    prereq = re.findall("[A-Z][A-Z]/[A-Z][A-Z][A-Z]* *[0-9][0-9][0-9][0-9]", descsplit[0])
else:
    prereq = "X"
for p in prereq:
    courses.append(coursecode)
    prereqs.append(str(p))
    print(coursecode+"->"+p)


