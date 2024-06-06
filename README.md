# Parser and Parse Tree Generator
This project is a graphical user interface (GUI) application built using Tkinter and CustomTkinter that 
reads, parses, and generates parse trees for simple programming language constructs. 
It also provides syntax error notifications for incorrect code.
### Features
- **Upload Code**: Load code from a `.txt` file
- **Check Syntax**: Parse the code and generate a parse tree.
- **Syntax Notifications**: Visual feedback for correct or incorrect syntax.

### Requirements
- Python 3.x
- `nltk`
- `customTkinter`
- `PIL`

### Installation
1. **Clone the repository**:
```sh
    git clone https://github.com/gamalahmedd/Parser.git
    cd parser-app
```
2. **Install the required package**:
```sh
    pip install nltk customtkinter pillow
```

### Usage
1. **Run the application**:
```python
    python app.py
```
2. **Upload Code**: Click the "Upload Code" button to load a `.txt` file containing your code.
3. **Check Syntax**: Click the "Check Syntax" button to parse the code and view the parse tree.

### Code Overview
- **GUI Code**: Initializes the main application window and defines the layout and interaction of the GUI components.
- **Parser Code**: Implements a simple parser using context-free grammar (CFG) defined with NLTK.
- **Notification Bar**: Provides visual feedback on the syntax check results.

### Project Structure
- `app.py`: Main application script.
- `images/`: Directory containing images used in GUI.
- `README.md`: This file.

### Screenshots
*Main Window Application*

![alt text](https://serving.photos.photobox.com/610683283f00b38e998d663589c458036d72cd3c032b41a547e777482ad77c7ebfd34bd6.jpg)

*Syntax error notification*

![alt text](https://serving.photos.photobox.com/200076594ac49067283a4cb4342e6c1959d0370dba3593890586d990f263b64c9382c683.jpg)

*Parsed Tree*

![alt text](https://serving.photos.photobox.com/443571501ef97108ff1fde762228bcff6ac3e2fd33ca6da3c5356dfa4ce22e82db7c9e26.jpg)

### License
This project is licensed under the MIT License. See the [LICENSE]() file for more details.

### Acknowledgements
- [NLTK](https://www.nltk.org/)
- [customTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Pillow (PIL)](https://python-pillow.org/)

**Notes**: This is not full parser, this is a simple parser for (`for`, `if else`) statements.
___
Feel free to contribute to this project by creating issues or submitting pull requests. For any questions, you can contact me at [gemyyahmedd@gmail.com]().