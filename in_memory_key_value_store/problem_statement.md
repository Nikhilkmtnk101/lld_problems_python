# In-Memory Key-Value Store Design

## Problem Statement
Design an in-memory key-value store similar to Redis with the following requirements:

- The key-value store should be in-memory and does not require access to the file system.
- The key will always be a string.
- The value would be an object/map with attributes and corresponding values.
- Each attribute key would be a string, and the attribute values could be string, integer, double, or boolean.
- The key-value store should be thread-safe.
- Expose the following functions:
  - `get(String key)`: Should return the value (object with attributes and their values). Return null if key not present.
  - `search(String attributeKey, String attributeValue)`: Returns a list of keys that have the given attribute key, value pair.
  - `put(String key, List<Pair<String, String>> listOfAttributePairs)`: Adds the key and the attributes to the key-value store. If the key already exists, then the value is replaced.
  - `delete(String key)`: Deletes the key, value pair from the store.
  - `keys()`: Return a list of all the keys.
- The value object should override the `toString` method to print the object as a comma-separated list of key-value pairs for the attributes. Example: `attribute1: attribute_value_1, attribute2: attribute_value_2, attribute3: attribute_value_3`.
- The data type of an attribute should get fixed after its first occurrence. Example: Once we encounter an attribute age with an integer value, then any entry with an age attribute having a non-integer value should result in an exception.
- Nothing should be printed inside any of these methods. All scanning and printing should happen in the Driver/Main class only. Exception Handling should also happen in the Driver/Main class.

## Input/Output Format
- **Input Format**: Multiple lines with each line containing a command.
  - Possible commands: `get <key>`, `put <key> <attributeKey1> <attributeValue1> <attributeKey2> <attributeValue2>....`, `delete <key>`, `search <attributeKey> <attributeValue>`, `keys`, `exit`.
  - Stop taking the input when you encounter the word `exit`.
  - Assume that attribute keys and values would not have space in between.
- **Output Format**: Print output based on the specific commands as mentioned below.
  - `get`: Comma and space-separated attributes. Example: `attribute1: attribute_value_1, attribute2: attribute_value_2, attribute3: attribute_value_3`. Print "No entry found for <key>" if `get` returns null.
  - `put`: Do not print anything. Print "Data Type Error" if attribute has data type other than previous set.
  - `delete`: Do not print anything.
  - `search`: Comma-separated keys. Example: `key1,key2,key3,key4`. Print in sorted order.
  - `keys`: Comma-separated keys. Example: `key1,key2,key3,key4`. Print in sorted order.

## Example
### Input

1. `put sde_bootcamp title SDE-Bootcamp price 30000.00 enrolled false estimated_time 30`
2. `get sde_bootcamp`
3. `keys`
4. `put sde_kickstart title SDE-Kickstart price 4000 enrolled true estimated_time 8`
5. `get sde_kickstart`
6. `keys`
7. `put sde_kickstart title SDE-Kickstart price 4000.00 enrolled true estimated_time 8`
8. `get sde_kickstart`
9. `keys`
10. `delete sde_bootcamp`
11. `get sde_bootcamp`
12. `keys`
13. `put sde_bootcamp title SDE-Bootcamp price 30000.00 enrolled true estimated_time 30`
14. `search price 30000.00`
15. `search enrolled true`
16. `exit`

### Output

1. `title: SDE-Bootcamp, price: 30000.00, enrolled: false, estimated_time: 30`
2. `sde_bootcamp`
3. `Data Type Error`
4. `No entry found for sde_kickstart`
5. `sde_bootcamp`
6. `title: SDE-Kickstart, price: 4000.00, enrolled: true, estimated_time: 8`
7. `sde_bootcamp,sde_kickstart`
8. `No entry found for sde_bootcamp`
9. `sde_kickstart`
10. `sde_bootcamp`
11. `sde_bootcamp,sde_kickstart`

## Expectations

- Make sure that you have a working and demonstrable code.
- Ensure that the code is functionally correct.
- Code should be modular and readable.
- Address separation of concerns.
- Avoid writing everything in a single file (if not coding in C/C++).
- Code should easily accommodate new requirements and minimal changes.
- Ensure there is a main method from where the code could be easily testable.
- [Optional] Write unit tests, if possible.
- No need to create a GUI.
