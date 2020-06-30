import argparse
import importlib
import inspect


def main(solutionName):
    print(f"Running solution {solutionName}")
    klass = importlib.import_module(f'{solutionName}.solution').Solution
    cases = importlib.import_module(f'{solutionName}.test_cases').cases

    sol = klass()
    # Such a hack, we always assume there is only one instance
    # method inside solution
    methodName = inspect.getmembers(sol, predicate=inspect.ismethod)[0][0]
    method = getattr(sol, methodName)
    for inputs, expected in cases:
        res = method(*inputs)
        try:
            print("----------------- passed")
            assert(res == expected)
        except AssertionError:
            print(
                f"Test case failed for {input} got -> {res} "
                 "expected -> {expected}"
            )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    help_doc = "Solution to execute (give directory name to " \
               "execute the test_cases)"
    parser.add_argument(
        "solutionName",
        help=help_doc,
        type=str
    )
    args = parser.parse_args()
    main(args.solutionName)
