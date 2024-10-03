# Lists in Python

- **Lists** allow us to store multiple values in a single variable. Each value in a list is called an element, and the elements can be of any data type (e.g., integers, floats, strings, etc.).
  
```python
marks1 = 12
marks2 = 56.5
marks3 = 46.9
marks4 = 43 
marks = [12, 56.5, 46.9, 43]  # List of marks
print(marks)
```

## Different Types of Lists

1. **Empty List**:
   ```python
   my_list = []
   ```

2. **Integer List**:
   ```python
   my_list = [1, 2, 3, 4, 5]
   ```

3. **String List**:
   ```python
   my_list = ['apple', 'banana', 'mango']
   ```

4. **Mixed-Type List**:
   - Lists can hold multiple data types.
   ```python
   my_list = [1, "ali", "ahmad", 3.4, True]
   ```

## Indexing and Slicing in Lists

1. **Accessing Elements**:
   - To access individual elements of a list, you use **indexing**. The index starts from `0`.
   ```python
   first_element = my_list[0]  # Returns the first element
   ```

2. **Slicing**:
   - You can access a range of elements using slicing. 
   ```python
   subset = my_list[1:3]  # Returns a subset of elements
   ```

3. **Negative Indexing**:
   - Use negative indexing to access elements from the end of the list.
   ```python
   last_element = my_list[-1]  # Returns the last element
   ```

## List Methods

- Lists come with built-in methods for various operations.

1. **Append**:
   - Add an element to the end of the list.
   ```python
   my_list.append('new_element')
   ```

2. **Extend**:
   - Add multiple elements to the list.
   ```python
   my_list.extend([4, 5, 6])
   ```

3. **Insert**:
   - Insert an element at a specific index.
   ```python
   my_list.insert(2, 'new_element')
   ```

4. **Remove**:
   - Remove an element from the list.
   ```python
   my_list.remove('element')
   ```

5. **Sort**:
   - Sort the list in ascending order.
   ```python
   my_list.sort()
   ```

6. **Reverse**:
   - Reverse the elements in the list.
   ```python
   my_list.reverse()
   ```

---

# Tuples in Python

- **Tuples** are similar to lists, but they are **immutable**, meaning their elements cannot be changed once assigned.
- Tuples are defined by placing elements inside parentheses `()` instead of square brackets `[]`.

## Tuple Examples

1. **Creating Tuples**:
   ```python
   my_tuple = (1, 2, 3)
   ```

2. **Accessing Elements**:
   - You can access tuple elements using indexing just like lists.
   ```python
   first_element = my_tuple[0]
   ```

3. **Immutability**:
   - You cannot modify tuple elements.
   ```python
   my_tuple[0] = 10  # This will raise an error
   ```

4. **Tuple Methods**:
   - Tuples support fewer methods because of their immutability.
   - Common methods include `.count()` and `.index()`.
   ```python
   my_tuple.count(1)  # Counts occurrences of 1
   my_tuple.index(2)  # Finds the index of 2
   ```

---

## Real-World Examples

1. **Storing Student Marks**:
   ```python
   marks = [90, 85, 95, 88]
   ```

2. **Shopping List**:
   ```python
   fruits = ['apple', 'banana', 'orange']
   ```

3. **Student Records** (using a list of dictionaries):
   ```python
   records = [{'name': 'Ali', 'age': 16}, {'name': 'Ahmad', 'age': 17}]
   ```

In summary:
- **Lists** are mutable and allow various data types to be stored.
- **Tuples** are immutable, useful for data that shouldn't be changed.