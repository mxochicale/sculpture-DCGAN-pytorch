# conda activate *VE
# python testing_versions.py
import torch 
import sys
import mayavi

print(f'python: {sys.version}')
print(f'torch: {torch.__version__}') 
print(f'mayavi: {mayavi.__version__}') 

print(f'cuda_is_available: {torch.cuda.is_available()}')
print(f'cuda version: {torch.version.cuda}')
print(f'cuda.device_count  {torch.cuda.device_count()}')

