from typing import List


#prima implementazione stupida
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stu0 = students.count(0)
        stu1 = students.count(1)
        i = 0
        while (stu0 != 0 or stu1 != 0) and i < len(sandwiches):
            if sandwiches[i] == 0:
                if stu0 == 0:
                    break
                stu0 -= 1

            else:
                if stu1 == 0:
                    break
                stu1 -= 1
            i+= 1

        return stu1 + stu0


sol = Solution()
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
print(sol.countStudents(students,sandwiches))