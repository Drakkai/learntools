from learntools.core import *
from learntools.core.problem import injected

class ExerciseFormatTutorial(EqualityCheckProblem):
    _var = 'color'
    _expected = 'blue'
    _hint = "Your favorite color rhymes with *glue*."
    _solution = CS('color = "blue"')

class CircleArea(EqualityCheckProblem):
    _vars = ['radius', 'area']
    _expected = [3/2, (3/2)**2 * 3.14159]

    _hint = "The syntax to raise a to the b'th power is `a ** b`"
    _solution = CS('radius = diameter / 2',
            'area = pi * radius ** 2')

class VariableSwap(CodingProblem):
    _vars = ['a', 'b']

    _hint = "Try using a third variable."
    _solution = """The most straightforward solution is to use a third variable to temporarily store one of the old values. e.g.:

    tmp = a
    a = b
    b = tmp

If you're familiar with Python, you might have seen this:

    a, b = b, a
"""

    @injected
    def store_original_ids(self, a, b):
        self.id_a = id(a)
        self.id_b = id(b)

    def check(self, a, b):
        ida = id(a)
        idb = id(b)
        orig_values = [1, 2, 3], [3, 2, 1]
        if ida == self.id_b and idb == self.id_a:
            return
        assert not (ida == self.id_a and idb == self.id_b), ("`a` and `b` still"
                " have their original values.")
        orig_ids = (self.id_a, self.id_b)
        if (b, a) == orig_values:
            # well this is ridiculous in its verbosity
            assert False, (
        "Hm, did you write something like...\n"
        "```python\na = [3, 2, 1]\nb = [1, 2, 3]```\n?\n"
        "That's not an unreasonable think to try, but there are two problems:\n"
        "1. You're relying on knowing the values of `a` and `b` ahead of time."
        " What if you wanted to swap two variables whose values weren't known"
        " to you ahead of time?\n"
        "2. Your code actually results in `a` referring to a *new* object (whose value is the same as `b`'s previous value), and similarly for `b`. To see why this is, consider that the code...\n"
        "```python\n"
        "a = [1, 2, 3]\n"
        "b = [1, 2, 3]```\n"
        "Is actually *different* from:\n"
        "```python\n"
        "a = [1, 2, 3]\n"
        "b = a```\n"
        "In the second case, `a` and `b` refer to the same object. In the first case, `a` and `b` refer to different objects which happen to be equivalent. This may seem like a merely philosophical difference, but it matters when we start *modifying* objects. In the second scenario, if we run `a.append(4)`, then `a` and `b` would both have the value `[1, 2, 3, 4]`. If we run `a.append(4)` in the first scenario, `a` refers to `[1, 2, 3, 4]`, but `b` remains `[1, 2, 3]`. (We'll talk more about lists and mutability in a later lesson.)"
        )
        assert ida in orig_ids, ("`a` was assigned something weird (its id has changed,"
                " but to something other than `b`'s id)")
        assert idb in orig_ids, ("`b` was assigned something weird (its id has changed,"
                " but to something other than `a`'s id)")
        assert ida != idb, "`b` and `a` are the same! Both have value `{}`".format(
                repr(a))
        assert False, "This fails in a way we did not anticipate!"

# It's an interesting question whether to make these parens questions checkable.
# Making them non-checkable for now.
class ArithmeticParensEasy(ThoughtExperiment):
    _hint = ('Following its default "BEDMAS"-like rules for order of operations,'
            ' Python will first divide 3 by 2, then subtract the result from 5.'
            ' You need to add parentheses to force it to perform the subtraction first.')
    _solution = CS("(5 - 3) // 2")

class ArithmeticParensHard(ThoughtExperiment):
    _hint = 'You may need to use several pairs of parentheses.'
    _solution = "`(8 - 3) * (2 - (1 + 1))` is one solution. There may be others."

ArithmeticParens = MultipartProblem(ArithmeticParensEasy, ArithmeticParensHard)

class CandySplitting(EqualityCheckProblem):
    _var = 'to_smash'
    _expected = (121 + 77 + 109) % 3
    _default_values = [-1]

    _hints = [
            "You'll probably want to use the modulo operator, `%`.",
            "`j % k` is the remainder after dividing `j` by `k`",
    ]
    _solution = CS("(alice_candies + bob_candies + carol_candies) % 3")


qvars = bind_exercises(globals(), [
    ExerciseFormatTutorial,
    CircleArea,
    VariableSwap,
    ArithmeticParens,
    CandySplitting,
    ],
    start=0,
    )
__all__ = list(qvars)
