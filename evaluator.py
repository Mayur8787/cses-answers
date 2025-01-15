import os
import sys
import zipfile
import argparse


class Evaluator:
    """
    Evaluator to evaluate solutions on given testcases.
    path: str = Path of the solution folder.
    """

    def __init__(self, path):
        self.path = path

    def get_solution_module(self):
        file_path = os.path.join(self.path, "solution.py")
        if not os.path.exists(file_path):
            raise FileNotFoundError("Solution file does not exist.")

        origin_path = sys.path.copy()
        sys.path.insert(0, self.path)

        try:
            module = __import__("solution")
        finally:
            sys.path = origin_path

        return module

    def get_tests(self):
        file_path = os.path.join(self.path, "tests.zip")
        if not os.path.exists(file_path):
            raise FileNotFoundError("tests.zip file does not exist.")

        tests = []

        with zipfile.ZipFile(file_path, "r") as zf:
            end = len(zf.namelist())
            for index in range(1, (end // 2) + 1):
                entry = {}
                with zf.open(f"{index}.in", "r") as file:
                    content = file.read()
                    entry["input"] = content.decode("utf-8")
                with zf.open(f"{index}.out", "r") as file:
                    content = file.read()
                    entry["output"] = content.decode("utf-8").strip()
                tests.append({index: entry})
        return tests

    def evaluate(self):
        """
        Helper function to evaluate the given code against given tests.
        """

        module = self.get_solution_module()

        if not hasattr(module, "Solution"):
            raise AttributeError(f"{module} does not contains Solution class.")

        obj = module.Solution()

        tests = self.get_tests()

        for item in tests:
            for index, test in item.items():
                inp = test["input"]
                output = test["output"]

                obj.give_input(inp)
                out = obj.solution().strip()

                if out == output:
                    print(f"Test {index} : Passed")
                else:
                    print(f"Test {index} : Failed")
                    # print(f"input: {inp}")
                    # print(f"expected output: {output}",f"actual output: {out}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path", help="Path of the folder which contains solution and tests"
    )
    args = parser.parse_args()
    obj = Evaluator(args.path)

    obj.evaluate()
