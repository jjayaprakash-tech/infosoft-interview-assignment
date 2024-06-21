
### Problem #1 - Data Stream Ingestion

### DataStream Class Documentation

#### Overview

The `DataStream` class is designed to handle a stream of strings arriving with associated timestamps. It ensures that each unique string is printed at most once within any 5-second window from its last print time.

#### Class Structure

```python
class DataStream:
    def __init__(self):
        # Dictionary to store the last printed timestamp for each string
        self.last_printed_time = {}
```

- **`__init__` method**: Initializes an instance of `DataStream` with an empty dictionary `self.last_printed_time`. This dictionary will store the timestamp of the last printed occurrence of each unique string.

#### Methods

##### `should_output_data_str` Method

```python
    def should_output_data_str(self, timestamp: int, data_str: str) -> bool:
        # Check if the data string has been seen before and when it was last printed
        if data_str not in self.last_printed_time:
            # If it hasn't been seen, we print it and record the timestamp
            self.last_printed_time[data_str] = timestamp
            return True
        else:
            # Check if 5 seconds have passed since the last print
            if timestamp - self.last_printed_time[data_str] >= 5:
                # Update the last printed time and allow printing
                self.last_printed_time[data_str] = timestamp
                return True
            else:
                # Otherwise, don't allow printing
                return False
```

- **`should_output_data_str` method**: Determines if the given `data_str` should be printed based on the provided `timestamp`.

  - **Parameters**:
    - `timestamp` (int): The timestamp associated with the current data string.
    - `data_str` (str): The string to be evaluated for printing.

  - **Logic**:
    - If `data_str` is not found in `self.last_printed_time`, it means this is the first time encountering this string, so it should be printed immediately. The method records this occurrence in `self.last_printed_time` with the current `timestamp` and returns `True`.
    
    - If `data_str` is already in `self.last_printed_time`, it checks if at least 5 seconds (`timestamp - self.last_printed_time[data_str] >= 5`) have passed since its last print. If yes, it updates the last printed time to the current `timestamp` and returns `True`, indicating the string should be printed again. If not, it returns `False`, indicating the string should not be printed.

#### Example Usage

```python
# Example usage:
data_stream = DataStream()
print(data_stream.should_output_data_str(0, "hello"))  # True
print(data_stream.should_output_data_str(1, "world"))  # True
print(data_stream.should_output_data_str(6, "hello"))  # True
print(data_stream.should_output_data_str(7, "hello"))  # False
print(data_stream.should_output_data_str(3, "world"))  # True
```

- **Output**:
  ```
  True
  True
  True
  False
  True
  ```

#### Explanation

1. `should_output_data_str(0, "hello")`: Prints `True` because "hello" is encountered for the first time.
2. `should_output_data_str(1, "world")`: Prints `True` because "world" is encountered for the first time.
3. `should_output_data_str(6, "hello")`: Prints `True` because more than 5 seconds have passed since "hello" was last printed.
4. `should_output_data_str(7, "hello")`: Prints `False` because less than 5 seconds have passed since "hello" was last printed.
5. `should_output_data_str(3, "world")`: Prints `True` because "world" hasn't been printed since the last 5 seconds.

#### Summary

The `DataStream` class efficiently manages the printing of unique strings based on their arrival times, ensuring that each string is printed at most once within any 5-second period. It uses a dictionary to track the timestamps of the last printed occurrences for each string.



##### Source Code

The source code for the `DataStream` classes can be found in [data_stream.py](https://github.com/jjayaprakash-tech/infosoft-interview-assignment/blob/main/source-code/data_stream.py).

#### Assignment Document

For the assignment details and requirements, refer to the [Assignment Document](https://github.com/jjayaprakash-tech/infosoft-interview-assignment/blob/main/assignment-documents).
