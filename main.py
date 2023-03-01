import tkinter as tk
import random


class TypingSpeedTest:
    # Initialize the root window
    def __init__(self, root):
        self.root = root
        self.root.title('Typing Speed Test')
        self.root.geometry('700x700')
        self.root.option_add("*Label.Font", "consolas 30")
        self.root.option_add("*Button.Font", "consolas 30")
        # Create the message label
        self.message_label = tk.Label(
            self.root,
            text="Press enter to start",
            font="consolas 20 bold"
        )
        self.message_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        # Define the list of possible texts to type
        self.text_to_test = [
            "The mission of this organization is to provide resources and assistance to underprivileged communities. "
            "They believe that everyone deserves access to education and opportunities. This nonprofit is dedicated "
            "to improving the lives of people living in poverty. Their programs include job training, housing assistance, "
            "and educational scholarships. They rely on the support of volunteers and donors to achieve their goals.",
            "The purpose of this book is to help readers improve their writing skills. The author provides practical "
            "advice and exercises to help readers become better writers. The book is suitable for beginners and experienced "
            "writers alike. It covers a range of topics, including grammar, style, and structure. The author's writing "
            "style is clear and engaging, making the book easy to read and understand.",
            "The aim of this research project is to investigate the impact of social media on mental health. The study "
            "will involve surveying a sample of young adults to determine their social media usage and its effect on their "
            "mental wellbeing. The findings will be used to develop recommendations for mental health professionals and "
            "social media companies. The researchers hope to contribute to a better understanding of this important issue.",
            "The goal of this company is to create innovative and sustainable solutions to environmental problems. They "
            "specialize in developing renewable energy technologies and reducing waste. Their products include solar "
            "panels, wind turbines, and biodegradable packaging. The company is committed to reducing its own environmental "
            "footprint and promoting sustainability in the wider community.",
            "The objective of this course is to provide students with a thorough understanding of economics. Topics "
            "covered include microeconomics, macroeconomics, and international trade. The course will be taught by experienced "
            "professors and will involve lectures, discussions, and assignments. Students will gain practical skills that they "
            "can apply in their personal and professional lives. Upon completion of the course, students will receive a certificate "
            "of achievement."]

        # Create variables to hold labels and other widgets
        self.left_label = None
        self.right_label = None
        self.current_letter_label = None
        self.time_left_label = None
        self.result_label = None
        self.result_button = None
        self.can_type = False
        self.seconds_passed = None

        # Bind the 'Enter' key to start the test
        self.root.bind('<Return>', self.start_test)

    # Method to start the test
    def start_test(self, event=None):
        self.can_type = True
        self.root.unbind('<Return>')
        self.root.bind('<Key>', self.type_key)
        self.message_label.destroy()
        self.reset_writing_labels()

    # Method to handle key presses during the test
    def type_key(self, event=None):
        # If there are no labels to type, return
        if self.right_label is None:
            return
        try:
            # If the typed letter matches the next letter in the right label
            if event.char.lower() == self.right_label.cget('text')[0].lower():
                # Move the right label one character to the left
                self.right_label.configure(
                    text=self.right_label.cget('text')[1:]
                )
                # Add the typed letter to the left label
                self.left_label.configure(
                    text=self.left_label.cget('text') + event.char.lower()
                )
                # Update the current letter label
                self.current_letter_label.configure(
                    text=self.right_label.cget('text')[0]
                )
        # If the typed letter is not a valid character
        except tk.TclError:
            pass

    # Method to reset the labels for a new typing test
    def reset_writing_labels(self):
        # Choose a random text from the possible texts list
        text = random.choice(self.text_to_test).lower()
        split_point = 0
        # Create the labels to display the text
        self.left_label = tk.Label(
            self.root,
            text=text[0:split_point],
            fg='grey'
        )
        self.left_label.place(relx=0.5, rely=0.5, anchor=tk.E)

        self.right_label = tk.Label(
            self.root,
            text=text[split_point:]
        )
        self.right_label.place(relx=0.5, rely=0.5, anchor=tk.W)

        self.current_letter_label = tk.Label(
            self.root,
            text=text[split_point],
            fg='grey'
        )
        self.current_letter_label.place(relx=0.5, rely=0.6, anchor=tk.N)

        self.time_left_label = tk.Label(
            self.root,
            text='0 Seconds',
            fg='grey'
        )
        self.time_left_label.place(relx=0.5, rely=0.4, anchor=tk.S)

        # Set writeable to False to prevent typing until the test starts
        self.can_type = False
        self.seconds_passed = 0

        # Call the stop_test method after 60 seconds
        self.root.after(60000, self.stop_test)

        # Call the add_second method every second
        self.root.after(1000, self.add_second)

        # Set writeable to True to allow typing during the test
        self.can_type = True

    # Method to stop the typing test and display the results
    def stop_test(self):
        # Set writeable to False to prevent typing after the test ends
        self.can_type = False

        # Calculate the number of words typed
        amount_words = len(self.left_label.cget('text').split(' '))

        # Remove the labels used during the typing test
        self.time_left_label.destroy()
        self.current_letter_label.destroy()
        self.right_label.destroy()
        self.left_label.destroy()

        # Display the results and a retry button
        self.result_label = tk.Label(
            self.root,
            text=f'Words per Minute: {amount_words}',
            fg='black'
        )
        self.result_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.result_button = tk.Button(
            self.root,
            text=f'Retry',
            command=self.restart
        )
        self.result_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    # Method to restart the typing test
    def restart(self):
        # Remove the result label and retry button
        self.result_label.destroy()
        self.result_button.destroy()

        # Reset the labels for a new typing test
        self.reset_writing_labels()

    # Method to add one second to the timer and update the label
    def add_second(self):
        # Increase the number of seconds passed by one
        self.seconds_passed += 1

        # Update the time left label
        self.time_left_label.configure(
            text=f'{self.seconds_passed} Seconds'
        )

        # If the test is still ongoing, call the add_second method again after one second
        if self.can_type:
            self.root.after(1000, self.add_second)


if __name__ == '__main__':
    root = tk.Tk()
    TypingSpeedTest(root)
    root.mainloop()
