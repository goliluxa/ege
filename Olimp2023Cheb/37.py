import itertools

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2)

def is_convex(x1, y1, x2, y2, x3, y3):
    cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
    return cross_product >= 0

def is_inside_polygon(x, y, polygon_vertices):
    n = len(polygon_vertices)
    inside = False
    p1x,p1y = polygon_vertices[0]
    for i in range(1,n+1):
        p2x,p2y = polygon_vertices[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        x_intersect = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= x_intersect:
                        inside = not inside
        p1x,p1y = p2x,p2y
    return inside

def find_largest_convex_polygon(eagle_nests, woodpecker_nests):
    n = len(eagle_nests)
    largest_area = 0
    largest_polygon = []
    for vertices in itertools.combinations(eagle_nests, 3):
        if is_convex(*vertices):
            polygon_area = area(*vertices[0], *vertices[1], *vertices[2])
            if polygon_area > largest_area:
                largest_area = polygon_area
                largest_polygon = vertices
    if not largest_polygon:
        return []
    inside_nests = []
    for nest in woodpecker_nests:
        x, y = nest
        if is_inside_polygon(x, y, largest_polygon):
            inside_nests.append(nest)
    return largest_polygon, inside_nests

# Example usage:
eagle_nests = [(0,0), (0,5), (5,5), (5,0)]
woodpecker_nests = [(2,2), (2,3), (3,2), (3,3)]
largest_polygon, inside_nests = find_largest_convex_polygon(eagle_nests, woodpecker_nests)
print(largest_polygon)
print(inside_nests)
