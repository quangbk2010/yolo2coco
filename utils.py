
from pathlib import Path
import globox

def convertyolo2coco(txt_path, json_path):
    annotations = globox.AnnotationSet.from_yolo(folder=txt_path, image_folder=txt_path)
    annotations.save_coco(path=Path(json_path), auto_ids=True) #, label_to_id={"CapTube_Glass": 0, "CapTUbe_Plastic": 1, "MicroTube_Plastic": 2, "PetriDish": 3, "USB": 4}

convertyolo2coco('path_to_txt_folder', 'path_to_json_result_file')
