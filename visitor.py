import operator
from forthVisitor import forthVisitor as GeneratedVisitor


class ForthInterpreter(GeneratedVisitor):

    def __init__(self):
        self._stack = []
        self._output = []
        self._call_stack = []
        self._builtins = self._init_builtins()
        self._procedures = {}

    def _push(self, v):
        self._stack.append(v)

    def _pop(self):
        if not self._stack:
            raise RuntimeError("pila buida!")
        return self._stack.pop()

    def _peek(self, n=0):
        if len(self._stack) <= n:
            raise RuntimeError("pila buida!")
        return self._stack[-(n + 1)]

    def _binary_op(self, op, ret_bool=False, check_div=False):
        def operation():
            b = self._pop()
            a = self._pop()
            if check_div and b == 0:
                raise RuntimeError("divisió per zero!")
            result = op(a, b)
            if ret_bool:
                self._push(-1 if result else 0)
            else:
                self._push(int(result))
        return operation

    def _op_swap(self):
        a, b = self._pop(), self._pop()
        self._push(a)
        self._push(b)

    def _op_rot(self):
        c, b, a = self._pop(), self._pop(), self._pop()
        self._push(b)
        self._push(c)
        self._push(a)

    def _op_dup(self):
        self._push(self._peek())

    def _op_over(self):
        self._push(self._peek(1))

    def _op_drop(self):
        self._pop()

    def _op_2dup(self):
        self._push(self._peek(1))
        self._push(self._peek(1))

    def _op_2drop(self):
        self._pop()
        self._pop()

    def _op_2swap(self):
        d, c, b, a = self._pop(), self._pop(), self._pop(), self._pop()
        self._push(c)
        self._push(d)
        self._push(a)
        self._push(b)

    def _op_2over(self):
        self._push(self._peek(3))
        self._push(self._peek(3))

    def _op_and(self):
        b, a = self._pop(), self._pop()
        self._push(-1 if (a == -1 and b == -1) else 0)

    def _op_or(self):
        b, a = self._pop(), self._pop()
        self._push(-1 if (a == -1 or b == -1) else 0)

    def _op_not(self):
        self._push(-1 if self._pop() == 0 else 0)

    def _op_dot(self):
        self._output.append(str(self._pop()))

    def _op_dots(self):
        self._output.append(str(self._stack))

    def _op_recurse(self):
        if not self._call_stack:
            raise RuntimeError("'recurse' fora d'un procediment!")
        self._run(self._procedures[self._call_stack[-1]])

    def _init_builtins(self):
        return {
            '+': self._binary_op(operator.add),
            '-': self._binary_op(operator.sub),
            '*': self._binary_op(operator.mul),
            '/': self._binary_op(operator.floordiv, check_div=True),
            'mod': self._binary_op(operator.mod, check_div=True),
            '<': self._binary_op(operator.lt, ret_bool=True),
            '>': self._binary_op(operator.gt, ret_bool=True),
            '=': self._binary_op(operator.eq, ret_bool=True),
            '<>': self._binary_op(operator.ne, ret_bool=True),
            '<=': self._binary_op(operator.le, ret_bool=True),
            '>=': self._binary_op(operator.ge, ret_bool=True),
            'and': self._op_and,
            'or': self._op_or,
            'not': self._op_not,
            'dup': self._op_dup,
            'drop': self._op_drop,
            'swap': self._op_swap,
            'over': self._op_over,
            'rot': self._op_rot,
            '2dup': self._op_2dup,
            '2drop': self._op_2drop,
            '2swap': self._op_2swap,
            '2over': self._op_2over,
            '.': self._op_dot,
            '.s': self._op_dots,
            'recurse': self._op_recurse,
        }

    def _run(self, body_list):
        if body_list:
            for item in body_list:
                self.visit(item)

    def _call_word(self, word):
        if word in self._procedures:
            self._call_stack.append(word)
            try:
                self._run(self._procedures[word])
            finally:
                self._call_stack.pop()
        elif word in self._builtins:
            self._builtins[word]()
        else:
            raise RuntimeError(f"procediment '{word}' no definit!")

    def get_output(self):
        return '\n'.join(self._output)

    def visitPushNumber(self, ctx):
        self._push(int(ctx.NUMBER().getText()))

    def visitDefFunc(self, ctx):
        self._procedures[ctx.ID().getText()] = ctx.body()

    def visitCallFunc(self, ctx):
        self._call_word(ctx.ID().getText())

    def visitBodyNumber(self, ctx):
        self._push(int(ctx.NUMBER().getText()))

    def visitBodyCall(self, ctx):
        self._call_word(ctx.ID().getText())

    def visitConditional(self, ctx):
        cond = self._pop()
        if cond != 0:
            self._run(ctx.thenBlock)
        else:
            self._run(ctx.elseBlock)
