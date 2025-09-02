# This duplicates the Image Service 3 /full/w,h/ static thumbs as /full/w,/ because Theseus asks for those when the orientation is portrait

import os
import shutil

if __name__ == "__main__":

    img_paths = [ f.path for f in os.scandir("C:\\git\\tomcrane\\yesterdays-lambeth-today-iiif-img") if f.is_dir() ]
    for img_path in img_paths:
        full_dir = img_path + "\\" + "full"
        if os.path.exists(full_dir):
            print(full_dir) 
            sizes = [ s for s in os.scandir(full_dir) if s.is_dir() ]
            for size_dir in sizes:
                print(size_dir.name)
                parts = size_dir.name.split(',')
                if len(parts) == 2:
                    w_dir = f"{full_dir}\\{parts[0]},"
                    print("making " + w_dir)
                    shutil.copytree(size_dir, w_dir)
