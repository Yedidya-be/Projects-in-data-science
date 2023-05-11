import napari

class CellAnnotation:
    def __init__(self, image_path):
        self.image_path = image_path
        self.cells_in_division = []
        self.cells_not_in_division = []

    def upload_seg(self, segmentation_path):
        # Implement the logic to upload the segmentation data
        pass

    def annotate(self):
        # Implement the logic to open the image in Napari and perform cell annotation
        pass
