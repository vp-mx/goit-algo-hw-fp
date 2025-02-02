from collections import deque

from shared_funcs import draw_tree, list_to_heap_tree


# Функція для генерації кольору за кроком обходу
def rgb_color(step, max_steps):
    """Generate color based on current step and max steps."""
    intensity = int(255 * (step / max_steps))
    return f"#{intensity:02x}{intensity:02x}{255 - intensity:02x}"


# Ітеративний DFS обхід дерева з використанням стека
def dfs(tree_root):
    if tree_root is None:
        return
    stack = [tree_root]
    step = 0
    max_steps = count_nodes(tree_root)

    while stack:
        node = stack.pop()
        # Присвоюємо вузлу колір, що залежить від порядку обходу
        node.color = rgb_color(step, max_steps)
        print("Press Enter to continue..." if step > 0 else "Press Enter to start...")
        _ = input()
        draw_tree(tree_root)
        step += 1
        # Додаєм спочатку правий вузол, потім лівий (щоб лівий обходився першим)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# Ітеративний BFS обхід дерева з використанням черги
def bfs(tree_root):
    if tree_root is None:
        return
    queue = deque([tree_root])
    step = 0
    max_steps = count_nodes(tree_root)

    while queue:
        node = queue.popleft()
        node.color = rgb_color(step, max_steps)
        print("Press Enter to continue..." if step > 0 else "Press Enter to start...")
        input()
        draw_tree(tree_root)
        step += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def count_nodes(node):
    """Count nodes in the tree."""
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


if __name__ == "__main__":
    # Приклад: створення бінарного дерева з купи
    heap_list = [0, 1, 2, 3, 4, 5, 6]
    heap_tree_root = list_to_heap_tree(heap_list)

    print("DFS traversal visualization:")
    dfs(heap_tree_root)

    # Перебудовуємо дерево для BFS обходу
    heap_tree_root = list_to_heap_tree(heap_list)

    print("BFS traversal visualization:")
    bfs(heap_tree_root)
