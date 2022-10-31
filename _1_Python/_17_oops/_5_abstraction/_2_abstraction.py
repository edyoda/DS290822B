from abc import ABC,abstractmethod 

class college:

    def timing(self):
        return "10am - 1pm"

    @abstractmethod
    def exam_ticket(self):
        pass


class classroom_A(college):
    def exam_ticket(self):
        return "IT Exam Ticket"

class classroom_B(college):
    def exam_ticket(self):
        return "CS Exam Ticket"

class classroom_C(college):
    def exam_ticket(self):
        return "BSC Exam Ticket"

a_obj = classroom_A()
print(a_obj.timing())
print(a_obj.exam_ticket())

b_obj = classroom_B()
print(b_obj.timing())
print(b_obj.exam_ticket())
