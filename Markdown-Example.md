# Example Markdown: Heading 1
## Heading 2
### Heading 3

## Basic formatting
___



## Code formatting
- This is an exmple of `inline code`. Where it's in the middle of another string.
- This is an example of basic code block:

    ```
    Code goes here
    ```
    
- This is an example of syntax highlighting

    ```python
    #python
    import random
    print(random.randint(10))
    ex_dict = {"test": "value", "test2": "value2"}
    ex_set = {1, 2, 3}
    ex_tuple_list = [(1, 2, 3), (9, 5, 3)]
    ```
    
    ```powershell
    #powershell
    $results = get-content -path C:\temp\log.txt | Select-String -Pattern "lame"
    ```
    
    ```json
    {
    "example_json": [
            {
            "priority": "high",
            "category": "general",
            "CPU Usage": "86%"
            },
            {
            "priority": "high",
            "category": "general",
            "Mem Usage": "86%"
            }
        ]
    }
    ```
    
    ```yaml
    #yaml
    - priority: high
      category: general
      CPU Usage: 86%
    - priority: high
      category: general
      Mem Usage: 86%
    ```
