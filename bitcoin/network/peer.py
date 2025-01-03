# network/peer.py


class Peer:
    def __init__(self, node):
        self.node = node
        self.connection_status = False

    def connect(self, target_node):
        if not self.connection_status:
            self.node.connect_peer(target_node)
            target_node.connect_peer(self.node)
            self.connection_status = True
            print(
                f"Established connection with {target_node.address}:{target_node.port}"
            )

    def disconnect(self, target_node):
        if self.connection_status:
            self.node.disconnect_peer(target_node)
            target_node.disconnect_peer(self.node)
            self.connection_status = False
            print(f"Closed connection with {target_node.address}:{target_node.port}")
