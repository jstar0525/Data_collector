# nvpmodel

https://jstar0525.tistory.com/86

```bash
$ sudo nvpmodel -m 3
$ sudo nvpmodel -d cool
$ sudo nvpmodel -q
```

# jtop

https://jstar0525.tistory.com/107

```bash
$ sudo apt-get install python-pip
$ sudo -H pip install -U jetson-stats
$ sudo reboot
$ sudo jtop
** jtop의 5CTRL에서 jetson_clocks를 Running으로 상태 변경
```

# intel realsense sdk

https://jstar0525.tistory.com/97

```bash
$ sudo apt-get update && sudo apt-get upgrade​
```
```bash
$ sudo apt-get install python python-dev
$ sudo apt-get install python3 python3-dev
```
```bash
$ git clone https://github.com/IntelRealSense/librealsense.git
$ cd ./librealsense
$ mkdir build
$ cd build
$ cmake ../ -DBUILD_PYTHON_BINDINGS:bool=true
```
```bash
Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the
  system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY
  OPENSSL_INCLUDE_DIR)

$ sudo apt-get install libssl-dev​
```
```bash
The Xinerama headers were not found

$ sudo apt-get install xorg-dev libglu1-mesa-dev​
```
```bash
$ make -j4
$ sudo make install
```
```bash
$ export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.6/pyrealsense2
$ source ~/.bashrc
```

# respeaker

https://jstar0525.tistory.com/103

```bash
$ sudo apt-get update
$ sudo apt-get install python-usb
$ sudo pip install pyusb click
$ https://github.com/jstar0525/usb_4_mic_array.git
$ cd usb_4_mic_array
$ sudo python dfu.py --download 6_channels_firmware.bin  # The 6 channels version
$ python tuning.py -p # after connect to respeaker
```
```bash
$ sudo apt-get install portaudio19-dev python-pyaudio
$ sudo pip install pyaudio
$ cd usb_4_mic_array
$ python get_indx.py

Input Device id  24  -  ReSpeaker 4 Mic Array (UAC1.0): USB Audio (hw:2,0)
```