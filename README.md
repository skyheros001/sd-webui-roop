# 分支 windows10本地安装因为一直提示安装不上，所以手动修改了一下，
install.py
+ sys.stdout.reconfigure(encoding='utf-8')

requirements.txt
+ 清空内容，仅加上
+ insightface==0.7.3

然后手动进入虚拟环境
venv\Scripts\activate.bat
并手动安装依赖
+ insightface==0.7.3
+ onnx==1.14.0
+ 去掉 onnxruntime==1.15.0
+ 增加 onnxruntime==1.13.1
+ opencv-python==4.7.0.72
+ ifnude
+ cython

说明：把onnxruntime从1.15换到1.13.1的原因是rembg 2.0.30 requires onnxruntime~=1.13.1,
如果还有其它插件的依赖冲突具体看说明来进行更新和安装。

备注建议其它依赖版本号
protobuf==3.20.2
open-clip-torch==2.5.0

# roop for StableDiffusion

This is an extension for StableDiffusion's [AUTOMATIC1111 web-ui](https://github.com/AUTOMATIC1111/stable-diffusion-webui/) that allows face-replacement in images. It is based on [roop](https://github.com/s0md3v/roop) but will be developed seperately.

![example](example/example.png)

### Disclaimer

This software is meant to be a productive contribution to the rapidly growing AI-generated media industry. It will help artists with tasks such as animating a custom character or using the character as a model for clothing etc.

The developers of this software are aware of its possible unethical applicaitons and are committed to take preventative measures against them. It has a built-in check which prevents the program from working on inappropriate media including but not limited to nudity, graphic content, sensitive material such as war footage etc. We will continue to develop this project in the positive direction while adhering to law and ethics. This project may be shut down or include watermarks on the output if requested by law.

Users of this software are expected to use this software responsibly while abiding the local law. If face of a real person is being used, users are suggested to get consent from the concerned person and clearly mention that it is a deepfake when posting content online. Developers of this software will not be responsible for actions of end-users.

## Installation

To install the extension, follow these steps:

+ In web-ui, go to the "Extensions" tab and use this URL `https://github.com/s0md3v/sd-webui-roop` in the "install from URL" tab.
+ Restart the UI

On Windows, Microsoft Visual C++ 14.0 or greater must be installed before installing the extension. [During the install, make sure to include the Python and C++ packages.](https://github.com/s0md3v/roop/issues/153)

## Usage

1. Under "roop" drop-down menu, import an image containing a face.
2. Turn on the "Enable" checkbox
3. That's it, now the generated result will have the face you selected

### The result face is blurry
Use the "Restore Face" option. You can also try the "Upscaler" option or for more finer control, use an upscaler from the "Extras" tab.

### There are multiple faces in result
Select the face numbers you wish to swap using the "Comma separated face number(s)" option.

### The face didn't get swapped
Did you click "Enable"?

If you did and your console doesn't show any errors, it means roop detected that your image is either NSFW or wasn't able to detect a face at all.

### Img2Img

You can choose to activate the swap on the source image or on the generated image, or on both using the checkboxes. Activating on source image allows you to start from a given base and apply the diffusion process to it.

Inpainting should work but only the masked part will be swapped.
