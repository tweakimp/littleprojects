# useful python commands

## Python Code:

- End script at this point 

  ```python
    raise Systemexit
  ```

- Variable string in one line

  ```python
    s = ("" if iterationcount == 1 else "s")
  ```
  
- Format string length, align

  ```python
    string, width = "abc", 10
    string = f"{string: <{width}}" # also > and ^ (align center)
    string = "abc       "
  ```

- Combining multiple strings
  ```python
    test = ['I', 'Like', 'Python', 'automation']
    joined = ' '.join(test)
  ```

- Set recursion limit (default 1000)
  ```python
   import sys
   sys.setrecursionlimit(999)
  ```

- List comprehensions for multidimensional arrays
  ```python
    [[a, b, c] for a in range(x + 1)
               for b in range(y + 1)
               for c in range(z + 1)
               if a + b + c != n]
  ```
  
- Remove duplicates from list while maintaining order
  ```python
    listwithduplicates = [1, 1, 2, 3, 5, 8, 8, 8, 89, 8, 9, 64, 3, 3]
    samelistwithoutduplicates = list(dict.fromkeys(listwithduplicates))
    samelistwithoutduplicates   # [1, 2, 3, 5, 8, 89, 9, 64]
  ```
  
- Stopwatch decorator:
  ```python
  from datetime import datetime
  def stopwatch(f):
    def wrap(*args, **kw):
      start = datetime.now()
      result = f(*args, **kw)
      end = datetime.now()
      print(end - start)
      return result
    return wrap
    ```
    
- Function profiler:
  ```python
  import cProfile
  cProfile.run("function()")
  ```
  
- Save data to hard drive:
  ```python
  import pickle
  a = [1, 2, 3, 4, 5]
  with open("filename.pickle", "wb") as handle:
      pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)
  with open("filename.pickle", "rb") as handle:
       b = pickle.load(handle)
  print(a == b)  # True
  ```
  
## git commands:
- fix line endings from CRLF to LF
  ```cli
    find . -name "*.py" -exec dos2unix {} \;
  ```

## Pip:

- List all packages
  ```cli
   pip freeze
  ```

- Update all packages
  ```cli
   pip freeze > requirements.txt && pip install --upgrade -r requirements.txt && rm requirements.txt
  ```
## Atom:
 
- Two commands at the same time:

  In ./atom/init.coffee:
  ```coffee
  atom.commands.add 'atom-text-editor',
  "custom:reload": (event) ->
    editorElement = atom.views.getView(atom.workspace.getActiveTextEditor())
    atom.commands.dispatch(editorElement, 'hydrogen:clear-results')
    atom.commands.dispatch(editorElement, 'hydrogen:run-all')
  ```
  In .atom/keymap.cson:
  ```cson
  'atom-text-editor':
  'f5': 'custom:reload'
  ```
