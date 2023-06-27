import os
import shutil
import pandas as pd

SRC = '/segment/anything/output/dir'
DST = '/object/mask/output/dir'

# Traverse all subdirectories inside the output directory
for root, dirs, files in os.walk(SRC):
    # Check if metadata.csv file exists in the current directory
    if 'metadata.csv' in files:
        metadata_path = os.path.join(root, 'metadata.csv')
        # Read metadata.csv as a dataframe
        metadata_df = pd.read_csv(metadata_path)

        # Get the id of the row with the largest bbox area
        largest_area = 0
        largest_id = None
        for index, row in metadata_df.iterrows():
            bbox_w = row['bbox_w']
            bbox_h = row['bbox_h']
            area = bbox_w * bbox_h
            if area > largest_area:
                largest_area = area
                largest_id = int(row['id'])

        if largest_id is not None:
            # Find the path of the target png file
            png_path = os.path.join(root, f"{largest_id}.png")
            if os.path.exists(png_path):
                # Create the corresponding directory in the mask directory
                mask_subdir = os.path.relpath(root, SRC)
                mask_subdir, fname = mask_subdir.split("/")
                mask_dir_path = os.path.join(DST, mask_subdir)

                os.makedirs(mask_dir_path, exist_ok=True)

                # Copy the png file to the mask directory
                mask_path = os.path.join(mask_dir_path, f"{fname}.png")
                shutil.copyfile(png_path, mask_path)
