# LexicographicSort
  - Call lexicographicSort(strList, lexicoIndex) to start sorting
  - Arguments
    - strList: a list of string to sort. Assume that elements in this list contains only chars in lexicoIndex
    - lexicoIndex: a string. The function sorts in order of characters in this string. 
      - For example, 'dcba' means that 'd' comes first, 'c' for the next, 'b', then 'a' in order.
      - '' comes first than any other strings
  - Return: a sorted list of strList in order of lexicoIndex
  - Example: 
    - lexicographicSort(['c', '', 'dc', 'd'], 'dc') -> ['', 'd', 'dc', 'c']
