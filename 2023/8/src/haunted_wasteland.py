from pathlib import Path


class Node:
    def __init__(self, name, left_value, right_value) -> None:
        self.name = name
        self.left_value = left_value
        self.right_value = right_value


if __name__ == "__main__":
    source = Path(__file__).resolve().parent
    input_file_path = source / "resources/input.txt"
    with input_file_path.open() as file:
        lines: list[str] = file.read().splitlines()
        lines.pop(1)
        directions: list[str] = [*lines.pop(0)]
        nodes: list[Node] = []
        for line in lines:
            name = line[:3]
            left_value = line[7:10]
            right_value = line[12:15]
            nodes.append(
                Node(name=name, left_value=left_value, right_value=right_value)
            )
        nodes.sort(key=lambda x: x.name)
        first_direction = directions.pop(0)
        if first_direction == "L":
            next_node_to_look_for = nodes[0].left_value
        else:
            next_node_to_look_for = nodes[0].right_value
        for direction in directions:
            next_node_to_look_for = next(
                (node for node in nodes if node.name == next_node_to_look_for), None
            )
