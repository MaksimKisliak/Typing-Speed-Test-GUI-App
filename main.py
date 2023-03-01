import tkinter as tk
import random


class TypeSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title('Type Speed Test')
        self.root.geometry('700x700')
        self.root.option_add("*Label.Font", "consolas 30")
        self.root.option_add("*Button.Font", "consolas 30")

        self.possible_texts = ["The mission of this organization is to provide resources and assistance to "
                               "underprivileged communities. They believe that everyone deserves access to education "
                               "and opportunities. This nonprofit is dedicated to improving the lives of people "
                               "living in poverty. Their programs include job training, housing assistance, "
                               "and educational scholarships. They rely on the support of volunteers and donors to "
                               "achieve their goals.", "The purpose of this book is to help readers improve their "
                                                       "writing skills. The author provides practical advice and "
                                                       "exercises to help readers become better writers. The book is "
                                                       "suitable for beginners and experienced writers alike. It "
                                                       "covers a range of topics, including grammar, style, "
                                                       "and structure. The author's writing style is clear and "
                                                       "engaging, making the book easy to read and understand.",
                               "The aim of this research project is to investigate the impact of social media on "
                               "mental health. The study will involve surveying a sample of young adults to determine "
                               "their social media usage and its effect on their mental wellbeing. The findings will "
                               "be used to develop recommendations for mental health professionals and social media "
                               "companies. The researchers hope to contribute to a better understanding of this "
                               "important issue.", "The goal of this company is to create innovative and sustainable "
                                                   "solutions to environmental problems. They specialize in "
                                                   "developing renewable energy technologies and reducing waste. "
                                                   "Their products include solar panels, wind turbines, "
                                                   "and biodegradable packaging. The company is committed to reducing "
                                                   "its own environmental footprint and promoting sustainability in "
                                                   "the wider community.", "The objective of this course is to "
                                                                           "provide students with a thorough "
                                                                           "understanding of economics. Topics "
                                                                           "covered include microeconomics, "
                                                                           "macroeconomics, and international trade. "
                                                                           "The course will be taught by experienced "
                                                                           "professors and will involve lectures, "
                                                                           "discussions, and assignments. Students "
                                                                           "will gain practical skills that they can "
                                                                           "apply in their personal and professional "
                                                                           "lives. Upon completion of the course, "
                                                                           "students will receive a certificate of "
                                                                           "achievement."]

        self.label_left = None
        self.label_right = None
        self.current_letter_label = None
        self.timeleft_label = None
        self.result_label = None
        self.result_button = None
        self.write_able = None
        self.passed_seconds = None

        self.reset_writing_labels()

    def key_press(self, event=None):
        try:
            if event.char.lower() == self.label_right.cget('text')[0].lower():
                self.label_right.configure(text=self.label_right.cget('text')[1:])
                self.label_left.configure(text=self.label_left.cget('text') + event.char.lower())
                self.current_letter_label.configure(text=self.label_right.cget('text')[0])
        except tk.TclError:
            pass

    def reset_writing_labels(self):
        text = random.choice(self.possible_texts).lower()
        split_point = 0
        self.label_left = tk.Label(self.root, text=text[0:split_point], fg='grey')
        self.label_left.place(relx=0.5, rely=0.5, anchor=tk.E)
        self.label_right = tk.Label(self.root, text=text[split_point:])
        self.label_right.place(relx=0.5, rely=0.5, anchor=tk.W)
        self.current_letter_label = tk.Label(self.root, text=text[split_point], fg='grey')
        self.current_letter_label.place(relx=0.5, rely=0.6, anchor=tk.N)
        self.timeleft_label = tk.Label(self.root, text='0 Seconds', fg='grey')
        self.timeleft_label.place(relx=0.5, rely=0.4, anchor=tk.S)
        self.write_able = True
        self.root.bind('<Key>', self.key_press)
        self.passed_seconds = 0
        self.root.after(60000, self.stop_test)
        self.root.after(1000, self.add_second)

    def stop_test(self):
        self.write_able = False
        amount_words = len(self.label_left.cget('text').split(' '))
        self.timeleft_label.destroy()
        self.current_letter_label.destroy()
        self.label_right.destroy()
        self.label_left.destroy()
        self.result_label = tk.Label(self.root, text=f'Words per Minute: {amount_words}', fg='black')
        self.result_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.result_button = tk.Button(self.root, text=f'Retry', command=self.restart)
        self.result_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def restart(self):
        self.result_label.destroy()
        self.result_button.destroy()
        self.reset_writing_labels()

    def add_second(self):
        self.passed_seconds += 1
        self.timeleft_label.configure(text=f'{self.passed_seconds} Seconds')
        if self.write_able:
            self.root.after(1000, self.add_second)


if __name__ == '__main__':
    root = tk.Tk()
    TypeSpeedTest(root)
    root.mainloop()