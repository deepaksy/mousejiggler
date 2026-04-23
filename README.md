# mousejiggler
A mouse jiggler program implemented  in python.

### **Pre-requisite**:
- Python 3.4x installation.
- An IDE prefered.
- A virtual environment - optional.
- *python packages(pip package)*:
   - pyautogui
   - random
   - time
   - keyboard
- asyncio (incase of using the older python version)


*Here, pyautogui, keyboard package you need to get from pip install <package-name>, other packages are readily available with python installation.*

### Usage:
1. Install python 3.4x or more.
2. clone the repository or copy the code.
3. create a virtual environment (optional)
   - command:
     ```python
     python -m venv <your-virtual-environment-name>
     ```
   - Activate your virtual environment:
     - command(macos/linux) :
       ```bash
       source <path-to-your-virtual-env>/bin
       ```
     - command(windows):
       ```batch
       <your-venv>/Scripts/activate.bat
       ```
4. Install the packages
   ```python
   pip install keyboard pyautogui
   ```
5. Execute the Script.
   - command:
     ```python
     python main.py
     ```
usecase: No usage definition needed. 😉



*Optional enhancement*: -
- *you can further optimise the code and create a os specific executable for the program.*
- *Currently, the program terminates when you press combination of keys **ctrl+shift+q** on you keyboard. You can further customize and enhance the program termination logic*.
- *The program is using python in-build asyncio to run optimized way with co-routines. If any experience programmer want to contribute to the project. they are pull requests are welcomed.*
