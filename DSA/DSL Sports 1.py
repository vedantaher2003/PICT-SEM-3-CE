universal = int(input("TOTAL NUMBER OF STUDENTS IN 2nd YEAR:- "))

print("give number of students playing cricket:- ")
lst_c = []  # CRICKET
n = int(input())
for i in range(0, n):
    d = str(input("Enter name of the student playing CRICKET :\n"))
    if d not in lst_c:
        lst_c.append(d)
print("ur final cricket list is-", lst_c)

print("give number of students playing badminton:- ")
lst_b = []  # BADMINTON
m = int(input())
for j in range(0, m):
    e = str(input("Enter name of the student playing BADMINTON : \n"))
    if e not in lst_b:
        lst_b.append(e)
print("ur final badminton list is-", lst_b)

print("give number of students playing football:- ")
lst_f = []  # FOOTBALL
p = int(input())
for k in range(0, p):
    f = str(input("Enter name the of student playing FOOTBALL: \n"))
    if f not in lst_f:
        lst_f.append(f)
print("ur final football list is-\n\n ", lst_f)


# intersection function

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


# union function

def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list


C_union_B = Union(lst_c, lst_b)
Universal = Union(C_union_B, lst_f)

print("Your UNIVERSAL LIST is---->  \n\n", Universal)


ch = "yes"

while (ch == "yes"):
    Menu = int(input('''Select any one:-
    PRESS_1- For list of students who play both CRICKET and BADMINTON
    PRESS_2- For list os students who play,either CRICKET or BADMINTON
    PRESS_3- For list of students who play neither CRICKET nor BADMINTON
    PRESS_4- For list of students who play CRICKET and FOOTBALL but not Badminton \n\n '''))

    if Menu == 1:
        # PART_1---->  C intersection B:-

        list_1 = intersection(lst_c, lst_b)
        print("PART(I)-->List of students who play both CRICKET and BADMINTON is :- \n\n", list_1)

    elif Menu == 2:
        # PART_2---->   (C u B ) - (C intersection B):-

        C_union_B = Union(lst_c, lst_b)

        list_2 = []

        list_1 = intersection(lst_c, lst_b)
        for i in C_union_B:
            if i not in list_1:
                list_2.append(i)
        print("List os students who play,either CRICKET or BADMINTON is :- \n", list_2)


    elif Menu == 3:
        #  PART_3----> (Universal) - (C u B) :-

        list_3 = list(set(Universal) - set(C_union_B))
        print("PART(III)-->List of students who play neither CRICKET nor BADMINTON :-\n\n", list_3)

    elif Menu == 4:

        # PART_4----> (C i F) - (C i B i F) :-

        C_i_F = intersection(lst_c, lst_f)
        C_i_F_i_B = intersection(C_i_F, lst_b)
        list_4 = list(set(C_i_F) - set(C_i_F_i_B))
        print('''PART(IV)-->List of students who play CRICKET and FOOTBALL but not Badminton is :- \n\n''')

    ch = input("Tpye 'yes'---> To Continue or Type 'no'---> To discontinue\n")
















