class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1, v2, dist=1):
        self._v1 = v1
        self._v2 = v2
        self._dist = dist
        v1.links.append(self)
        v2.links.append(self)

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        if not any(
            (l.v1 == link.v1 and l.v2 == link.v2)
            or (l.v1 == link.v2 and l.v2 == link.v1)
            for l in self._links
        ):
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)

    def find_path(self, start_v, stop_v):
        def dfs(v, visited, path, path_links, dist):
            if v == stop_v:
                return path[:], path_links[:], dist
            visited.add(v)
            shortest = None
            for link in v.links:
                next_v = link.v2 if link.v1 == v else link.v1
                if next_v not in visited:
                    path.append(next_v)
                    path_links.append(link)
                    res = dfs(next_v, visited, path, path_links, dist + link.dist)
                    if res and (shortest is None or res[2] < shortest[2]):
                        shortest = res
                    path.pop()
                    path_links.pop()
            visited.remove(v)
            return shortest

        return dfs(start_v, set(), [start_v], [], 0)


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist=1):
        super().__init__(v1, v2, dist)
