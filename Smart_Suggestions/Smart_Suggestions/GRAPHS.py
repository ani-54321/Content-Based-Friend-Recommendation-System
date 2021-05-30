class Graph:
    stack = []
    queue = []
    visited = []
    next = []

    def __init__(self, data):
        self.data = data[0].strip()
        self.extra_info = data[1:]
        self.next = []

    def graph_insert(self, node):
        node.next.append(self)

    def graph_traversal_dfs(user, storage):
        # print(user.data)
        for conn in user.next:
            if conn not in user.stack and conn not in user.visited:
                # print(conn.data, "--->", end="")
                user.stack.append(conn)
                storage.append([user.extra_info[1], conn.extra_info[1]])
                conn.graph_traversal_dfs(storage)

        if len(user.stack) != 0:
            cur = user.stack.pop(-1)
            # print(cur.data)
            user.visited.append(cur)
            cur.graph_traversal_dfs(storage)

    def conn_suggestions_bfs(user, graph_suggestions):
        # print(user.data)
        for conn in user.next:
            if conn not in user.queue and conn not in user.visited:
                graph_suggestions.append(conn)
                user.queue.append(conn)
        
        if len(user.queue) != 0:
            cur = user.queue.pop(0)
            print(cur.data)
            user.visited.append(cur)
            cur.conn_suggestions_bfs(graph_suggestions)
        
        else:
            return graph_suggestions


# parrent = Graph("The Database")
# node1 = Graph("ABC")
# node1.graph_insert(parrent)


# node2 = Graph("XYZ")
# node2.graph_insert(parrent)
# node2.graph_insert(node1)

# node3 = Graph("LMN")
# node3.graph_insert(parrent)

# node4 = Graph("OPQ")
# node4.graph_insert(parrent)
# node4.graph_insert(node2)
# node1.graph_insert(node4)

# # memo = []

# # parrent.graph_traversal_dfs()
# # node1.conn_suggestions_bfs(memo)
# # print(memo)

# Graph.visited.clear
# Graph.stack.clear

# node1.conn_suggestions()