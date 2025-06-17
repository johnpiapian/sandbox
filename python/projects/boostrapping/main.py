from zcompiler import ZCompiler


def getZSourceCode(path):
    with open(path, "r") as f:
        return f.read()

z_code = '''
@x is 10.
@y is 20.

@z is add(@x, add(@y, @y)).
@z is mul(@x, sub(@y, 5)).

show @z.

if @z < @x: show @z
or @z > @x: show @x
or: show "nothing".

while @z > 0: @z is sub(@z, 1), show @z.

double(@a, @b): return sub(@a, @b).
'''

# interpreter = zcompiler.ZInterpreter()
# python_code = interpreter.interpret_z(z_code)
# print(python_code)

z_code = '''
@x is 10.
@y is 20.

add(@x, @y).
sub(@x, @y).
'''

compiler = ZCompiler(z_code)
compiler.compile()
compiler.print()
