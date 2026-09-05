from abc import ABC, abstractmethod


class Builder(ABC):
    def build(self):
        self.test()
        self.lint()
        self.assemble()
        self.deploy()

    @abstractmethod
    def test(self):
        pass

    @abstractmethod
    def lint(self):
        pass

    @abstractmethod
    def assemble(self):
        pass

    @abstractmethod
    def deploy(self):
        pass


class AndroidBuilder(Builder):
    def test(self):
        print("Running Android tests")

    def lint(self):
        print("Linting Android code")

    def assemble(self):
        print("Assembling Android build")

    def deploy(self):
        print("Deploying Android build")


AndroidBuilder().build()
