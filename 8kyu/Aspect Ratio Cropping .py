import math
from typing import Tuple

def aspect_ratio(x: int, y: int) -> Tuple[int, int]:
    # Calculate the new width maintaining a 16:9 aspect ratio
    new_width = math.ceil((16 / 9) * y)
    return (new_width, y)