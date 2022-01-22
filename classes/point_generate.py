import json
from classes.point import Point


def generate_points(mode: int) -> list:
    """Generate active points list on given board.

    Load coordinates from file and return list.

    Paramters
    ---------
    mode : int
        Game mode meaning board size.
    """
    with open("classes/mode_points.json", 'r') as file_handle:
        data = json.load(file_handle)
        points_list = []
        for point in data[str(mode)]:
            id = tuple(point["id"])
            posbl_mov = []
            for point in point["connected_p"]:
                posbl_mov.append(tuple(point))
            points_list.append(Point(id, posbl_mov))
        return points_list
