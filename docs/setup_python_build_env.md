# Setup Python & Build Environment

## References

- [microbit-v2-samples](https://github.com/lancaster-university/microbit-v2-samples)

## Steps

- Python

```sh
$ pyenv versions
  system
* 3.10.16 (set by /home/abr/prjs/plant_watering/.python-version)
  3.13.3

pyenv local 3.13.3

$ pyenv versions
  system
  3.10.16
* 3.13.3 (set by /home/abr/prjs/plant_watering/.python-version)

$ python --version
Python 3.13.3

$ pip list
Package      Version
------------ -------
argcomplete  3.6.2
click        8.2.1
packaging    25.0
pip          25.3
pipx         1.8.0
platformdirs 4.4.0
pyserial     3.5
userpath     1.9.2

python -m venv .venv
source .venv/bin/activate
(.venv) $
...
```

## Build Env

```sh
    sudo apt install gcc
    sudo apt install git
    sudo apt install cmake
    sudo apt install gcc-arm-none-eabi binutils-arm-none-eabi
```

## Build

- Clone this repository:

```sh
git clone https://github.com/lancaster-university/microbit-v2-samples.git
cd microbit-v2-samples
```

- In the root of this repository type python build.py

```sh
python build.py
```

- The hex file will be built `MICROBIT.hex` and placed in the root folder.
