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
