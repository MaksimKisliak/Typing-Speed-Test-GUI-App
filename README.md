# Typing Speed Test
<p>This is a simple typing speed test program written in Python using the Tkinter library for the GUI. The program displays a random piece of text and the user has 60 seconds to type it as accurately and quickly as possible. At the end of the test, the program displays the number of words typed per minute. The application was created as part of the 100 Days of Code - The Complete Python Pro Bootcamp course challenge.</p>How to use
<ol>
 <li>Install Python on your computer if it is not already installed.</li>
 <li>Download the <code>typing_speed_test.py</code> file.</li>
 <li>Open a terminal or command prompt and navigate to the directory containing the <code>typing_speed_test.py</code> file.</li>
 <li>Run the command <code>python typing_speed_test.py</code>.</li>
 <li>Press Enter to start the typing test.</li>
 <li>Type the displayed text as quickly and accurately as possible.</li>
 <li>After 60 seconds, the program will display the number of words typed per minute.</li>
 <li>Click the "Retry" button to start a new test.</li>
</ol>Dependencies
<ul>
 <li>Python 3.x</li>
 <li>Tkinter library</li>
</ul>How it works
<p>The program chooses a random piece of text from a list of possible texts and displays it on the screen. The user has 60 seconds to type the text as accurately and quickly as possible. The program uses the <code>Tkinter</code> library to create the graphical user interface. The typing test starts when the user presses the Enter key. During the typing test, the program checks each key that the user types to make sure it matches the next character in the text. If the key matches, the program displays the next character in the text and moves the cursor to the next position. After 60 seconds, the program calculates the number of words typed and displays the result on the screen. The user can click the "Retry" button to start a new typing test.</p>
