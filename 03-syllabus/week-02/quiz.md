# Quiz 02

Test your understanding of the Python data model, typing, and generator internals. Record your answers before checking with your learning partner.

1. What is the fundamental difference between calling `f.readlines()` versus iterating over `f` with `for line in f:`?
   a) `f.readlines()` reads line-by-line while `for line in f:` loads the full file into a list.  
   b) `for line in f:` uses an iterator that reads lazily into memory, whereas `f.readlines()` loads all lines simultaneously into a list in RAM.  
   c) `for line in f:` requires binary mode `rb`.  
   d) There is zero difference; Python compiles both into identical bytecode.  
   *(Answer key: `instructor-keys/quiz-02.md`)*

2. Why should floating-point numbers (`float`) never be used to represent monetary currency?
   a) Floating-point numbers cannot store negative numbers.  
   b) Binary floating-point representation cannot represent fractional decimal values (like 0.1) exactly, leading to rounding errors.  
   c) Python floats are capped at 16-bit integers.  
   d) Modern CPUs do not support floating-point arithmetic.  
   *(Answer key: `instructor-keys/quiz-02.md`)*

3. What happens if a context manager's `__exit__` method returns `True` after an exception occurs inside the `with` block?
   a) Python raises a `TypeError`.  
   b) The exception is silently suppressed and execution continues outside the `with` block.  
   c) The exception is automatically re-raised with an amended traceback.  
   d) The interpreter immediately terminates.  
   *(Answer key: `instructor-keys/quiz-02.md`)*

4. How does `typing.Protocol` achieve static duck typing?
   a) By requiring classes to explicitly inherit from `Protocol` in their class definition.  
   b) By checking at compile/type-check time whether a class implements the specified attributes and methods, regardless of inheritance hierarchy.  
   c) By converting Python classes to C structs at runtime.  
   d) By generating automatic metaclasses on module import.  
   *(Answer key: `instructor-keys/quiz-02.md`)*

5. What distinguishes a generator function from a standard Python function?
   a) A generator function contains the `yield` keyword and returns an iterator that pauses state between executions.  
   b) Generator functions execute asynchronously on separate CPU threads.  
   c) Generator functions cannot accept arguments.  
   d) Generator functions must always return dictionaries.  
   *(Answer key: `instructor-keys/quiz-02.md`)*

6. What is the role of `__repr__` compared to `__str__` in the Python data model?
   a) `__repr__` is intended for end-users, while `__str__` is intended for developers.  
   b) `__repr__` should provide an unambiguous representation of the object (often valid Python code to recreate it) for debugging, while `__str__` is a human-readable display string.  
   c) `__repr__` is deprecated in Python 3.12.  
   d) `__str__` only works with numeric values.  
   *(Answer key: `instructor-keys/quiz-02.md`)*

7. What does setting `frozen=True` on a `@dataclass` accomplish?
   a) Compiles the class to machine code using Cython.  
   b) Prevents mutation of fields after initialization and automatically generates a `__hash__` method.  
   c) Encrypts the data in memory.  
   d) Restricts the class to single-threaded execution.  
   *(Answer key: `instructor-keys/quiz-02.md`)*

8. When raising a new exception from an existing caught exception, why should you use `raise CustomError("message") from err`?
   a) It forces Python to ignore the original error.  
   b) It explicitly links the exception causes in the traceback (exception chaining), preserving root-cause history for debugging.  
   c) It speeds up garbage collection.  
   d) It prevents the program from writing to `stderr`.  
   *(Answer key: `instructor-keys/quiz-02.md`)*
