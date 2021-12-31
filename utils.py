from classes import Player, Point, Board


def find_mills(player: "Player"):
    """find all mills
    check
    if points in player points has 2 connections
    if connected points are in the same line
    """
    mills = []
    for point1 in player.occupied():
        connect_list = []
        for point2 in player.occupied():
            if point1.coord() in point2.posbl_mov():
                connect_list.append(point2)
        if len(connect_list) == 2:
            for i in range(2):
                for point in connect_list:
                    if not point.coord()[i] == point1.coord()[i]:
                        break
                connect_list.append(point1)
                mills.append(connect_list)
    return mills


"""lock mills"""
"""mill"""