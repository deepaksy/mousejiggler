# mousejiggler
A mouse jiggler program implemented  in python.

### **Pre-requisite**:
- Python 3.x installation.
- An IDE prefered.
- A virtual environment - optional.
- *python packages(pip package)*:
   - pyautogui
   - random
   - time
   - threading
   - keyboard


*Here, pyautogui, keyboard package you need to get from pip install <package-name>, other packages are readily available with python installation.*

### Usage:
1. Install python 3.x or more.
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
- *Currently, the program terminates when you press **esc** on you keyboard. You can further customize and enhance the program termination logic*.
- *The program is using python in-build threading library to run the module in a multi-threading enviornment. If anyone have experience and have worked with multi-threading in python. they are invited to enhance the threading behaviour of the program.*
