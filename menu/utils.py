def build_menu_tree(items, ancestors, parent=None):
    tree = []
    for item in items:
        if item.parent == parent and item in ancestors:
            children = build_menu_tree(items, ancestors, parent=item)
            tree.append((item, children))
        elif item.parent == parent:
            tree.append((item, []))
    return tree


def get_menu_item_ancestors(menu_item):
    ancestors = []
    current_item = menu_item
    while current_item is not None:
        ancestors.append(current_item)
        current_item = current_item.parent
    return ancestors
