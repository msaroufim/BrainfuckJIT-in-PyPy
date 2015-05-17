#Implementing BrainFuck in PyPy

In what follows we will be implementing a simple interpreted language using PyPy which is a set of tools for implementing interpreters. The exposition follows [PyPy Status Blog: Writing an interpreter with PyPy by Carl Friedrich Bolz](http://morepypy.blogspot.com/2011/04/tutorial-writing-interpreter-with-pypy.html)

##BrainFuck features

The language consists in a sequence of tapes that can hold integer values and a single pointer to one of the cells. Even with such a simple model we will have IO operations, looping and branching and assignment.

* > Moves the tape pointer one cell to the right
* < Moves the tape pointer once cell to the left 
* + Increment the value of the cell underneath the pointer
* - Decrement the value of the cell underneath the pointer
* [ If the value under the cell is 0, skip to the instruction after the matching ]
* ] Skip back to matching [
* . Print out a single byte to stdout from the current cell
* , Read in a single byte from stdin  from the current cell

##Usage

```
python evalloop.py 99beer.b
```

This implementation is very slow so feel free to instead use the below to have a better idea of what's going on underneath the blinking cursor.

```python
python -m trace --trace evalloop.py 99beer.b
```

##How to build it

###Implementing the tape

Checkout the ```Tape``` class and the rest won't need to much imagination

```python
def __init__(self):
        """
        Pointer starts at first cell
        Tape starts out as all 0
        """
        self.thetape = [0]
        self.position = 0
```

###Main loop

We initialize an empty tape and iterate over each character of code using the program counter.

```python
tape = Tape()
    pc   = 0
    while pc < len(program):
        code = program[pc]
```


Assignment is easy

```python
 if code == ">":
    tape.advance()
```

So is IO

```python
elif code == ".":
    sys.stdout.write(chr(tape.get()))
```

For looping we need a way to keep track of matching brackets and we do this via a simple stack when parsing the program and we will pass the matching brackets in a dictionary form to the main loop.

##PyPy translation

The above was undoubtedly incredibly slow, so to speed it up we'll write the above using RPython which implements a restricted subset of Python to allow speedups.

For example, we can no longer use ```sys.stdout.write``` but will instead use ```os.write```

```python
elif code == ".":
    os.write(1, chr(tape.get()))
```

More importantly, we're expected to implement three functions:

* ```target``` which returns an ```entry_point``` function
* ```entry_point``` which given a filename creates a file pointer for ```run```
* ```run``` which will ```os.read(fp)```, populate the ```program_contents```, parse it and then run evaluate it.

```pypy-evalloop.py``` contains the details

###Usage

Go ahead and download Pypy from github and run

```
python ./pypy/pypy/translator/goal/translate.py pypyevallop.py
```

The result will be an executable binary that you can then use to interpret the BrainFuck file much much faster.

```
./pypyevallop-c 99beer.b
```
