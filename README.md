# P2P with Machine Learning

### About
The aim is to implement a terminal based application with a P2P network that uses the TCP protocol (or existing P2P Framework). The motivation behind the project is to build a system to facilitate real time crowdsourced tutoring / student space where students (and faculties) can come together to assist peers (and students). On top of that machine learning nodes will enhance the system by offering the ability to convert the documents from formats like images / audio files to text files. 
The system consists of multiple clusters of nodes (Student, Professor, ML, Chat) responsible for various features within the application. There would be features like sharing notes in forms such as text, audio and Image. Additionally, there would be an exchange of chat messages.


### Installation and setup 
- #### This project uses Google tesseract which can be installed from any of the following link:
    - https://digi.bib.uni-mannheim.de/tesseract/
    - https://github.com/tesseract-ocr/tesseract

- #### For installtion of other dependencies 
    - pip install -r requirements.txt

### Example for everyone joining the room
First node (which automatically becomes the server)
```
cd <location of root of repo>
python start.py
What is your name? ishan
What course is this for? SWE
Starting collaboration!
ishan is now the chat node of this room.
```

```
Additional node (which automatically becomes the server)
cd <location of root of repo>
python start.py
What is your name? richa
What course is this for? swe
Starting collaboration!
You have joined SWE's room. Welcome!
```

Additional node (which automatically becomes the server)
```
cd <location of root of repo>
python start.py
What is your name? andrew
What course is this for? swe
Starting collaboration!
You have joined SWE's room. Welcome!
```

Additional node (which automatically becomes the server)
```
cd <location of root of repo>
python start.py
What is your name? harsh
What course is this for? swe
Starting collaboration!
You have joined SWE's room. Welcome!
```

### Example for ML functions

Adding ML node (which automatically becomes the server)
```
cd <location of root of repo>
python start.py
What is your name? ml_node
What course is this for? swe
Starting collaboration!
You have joined SWE's room. Welcome!
```

Now anyone in the chat can write:
```
[ML] test.png
```
After this ml_node will broadcast IMG->TXT data with the help of main chat node to all the nodes

### Example for saving chat locally for future reference
```
savehistory()
```
This will save history of the chat for that node in their local dir with date and time


Can't use multiprocessing instead of threading in Python because : https://stackoverflow.com/questions/42837544/python-3-multiprocessing-eoferror-eof-when-reading-a-line


### Future Work

#### Code

- Integartion Voice to TXT
- Add authentication - professor to the [PROF announcement] [Lecture upload]

#### DONE
- ML node integartion
- (IMP) Facilitator bug -> everyone tries to become the server
- ML node can't be facilatator

### Diagrams

#### Basic High Level Design Implementation
![High Level](Diagram/HighLevelDesign.PNG)

#### Use Case Implementation
![Use Case](Diagram/BasicUseCase.PNG)

