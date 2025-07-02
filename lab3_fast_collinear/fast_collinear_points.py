from line_segment import LineSegment
from point import Point


class FastCollinearPoints:
    def __init__(self, points: list[Point]):
       if points is None:
            raise ValueError("Input is None")
       if any(p is None for p in points):
            raise ValueError("Input contains None")
       if len(points) != len({(p.x, p.y) for p in points}):
            raise ValueError("Input contains repeated points")
        
       self.segments_list = []
       sorted_points = sorted(points.copy())  

       # Analyze the slopes between points. 
       for i in range(len(sorted_points)):
            slopes = {}
            # Calculate the slope to every other point.  
            for j in range(len(sorted_points)):
                if i != j:
                    slope = sorted_points[i].slope_to(sorted_points[j])
                    if slope not in slopes:
                        slopes[slope] = []
                    slopes[slope].append(sorted_points[j])
            
            # Identify any patterns in the slopes. 
            for slope in slopes:
                if len(slopes[slope]) >= 3:
                    collinear = sorted([sorted_points[i]] + slopes[slope])
                    segment = LineSegment(collinear[0], collinear[-1])
                    if not any(seg.p == segment.p and seg.q == segment.q for seg in self.segments_list):
                        self.segments_list.append(segment)

    def number_of_segments(self) -> int:
        return len(self.segments_list)

    def segments(self) -> list[LineSegment]:
        return self.segments_list.copy()
