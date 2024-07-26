from PIL import Image


class ReadImage:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"default": r"output/ComfyUI_00001_.png"}),
            },
        }

    RETURN_TYPES = ("PIL",)
    RETURN_NAMES = ("image",)

    FUNCTION = "read_image"

    # OUTPUT_NODE = False

    CATEGORY = "utils"

    def read_image(self, text):
        image = Image.open(text)
        return (image,)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "ReadImage": ReadImage
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ReadImage": "Read image to pil"
}