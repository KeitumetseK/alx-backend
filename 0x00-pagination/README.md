# Pagination Project

This project involves implementing various pagination techniques in Python using a dataset of popular baby names.

## Task 0: Simple Helper Function

### `index_range` function
- A simple helper function that takes `page` and `page_size` as arguments and returns a tuple containing the start and end index for the items to be displayed on the specified page.

## Task 1: Simple Pagination

### `Server` class with `get_page` method
- This class reads data from a CSV file and implements simple pagination using the `get_page` method.
- The method returns the appropriate page of the dataset based on the page number and page size provided.

## Task 2: Hypermedia Pagination

### `Server` class with `get_hyper` method
- Extends the `Server` class by adding the `get_hyper` method, which returns a dictionary containing pagination details such as page size, current page number, data, and information about the next and previous pages.

## Task 3: Deletion-Resilient Hypermedia Pagination

### `Server` class with `get_hyper_index` method
- **Objective**: To ensure that if rows are deleted between queries, users do not miss items when navigating through the pages.
- **Method**: `get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict`
  - This method returns a dictionary with:
    - `index`: Start index of the current page.
    - `next_index`: Index for the next page.
    - `page_size`: The current page size.
    - `data`: The actual page of the dataset.
  - The method adjusts the `index` if rows are deleted between queries, ensuring continuity in pagination.

### Example Usage
```python
server = Server()
server.indexed_dataset()

# Retrieve the first page of data with a page size of 2
res = server.get_hyper_index(3, 2)
print(res)

# Retrieve the next page using the `next_index`
res_next = server.get_hyper_index(res.get('next_index'), 2)
print(res_next)

# Delete a row and retrieve the initial index again
del server._Server__indexed_dataset[res.get('index')]
res_deleted = server.get_hyper_index(3, 2)
print(res_deleted)

