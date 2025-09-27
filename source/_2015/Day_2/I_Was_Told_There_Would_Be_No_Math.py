def calculate_area_of_wrapping_paper(length: int, width: int, height: int) -> int:
    length_x_width = length * width
    width_x_height = width * height
    height_x_length = height * length

    return 2 * (length_x_width + width_x_height + height_x_length) + min(length_x_width, width_x_height, height_x_length)

def calculate_ribbon_length(length: int, width: int, height: int) -> int:
    return (length + width + height - max(length, width, height)) * 2 + length * width * height