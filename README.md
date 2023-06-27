# Diffusion-based Synthetic Anomalies for Industrial Inspection (DSAII)
```clike=
  synthetic_tidy_v2
  ├─ audio cable
  │  ├─ img_url.json
  │  │
  │  ├─ normal
  │  │  ├─ 000.png
  │  │  ├─ 001.png
  │  │    ...
  │  │  └─ 019.png
  │  │
  │  ├─ anomaly
  │  │  ├─ 000.png
  │  │  ├─ 001.png
  │  │    ...
  │  │  └─ 017.png
  │  │
  │  └─ mask
  │     ├─ 000.png
  │     ├─ 001.png
  │       ...
  │     └─ 017.png
  ├─ audiopipe
  ...
```

## Why use DSAII?
DSAII dataset contains normal images with **large intra-class variation**, while defective images are generated by diffusion model. This setting aims to evaluate the model’s **generalizability** and **few-shot capabilities**. The model needs to learn the abstract pattern of the object/texture and the its normal appearance to achieve better performance.

## Dataset Structure
DSAII dataset are obtained by crawling and arranging similar images from the web. Each class (0\~77) contains 10\~20 images without defect, which is saved under path `synthetic_tidy_v2/{CLASS}/normal`. The image reference link is listed in `img_url.json`. The whole dataset contains 2906 images (including normal and defect images).

For each normal images, we apply Stable Diffusion for defect inpainting respectively. The inpainting mask is acquired by random sampling ground_truth mask from [MVTec AD](https://www.mvtec.com/company/research/datasets/mvtec-ad) dataset, then applying augmentations as our input inpainting masks. The inpainting masks are saved under path `synthetic_tidy_v2/{CLASS}/mask`. The output defect images are saved under path `synthetic_tidy_v2/{CLASS}/defect`. The failure cases are eliminated.

<!--- ## Dataset Download
For downloading our synthetic dataset, please visit <a href="https://drive.google.com/file/d/148yCBS_6I7WqSMbgY4LTKq97Nb5NTS2L/view?usp=sharing" target="_blank">synthetic_tidy_v2</a>. For the convenience, <a href="https://drive.google.com/file/d/1j4iDajm9rt1Pj0Numpn0-4tT6rnyM7EL/view?usp=sharing" target="_blank">synthetic_mvtec_like</a> is also provided with same structure as MVTecAD dataset. -->

## Instructions
* Step 1: Prepare representative images for each class you want to create.    
For crawling bunches of similar images, first prepare one image for each class, for example:
```clike=
  /path/to/dir
  ├─ audiopipe
  │  └─ 000.png
  ├─ bucket
  │  └─ 000.png
  ...
```
* Step 2: Prepare a Google Chrome browser.    
* Step 3: Download `chromedriver.exe` from <a href="https://chromedriver.chromium.org/downloads" target="_blank">official website</a>.
* Step 4: Edit `SRC`, `DST` path to directory in `crawler_picture.py` then execute `python crawler_picture.py`.
After executing `crawler_picture.py`, you will get output directory, for example:
```clike=
  /path/to/dir
  ├─ audiopipe
  │  ├─ 000.png
  │  ├─ 001.png
  │  │    ...
  │  └─ 019.png
  ├─ bucket
  │  ├─ 000.png
  ...
```
* 


## Experiment
We test synthetic dataset on [Patchcore](https://github.com/amazon-science/patchcore-inspection) (CVPR, 2022), [SimpleNet](https://github.com/DonaldRR/SimpleNet) (CVPR, 2023). The performance is record as follow.

| Method | Mean Image AUC (%) | Mean Pixel AUC (%)|
|-----|-----|--------|
|Patchcore | 57.2 |   87.5    |
|SimpleNet  |69.1    |   65.3  |

## NTHU CVLAB
For more details, please visit [CVLAB](https://cv.cs.nthu.edu.tw/).
<br><br>
CHENG-YU HO: `lesthan41@gapp.nthu.edu.tw` <br>
YU-HSUAN HSIEH: `ss111062646@gapp.nthu.edu.tw`

## License
MIT Licence
