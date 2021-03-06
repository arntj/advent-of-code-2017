def parse_node(input_values):
  children_count = input_values[0]
  metadata_count = input_values[1]
  remaining_values = input_values[2:]

  children = []

  while children_count > 0:
    (child, values) = parse_node(remaining_values)
    children.append(child)
    remaining_values = values
    children_count -= 1

  metadata = remaining_values[:metadata_count]

  node = (children, metadata)

  return (node, remaining_values[metadata_count:])

def sum_metadata(node):
  (children, metadata) = node
  return sum((sum_metadata(c) for c in children)) + sum(metadata)

def calculate_node_value(node):
  (children, metadata) = node

  if len(children) == 0:
    return sum(metadata)

  result = 0

  for m in metadata:
    i = m - 1
    if i < len(children):
      result += calculate_node_value(children[i])

  return result
