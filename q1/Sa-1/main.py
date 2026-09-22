class AssignmentSubmission:

    def __init__(self, student_name:str, student_id:str, assignment_title:str, due_date:str, is_submitted:bool, grade:float, submitted_files:list[str]):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = is_submitted
        self.__grade = grade
        self.__submitted_files = submitted_files

    def __validate_grade(self, grade:float)->bool:
        if 0 <= grade <= 100:
            return bool(grade)
        else:
            print("Not Graded")

    def __check_submission_status(self)->bool:
        return bool(self.__is_submitted)

    def __is_duplicate(self, filename:str)->bool:
        return bool(filename in self.__submitted_files)

    def add_file(self, filename:str):
        if self.__is_duplicate(filename):
            print("File", filename, "has already been submitted.")
        else:
            self.__submitted_files.append(filename)
            self.__is_submitted = True

    def remove_file(self, filename:str):
        if self.__grade: 
            print("Cannot remove", filename, ": submission has already been graded.")
            return
        if self.__is_duplicate(filename):
            self.__submitted_files.remove(filename)
            if not self.__submitted_files:
                self.__is_submitted = False
        else:
            print("File",filename, "not found in submitted files.")

    def assign_grade(self, score:float):
        if self.__check_submission_status():
            if self.__validate_grade(score):
                self.__grade = score

    def get_grade(self):
        return self.__grade
    def view_files(self):
        return self.__submitted_files

    def get_status_report(self):
        status = f"Submitted({len(self.__submitted_files)})" if self.__is_submitted else "Missing"
        grade_display = self.__grade if self.__grade else "Not-Graded"
        return f"ID: {self.student_id} | {self.student_name} | Status: {status} | Grade: {grade_display}"

print("---INITIALIZING DROPBOX FOR STUDENTS---")
student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01", is_submitted=True, grade=0, submitted_files=[])
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date="2026-10-01", is_submitted=False, grade=0, submitted_files=[])
student3 = AssignmentSubmission(student_name="Juan dela Cruz", student_id="pshs-1033-x", assignment_title="CS-101", due_date="2026-10-01", is_submitted=False, grade=0, submitted_files=[])
student4 = AssignmentSubmission(student_name="Maria Santos", student_id="pshs-1044-x", assignment_title="CS-101", due_date="2026-10-01", is_submitted=False, grade=0, submitted_files=[])
student5 = AssignmentSubmission(student_name="Jose Reyes", student_id="pshs-1055-x", assignment_title="CS-101", due_date="2026-10-01", is_submitted=False, grade=0, submitted_files=[])
print()

print("---TEST SCENARIO 1: Multiple Files from List---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("---TEST SCENARIO 2: Removing Files from List---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("---TEST SCENARIO 3: Preventing Duplicate Files---")
student3.add_file("script.py")
student3.add_file("script.py")  #this should trigger a private duplicate check
print(f"Juan's Files: {student3.view_files()}\n")

print("---TEST SCENARIO 4: Removing file after being graded---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf")  #blocked by grading status
print()

print("---TEST SCENARIO 5: Empty list handling---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100) # Should fail because list is empty
print()

print("---FINAL SYSTEM REPORT---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())
