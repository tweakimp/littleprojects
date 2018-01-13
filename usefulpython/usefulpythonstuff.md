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

- Combining multiple strings
  ```python
    test = ['I', 'Like', 'Python', 'automation']
    joined = ' '.join(test)
  ```

- Set recursion limit (default 1000)
  ```python
   import sys
   sys.setrecursionlimit(1001)
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

## Pip:

- List all packages
  ```cli
   pip freeze
  ```

- Update all packages
  ```cli
   pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
  ```
