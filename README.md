# Sculpture-GAN
3D DCGAN inspired GAN trained on 32x32x32 voxelizations of [Thingi10k](https://ten-thousand-models.appspot.com/) - a corpus of 10,000 3D printable objects and sculptures - as a result, the generated sculptures are almost always 3D-printable, but usually do not have any real 'meaning', and are just abstract sorts of shapes.

# Example abstract shape generations

## 3D-printed generation

![1](images/3dprinted.jpg?raw=true)

## Computer visualized generations

![1](images/snapshot10.png?raw=true)
![2](images/snapshot6.png?raw=true)
![3](images/snapshot13.png?raw=true)



# Usage
There are 3 files you need to use to generate your own 3D shapes.
You need to download [Thingi10k](https://ten-thousand-models.appspot.com/), see [data](data) path. 

## generate_dataset.py
* Open `generate_dataset.py` and in line 8, set the variable `path_to_dataset` to be the path to your `raw_meshes` folder from your thingi10k download.
```
cd $HOME/repositories/sculpture-DCGAN-pytorch
conda activate sculpture-DCGAN-pytorchVE
python generate_dataset.py
```
* Run the file with `python generate_dataset.py`, and it will start generating numpy arrays that contain all of the now-voxelized models in thingi10k and save them to your `data/` folder.

## train.py

On line 23 of `train.py`, point it to the desired (usually the largest) .npy file in your `data/` folder by setting `numpy_array_saved` equal to its path.

Then, you can just run `python train.py` and trained network checkpoints will start to populate your `network_checkpoints/` folder.

## visualize.py

Point `visualize.py` to an array of generations in your `generations` folder (an array is created every 50 epochs) by setting `array_to_visualize` equal to its path. 

This script will allow you to see the models that network has generated in 3D, with the option to save as PNG, obj, etc.

# Issues / Future efforts

Right now, the main issue is the fact that it's very hard to get data for this sort of project; the only two datasets I have encountered are shapnet and thingi10k; currently; i am trying to train a conditional version of the 3d GAN with shapenet so that you can select that you want to generate a table, chair, etc, and the network will move past just generating "shapes"...

## SETUP

### HARDWARE:
* Current: 
```
$ nvidia-smi -q

==============NVSMI LOG==============

Timestamp                                 : Thu Jul 21 21:52:47 2022
Driver Version                            : 470.129.06
CUDA Version                              : 11.4

Attached GPUs                             : 1
GPU 00000000:01:00.0
    Product Name                          : NVIDIA GeForce RTX 3080 Laptop GPU
    Product Brand                         : GeForce
    Display Mode                          : Enabled
    Display Active                        : Enabled
    Persistence Mode                      : Disabled

FB Memory
        Total                             : 16116 MiB
``` 

### SOFTWARE

* Current machine OS:
```
$ hostnamectl
 Operating System: Ubuntu 20.04.3 LTS
            Kernel: Linux 5.15.0-41-generic
      Architecture: x86-64
```

[packages versions](dependencies/)
```
$ python testing_versions.py
python: 3.7.13 (default, Mar 29 2022, 02:18:16) 
[GCC 7.5.0]
torch: 1.12.0
mayavi: 4.7.1
cuda_is_available: True
cuda version: 11.3
cuda.device_count  1
```

## MX Log 
* Installed dependencies, download datasets and update README (23-July-2022)
* Errors: No such file or directory: '$HOME/datasets/Thingi10K/05_raw_meshes/233195.binvox' which might be related to python version https://petermortimer.de/binvox-rw-py3.html#Troubleswithwriting.binvoxfilesinPython3 (23-July-2022)