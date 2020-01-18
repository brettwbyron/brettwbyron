tests = [["Student A", 71],["Student B", 89],["Student C", 68], \
         ["Student D", 80],["Student E", 98],["Student F", 53], \
         ["Student G", 89],["Student H", 83],["Student I", 97], \
         ["Student J", 17],["Student K", 70],["Student L", 93], \
         ["Student M", 63],["Student N", 76],["Student O", 39]]

print "Before Sort"
for test in tests:
    student, score = test
    print student, "got a", score
print "-"*20

#sort the list by high score to low score

print "After Sort"
for test in tests:
    student, score = test
    print student, "got a", score
print "-"*20

#compute the average

print "The average:"
