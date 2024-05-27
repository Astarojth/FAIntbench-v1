# FAIntbench: A Fair AI Painting Benchmark for Bias Evaluation in Text-to-Image Models
This repository is supplement material for the paper: FAIntbench: A Holistic and Precise Benchmark for Bias Evaluation in Text-to-Image Models

🛰️: [![Toyset](https://img.shields.io/badge/Project-Toyset-87CEEB)](https://drive.google.com/file/d/1Tx000qwAcCsmOE9b5XUzyqlh8-1yBJMP/view?usp=sharing) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
📖: [![paper](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)]() &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

## 📚 Features

* Clear and robust definition. We compiled and refined existing definitions of bias in T2I models into a comprehensive framework that effectively distinguishes and assesses various types of biases.

* Large prompt dataset. Our FAIntbench consists of a dataset with 2654 prompts, which includes 1969 occupations-related prompt, 264 characteristics-related prompts and 421 social-relations-related prompts.
<p align="center">
  <img src="Figure/fig4.png" width="75%"/>
</p>

* Multi-dimensional evaluation metric. Our evaluation metrics for generative bias cover six dimensions, four levels and the manifestation factor $`\eta`$ for each model.
<p align="center">
  <img src="Figure/fig6.png" width="35%"/> <img src="Figure/fig3.png" width="75%"/>
</p>

## 📊 Test Models
* [Stable Cascade](https://huggingface.co/stabilityai/stable-cascade)
* [StableDifussion XL](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)
* [StableDifussion XL Turbo](https://huggingface.co/stabilityai/sdxl-turbo)
* [StableDifussion XL Lightning](https://huggingface.co/ByteDance/SDXL-Lightning)
* [PixArt Sigma](https://github.com/PixArt-alpha/PixArt-sigma)

## 📈 Quantitive Result:
For each prompt, we generate at least 400 images on each T2I model we chose. Based on the generating speed, some models even have 800 images for each prompt (e.g. sdxl Turbo).
<p align="center">
  <img src="Figure/fig1.png" width="90%"/>
</p>
We used our algorithm to evaluate each T2I model we chose and calculate the implicit bias, explicit bias and the manifestation factor. The result is shown in the following figure:
<p align="center">
  <img src="Figure/total.png" width="90%"/>
</p>

## 📌 Prerequesties
Prerequesties are the same as the prequesties of CLIP and models you use. The Following are some useful links and tips:
* [CLIP](https://github.com/openai/CLIP)
* [Cmofyui](https://github.com/comfyanonymous/ComfyUI)
* Pytorch >= 1.7.1
* Python >= 3.9
* OpenCV
* PIL

## 🌟 Usage!
* First, use the prompts provided by us in prompt folder to generate images. 200 images for each prompt will be sufficient to get enough accuracy. The folder structure to store the result is: model_name/prompt_name/image.png
* Second, use the image generanted in step 1 as input, run CLIP API "1_img2metajson.py" provided in preprocess folder "1_img2metajson.py". This script will output a json file containing the bias data of each model.
* Third, use the json file generated in step 2 as input, run "2_optimize.py" provided in preprocess folder, which will also generate json files that is optimized.
* Finally, set the json path to each of the three implicit, explicit and eta scripts under eval for the implicit, explicit and eta script to get the result
