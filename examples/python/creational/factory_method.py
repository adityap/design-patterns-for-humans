from abc import ABC, abstractmethod


class Interviewer(ABC):
    @abstractmethod
    def ask_questions(self):
        pass


class Developer(Interviewer):
    def ask_questions(self):
        print("Asking about design patterns")


class HiringManager(ABC):
    @abstractmethod
    def make_interviewer(self):
        pass

    def take_interview(self):
        self.make_interviewer().ask_questions()


class DevelopmentManager(HiringManager):
    def make_interviewer(self):
        return Developer()


DevelopmentManager().take_interview()
