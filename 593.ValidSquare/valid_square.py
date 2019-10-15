class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        edges = set()
        edges.add(self.dist2(p1, p2))
        edges.add(self.dist2(p1, p3))
        edges.add(self.dist2(p1, p4))
        edges.add(self.dist2(p2, p3))
        edges.add(self.dist2(p2, p4))
        edges.add(self.dist2(p3, p4))
        edge1 = edges.pop()
        if len(edges) == 1 :
            if edge1 * 2 in edges or edge1 / 2 in edges :
                return True
        else :
            return False
        
    def dist2(self, p1: List[int], p2: List[int]) -> int:
        d2 = (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])
        return d2
