# Theory question 1
## The large module
We have learned, that most of the time and work investment in case of software design is invested in the maintenance
of the software. For this we have to respect the software design principles so that later in the lifecycle it is
possible to flexibly maintain the software.

### Problems whit the module
* Lack of documentation: a complicated, long module has to be probably looked through for the functionality 
  to be understood, if there is a need to adjust or debug. To read a long, complicated code is much more difficult
  than to read a documentation, so the adjustment will take more time. Sometimes faulty implementation can be spotted
  if it is clear from the documentation, what the intention was.
  
* Very long methods: to easily understand a method, it needs to be of a manageable size. A multiple hundred lines code 
  is not easy to understand anymore and probably possible to be implemented in separate functionalities, which can
  be managed better separately.
  
### Not respected design principles
* KISS: "Keep it simple and short" is clearly not respected here with multiple hundred line methods. Without knowing
  the exact contents it is difficult to judge, but most probably it would be possible to implement the code in more 
  parts in separate functions where each one solves one problem.
  
* DRY/YAGNI: Whit a complicated, long code that is not well documented, it is possible, that some parts were repeated
  (DRY), or some parts were written unnecessarily (YAGNI).
  
* Single Responsibility Principle: If there are very few classes, it might be that in case of changes in the past 
  the changes or extensions were hard-coded into the classes, even if it had been reasonable to implement new 
  classes for the required new responsibilities.
  
# Theory question 2

## So your boss wants you to implement the next feature...
...but you have no time to completely revision/rewrite your module...

### What would be your approach?
Since my boss wants me to implement something new in something soo complex/hard to understand, I, still, would take my
time to kind of start a little refactoring now and then. Meaning just doing little code adjustment to make it
easier (for me) to work with it. For now as well as in the future. While doing that, working through
the already written code, I also hope that the code gets clearer to me, and I kind of know where I can find what.
To keep the refactoring small and not change too much (and doing this next to my normal programming time, so my boss
truly believes I am just working on the new feature) I would consider the possibilities after Martin Fowler (or rather
the book from him with Kent Beck); combine methods, (re-)structure the data, maybe simplify some method calls or
expressions... And for the new code in the new feature, I would definitely consider the design principles and work with
them rather than against them (like the colleague/s before me did).