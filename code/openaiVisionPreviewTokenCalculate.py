#
# https://openai.com/api/pricing/
# 多分あってるはず、間違ってたら誰かPRください
import math
def openaiVisionPreviewTokenCalculate(width, height, detail="high"):
    newWidth = 768
    newHeight = 768

    if detail == "low":
        return 85

    if width > 2048 or height > 2048:
        aspect_ratio = width / height

        if aspect_ratio > 1:
            newWidth = 2048
            newHeight = int(2048 / aspect_ratio)
        else:
            newHeight = 2048
            newWidth = int(2048 * aspect_ratio)
    if width >= height and height > 768:
        newWidth = int((768 / height) * width)
        newHeight = height
    elif height > width and width > 768:
        newHeight = int((768 / width) * height)
        newWidth = width
    else:
        newWidth = width
        newHeight = height

    tiles_width = math.ceil(newWidth / 512)
    tiles_height = math.ceil(newHeight / 512)
    total_tokens = 85 + 170 * (tiles_width * tiles_height)

    return total_tokens
