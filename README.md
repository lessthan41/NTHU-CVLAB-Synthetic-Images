# NTHU CVLAB - Synthetic Images

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

This dataset are obtained by crawling and arranging similar images from the web. Each class (0\~77) contains 10\~20 images without defect, which is saved under path `synthetic_tidy_v2/{CLASS}/normal`. The image reference link is listed in `img_url.json`.

For each normal images, we apply Stable Diffusion for defect inpainting respectively. The inpainting mask is acquired by random sampling ground_truth mask from [MVTec AD](https://www.mvtec.com/company/research/datasets/mvtec-ad) dataset, then applying augmentations as our input inpainting masks. The inpainting masks are saved under path `synthetic_tidy_v2/{CLASS}/mask`. The output defect images are saved under path `synthetic_tidy_v2/{CLASS}/defect`. The failure cases are eliminated.

For downloading our synthetic dataset, please visit [synthetic_tidy_v2](). For the convenience, [synthetic_mvtec_like]() is also provided with same structure as MVTecAD datset.
