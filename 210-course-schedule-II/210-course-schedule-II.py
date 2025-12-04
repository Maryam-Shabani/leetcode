class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependencies = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for course,  prerequisite in prerequisites:
            dependencies[prerequisite].append(course)
            indegrees[course] +=1
        possible_courses = [course for course in range(numCourses) if indegrees[course] == 0]
        taken_courses = []
        while possible_courses:
            next_course = possible_courses.pop()
            print(next_course)
            taken_courses.append(next_course)
            for dependent_course in dependencies[next_course]:
                indegrees[dependent_course] -= 1
                if indegrees[dependent_course] == 0:
                    possible_courses.append(dependent_course)
                    
        return taken_courses if len(taken_courses) == numCourses else []