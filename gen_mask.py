import cv2
import numpy as np
import glob
import torchvision.transforms as T
import torch
import os

SKIP = ["class", "to", "SKIP"]
SRC = "/extracted/mask/folder"
MASK = "./mvtec"
DST = "/path/to/ground/truth/mask"


def gen_mask(src_dir,mvtec_path):
    aug = T.Compose([T.ToTensor(),
                    T.RandomAffine(degrees=(0,360),translate=(0.5,0.5),scale=(0.1,2),shear=(10,10)),
                    T.RandomHorizontalFlip(),
                    T.RandomVerticalFlip()])
    obj_masks = glob.glob(src_dir+"/*/*.png")
    masks = glob.glob(mvtec_path+"/*/ground_truth/*/*.png")

    for i,obj_path in enumerate(obj_masks):
        obj_mask = cv2.imread(obj_path,cv2.IMREAD_GRAYSCALE)
        obj_mask = 1-T.ToTensor()(obj_mask)
        
        mask = cv2.imread(masks[np.random.randint(0,len(masks))],cv2.IMREAD_GRAYSCALE)
        mask = aug(mask)
        mask = T.Resize((obj_mask.size()[1],obj_mask.size()[2]))(mask)

        if int(os.path.basename(os.path.dirname(obj_path))) in SKIP:
            mask = T.ToPILImage()(mask)
            mask.save(obj_path.replace(SRC,DST))
            continue

        obj_mask[mask==0] = 0
        
        cnt = 0
        while cnt < 1000 and (torch.sum(obj_mask) < (obj_mask.size()[1]*obj_mask.size()[2])*0.01 or torch.sum(obj_mask) > (obj_mask.size()[1]*obj_mask.size()[2])*0.05):
            obj_mask = cv2.imread(obj_path,cv2.IMREAD_GRAYSCALE)
            obj_mask = 1-T.ToTensor()(obj_mask)
            
            mask = cv2.imread(masks[np.random.randint(0,len(masks))],cv2.IMREAD_GRAYSCALE)
            mask = aug(mask)
            mask = T.Resize((obj_mask.size()[1],obj_mask.size()[2]))(mask)

            obj_mask[mask==0] = 0
            cnt += 1

        obj_mask = T.ToPILImage()(obj_mask)
        obj_mask.save(obj_path.replace(SRC,DST))
        print(obj_path, "Done")

def mkdir():
    for i in range(78):
        os.makedirs(os.path.join(DST,str(i)),exist_ok=True)


def texture_gen_mask(src_dir,mvtec_path):
    aug = T.Compose([T.ToTensor(),
                    T.RandomAffine(degrees=(0,360),translate=(0.1,0.1),scale=(0.1,2),shear=(10,10)),
                    T.RandomHorizontalFlip(),
                    T.RandomVerticalFlip()])
    obj_masks = glob.glob(src_dir+"/*/*.png")
    masks = glob.glob(mvtec_path+"/*/ground_truth/*/*.png")

    for i,obj_path in enumerate(obj_masks):
        if int(os.path.basename(os.path.dirname(obj_path))) in SKIP:
            obj_mask = T.ToTensor()(cv2.imread(obj_path,cv2.IMREAD_GRAYSCALE))
            mask = cv2.imread(masks[np.random.randint(0,len(masks))],cv2.IMREAD_GRAYSCALE)
            mask = aug(mask)
            mask = T.Resize((obj_mask.size()[1],obj_mask.size()[2]))(mask)
        
            cnt = 0
            while cnt < 1000 and (torch.sum(mask) > (mask.size()[1]*mask.size()[2])*0.1 or torch.sum(mask) < (mask.size()[1]*mask.size()[2])*0.05):
                obj_mask = T.ToTensor()(cv2.imread(obj_path,cv2.IMREAD_GRAYSCALE))
                mask = cv2.imread(masks[np.random.randint(0,len(masks))],cv2.IMREAD_GRAYSCALE)
                mask = aug(mask)
                mask = T.Resize((obj_mask.size()[1],obj_mask.size()[2]))(mask)
        
                cnt += 1

            mask = T.ToPILImage()(mask)
            mask.save(obj_path.replace(SRC,DST))
            print(obj_path, "Done", "Count:", cnt)



if __name__ == "__main__":
    gen_mask(SRC,MASK)
    texture_gen_mask(SRC,MASK)
