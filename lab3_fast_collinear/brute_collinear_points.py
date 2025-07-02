from line_segment import LineSegment
from point import Point

class BruteCollinearPoints:
    def __init__(self, points: list[Point]):
        if points is None:
            raise ValueError("Input is None")
        if any(p is None for p in points):
            raise ValueError("Input contains None")
        if len(points) != len({(p.x, p.y) for p in points}):
            raise ValueError("Input contains repeated points")
        
        self.segments_list = []
        sorted_points = sorted(points.copy()) # Sort for consistent ordering
        
        # combinations of 4 points
        for i in range(len(sorted_points)):
            for j in range(i+1, len(sorted_points)):
                for k in range(j+1, len(sorted_points)):
                    for l in range(k+1, len(sorted_points)):
                        p, q, r, s = sorted_points[i], sorted_points[j], sorted_points[k], sorted_points[l]
                        if p.slope_to(q) == p.slope_to(r) == p.slope_to(s):        # Check if all 4 points are collinear
                            segment = LineSegment(min(p, q, r, s), max(p, q, r, s))
                            if not any(seg.p == segment.p and seg.q == segment.q for seg in self.segments_list):    # to avoid repeated  segments
                                self.segments_list.append(segment)

    def number_of_segments(self) -> int:
        return len(self.segments_list)

    def segments(self) -> list[LineSegment]:
        return self.segments_list.copy()
