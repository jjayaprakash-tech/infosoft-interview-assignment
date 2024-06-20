"""
Script: data_stream.py
Description: The DataStream class is designed to handle a stream of strings arriving with associated timestamps. 
             It ensures that each unique string is printed at most once within any 5-second window from its last print time.
Developer: Jayaprakash J
Date: June 21, 2024
"""

class DataStream:
    def __init__(self):
        # Dictionary to store the last printed timestamp for each string
        self.last_printed_time = {}
    
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

# Example usage:
data_stream = DataStream()
print(data_stream.should_output_data_str(0, "hello"))  # True
print(data_stream.should_output_data_str(1, "world"))  # True
print(data_stream.should_output_data_str(6, "hello"))  # True
print(data_stream.should_output_data_str(7, "hello"))  # False
print(data_stream.should_output_data_str(6, "world"))  # True
