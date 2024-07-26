from PIL import Image


class ReadPNGMetadata:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("PIL",),
                "key": ("STRING", {"default": "parameters"})
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("metadata", "parameters")

    FUNCTION = "read_metadata"

    # OUTPUT_NODE = False

    CATEGORY = "image"

    def read_metadata(self, image, key):
        info = image.info
        try:
            params = info[key]
        except:
            params = "error"
        return str(info), params


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "ReadPNGMetadata": ReadPNGMetadata
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ReadPNGMetadata": "Read PNG Metadata Node"
}