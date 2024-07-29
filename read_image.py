from PIL import Image
import folder_paths
import os

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

class LoadImagePIL:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        return {"required":
                    {"image": (sorted(files), {"image_upload": True})},
                }

    CATEGORY = "image"

    RETURN_TYPES = ("PIL",)
    RETURN_NAMES = ("image",)

    FUNCTION = "read_image"

    # OUTPUT_NODE = False

    def read_image(self, image):
        image_path = folder_paths.get_annotated_filepath(image)
        image = Image.open(image_path)
        return (image,)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "ReadImage": ReadImage,
    "LoadImagePIL": LoadImagePIL
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ReadImage": "Read image to pil",
    "LoadImagePIL": "Read image to pil"
}