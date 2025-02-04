
# Execution time decorator

Just a decorator for printing the execution time of your python functions.


## Use

Download the file and add it to your project, then import the decorator.

```bash
  from timer import timer


  @timer
  def my_func(ex_arg):
      ...
```
 Every time your function is used, you will se something like this on your console:
 ```bash
  Execution time of "my_func" was 0.000016743 seconds
```
        
