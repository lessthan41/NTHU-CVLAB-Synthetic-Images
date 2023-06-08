# Synthetic Image Dataset for Anomaly Detection and Segmentation
```clike=
  synthetic_tidy_v2
  ├─ 0
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
  ├─ 1
  ...
```

## Dataset Structure
This dataset are obtained by crawling and arranging similar images from the web. Each class (0\~77) contains 10\~20 images without defect, which is saved under path `synthetic_tidy_v2/{CLASS}/normal`. The image reference link is listed in `img_url.json`.

For each normal images, we apply Stable Diffusion for defect inpainting respectively. The inpainting mask is acquired by random sampling ground_truth mask from [MVTec AD](https://www.mvtec.com/company/research/datasets/mvtec-ad) dataset, then applying augmentations as our input inpainting masks. The inpainting masks are saved under path `synthetic_tidy_v2/{CLASS}/mask`. The output defect images are saved under path `synthetic_tidy_v2/{CLASS}/defect`. The failure cases are eliminated.

## Dataset Download
For downloading our synthetic dataset, please visit <a href="https://drive.google.com/file/d/1bcfn1jAIjkahJPWe2d_9upK0n5nBkO_q/view?usp=sharing" target="_blank">synthetic_tidy_v2</a>. For the convenience, <a href="https://drive.google.com/file/d/1t83KOk67e2Fz2HdtQgF7NtMQQTWBKRei/view?usp=sharing" target="_blank">synthetic_mvtec_like</a> is also provided with same structure as MVTecAD dataset.

## Experiment
We test synthetic dataset on [Patchcore](https://github.com/amazon-science/patchcore-inspection) (CVPR, 2022), [SimpleNet](https://github.com/DonaldRR/SimpleNet) (CVPR, 2023). The performance is record as follow. 

|  |Image AUC |Pixel AUC|
|-----|-----|--------|
|Patchcore | 57.2 |   87.5    |
|SimpleNet  |69.1    |   65.3  |

## NTHU CVLAB
For more details, please visit [CVLAB](https://cv.cs.nthu.edu.tw/).

