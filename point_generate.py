import json
from point import Point

def generate_points(mode):
    with open("mode_points.json", 'r') as file_handle:
        data = json.load(file_handle)
        points_list = []
        for point in data[str(mode)]:
            id = tuple(point["id"])
            posbl_mov = []
            for point in point["connected_p"]:
                posbl_mov.append(tuple(point))
            points_list.append(Point(id, posbl_mov))
        return points_list


