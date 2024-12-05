import re


def read_print_puzzle(file_path: str):
    # Read the file content
    with open(file_path) as file:
        return file.read()


def process_print_puzzle(
    print_puzzle: str,
) -> tuple[dict[int, list[int]], list[list[int]]]:
    """
    Reads the puzzle with a specific structure and generates a reverse dictionary
    of ordering rules and a list of lists of page numbers.

    The file structure is as follows:
    - The first part contains lines of the form "a|b", where 'a' and 'b' are integers.
    - The second part contains lines of comma-separated integers.

    Args:
        print_puzzle (str): The content of the puzzle

    Returns:
        tuple: A tuple containing:
            - ordering_rules (Dict[int, List[int]]): A reverse dictionary where the key is 'b' and the value is a list of 'a' values.
            - pages_updates (List[List[int]]): A list of lists of page numbers from the second part of the file.
    """
    ordering_rules = {}
    pages_updates = []

    # Split the content into two parts: ordering rules and page numbers
    parts = print_puzzle.split("\n\n")

    # Process the first part: ordering rules
    ordering_rules_lines = parts[0].strip().split("\n")
    for line in ordering_rules_lines:
        match = re.match(r"(\d+)\|(\d+)", line.strip())
        if match:
            key = int(match.group(2))
            value = int(match.group(1))
            if key not in ordering_rules:
                ordering_rules[key] = []
            ordering_rules[key].append(value)

    # Process the second part: page numbers
    page_numbers_lines = parts[1].strip().split("\n")
    for line in page_numbers_lines:
        page_numbers = list(map(int, line.strip().split(",")))
        pages_updates.append(page_numbers)

    return ordering_rules, pages_updates
