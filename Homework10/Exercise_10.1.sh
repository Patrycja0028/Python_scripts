# Create a virtual environment for this course using venv or virtualenv. Install numpy, matplotlib, pandas. Send me a list of commands used with outputs. 

python -m venv myenv
myenv\Scripts\activate # (myenv) (base) PS C:\Users\Admin>
pip install numpy matplotlib pandas

# Collecting numpy
#   Downloading https://files.pythonhosted.org/packages/ea/bc/da526221bc111857c7ef39c3af670bbcf5e69c247b0d22e51986f6d0c5c2/numpy-1.19.5-cp36-cp36m-win_amd64.whl (13.2MB)
#     100% |████████████████████████████████| 13.2MB 3.7MB/s
# Collecting matplotlib
#   Downloading https://files.pythonhosted.org/packages/da/75/7bb16e22aa3f8d23a3afd065a7c933de71b67561c4561cf162fbc5d94221/matplotlib-3.3.4-cp36-cp36m-win_amd64.whl (8.5MB)
#     100% |████████████████████████████████| 8.5MB 4.9MB/s
# Collecting pandas
#   Downloading https://files.pythonhosted.org/packages/79/87/8bb36bd4ebae147612c73d1bdc1385db7beebb9eb141c4bfefb33f52c87c/pandas-1.1.5-cp36-cp36m-win_amd64.whl (8.7MB)
#     100% |████████████████████████████████| 8.7MB 3.7MB/s
# Collecting cycler>=0.10 (from matplotlib)
#   Using cached https://files.pythonhosted.org/packages/5c/f9/695d6bedebd747e5eb0fe8fad57b72fdf25411273a39791cde838d5a8f51/cycler-0.11.0-py3-none-any.whl
# Collecting python-dateutil>=2.1 (from matplotlib)
#   Downloading https://files.pythonhosted.org/packages/ec/57/56b9bcc3c9c6a792fcbaf139543cee77261f3651ca9da0c93f5c1221264b/python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229kB)
#     100% |████████████████████████████████| 235kB 6.1MB/s
# Collecting kiwisolver>=1.0.1 (from matplotlib)
#   Downloading https://files.pythonhosted.org/packages/6e/df/1250c32ab3b532c32a7e47c1cd240faba98f75b1b5150939b10e9bffb758/kiwisolver-1.3.1-cp36-cp36m-win_amd64.whl (51kB)
#     100% |████████████████████████████████| 61kB 4.4MB/s
# Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3 (from matplotlib)
#   Downloading https://files.pythonhosted.org/packages/e5/0c/0e3c05b1c87bb6a1c76d281b0f35e78d2d80ac91b5f8f524cebf77f51049/pyparsing-3.1.4-py3-none-any.whl (104kB)
#     100% |████████████████████████████████| 112kB 7.3MB/s
# Collecting pillow>=6.2.0 (from matplotlib)
#   Downloading https://files.pythonhosted.org/packages/8f/10/c8dc9fff37b69b5962b7783ab4835611e83dada453cd9913d82ca2a1321b/Pillow-8.4.0-cp36-cp36m-win_amd64.whl (3.2MB)
#     100% |████████████████████████████████| 3.2MB 7.3MB/s
# Collecting pytz>=2017.2 (from pandas)
#   Downloading https://files.pythonhosted.org/packages/ec/dd/96da98f892250475bdf2328112d7468abdd4acc7b902b6af23f4ed958ea0/pytz-2026.2-py2.py3-none-any.whl (510kB)
#     100% |████████████████████████████████| 512kB 6.0MB/s
# Collecting six>=1.5 (from python-dateutil>=2.1->matplotlib)
#   Downloading https://files.pythonhosted.org/packages/b7/ce/149a00dd41f10bc29e5921b496af8b574d8413afcd5e30dfa0ed46c2cc5e/six-1.17.0-py2.py3-none-any.whl
# Installing collected packages: numpy, cycler, six, python-dateutil, kiwisolver, pyparsing, pillow, matplotlib, pytz, pandas
# Successfully installed cycler-0.11.0 kiwisolver-1.3.1 matplotlib-3.3.4 numpy-1.19.5 pandas-1.1.5 pillow-8.4.0 pyparsing-3.1.4 python-dateutil-2.9.0.post0 pytz-2026.2 six-1.17.0


pip list

# Package         Version
# --------------- -----------
# cycler          0.11.0
# kiwisolver      1.3.1
# matplotlib      3.3.4
# numpy           1.19.5
# pandas          1.1.5
# Pillow          8.4.0
# pip             18.1
# pyparsing       3.1.4
# python-dateutil 2.9.0.post0
# pytz            2026.2
# setuptools      40.6.2
# six             1.17.0
