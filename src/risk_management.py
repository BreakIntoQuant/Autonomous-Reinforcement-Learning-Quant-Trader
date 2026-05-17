def position_limit_check(
    position,
    max_position=10
):

    if abs(position) > max_position:

        return False

    return True