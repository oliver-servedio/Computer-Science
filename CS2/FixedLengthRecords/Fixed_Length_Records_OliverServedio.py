
fhand = open("student_data_cs2.txt",'r')
fout = open('csv_student_data_cs2','w')

for line in fhand:
# - ID: 4 characters
    fout.write((line[0:6]).strip() + ', ')
# - FirstName: 15 characters
    fout.write((line[6:21]).strip() + ', ')
# - LastName: 15 characters
    fout.write((line[21:36]).strip() + ', ')
# - Grade: 6 characters
    fout.write((line[36:42]).strip() + ', ')
# - GPA: 6 characters
    fout.write((line[42:48]).strip() + ', ')
# - BirthDate: 12 characters
    fout.write((line[48:60]).strip() + ', ')
# - Gender: 7 character
    fout.write((line[60:67]).strip() + ', ')
# - ClassRank: 9 characters
    fout.write((line[67:76]).strip() + ', ')
# - AttendPct: 10 characters
    fout.write((line[76:86]).strip() + ', ')
# - Honors: 7 character
    fout.write((line[86:93]).strip() + ', ')
# - Sports: 9 characters
    fout.write((line[93:102]).strip() + ', ')
# - ClubCount: 9 characters
    fout.write((line[102:112]).strip() + ',  ')
    fout.write('\n')