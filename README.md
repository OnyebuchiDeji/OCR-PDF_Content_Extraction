####    Date: 15th September, 2025


##  Extracting PDF Content with Python


##  What is Done?

Different libraries are used for different use cases.
This practice project shows the use of 3 different libraries to accomplish the given tasks

##  Libraries Installed

+   For Text Extraction for Processing: `pip install pdfminer.six`
+   For Images: `pip install PyMuPDF pillow`
+   For Tables: `pip install tabula-py jpype1`  --- jpype1 is a dependency of tabula-py

##  NOTE!
The `app_3.py` doesn't work due to issues with jpype1. It gave this error: 
    ```
        jpype._jvmfinder.JVMNotFoundException: No JVM shared library file (jvm.dll) found. Try setting up the JAVA_HOME environment variable properly.
    ```
Since I wasn't guided through this process, and hence donm't know what hava library file is needed, I ignore this last app
as the issue is most likely due to updates (since it worked in the tutorial video).

I explore another solution for extracting pdf tables in another practice project, and the `app_1.py` and `app_2.py` work so all is well.

### References
**"Extract PDF Content with Python", NeuralNine (2022) [Youtube]**

####    Done: 15th September, 2025