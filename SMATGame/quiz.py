'''
import pygame as pg
import random
import sys

class Quiz:
    used_questions = set()  # A global set to track used questions

    def __init__(self, game):
        self.game = game
        self.all_questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
            {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
            {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Jupiter", "Mars", "Saturn"], "answer": "Jupiter"},
            {"question": "Who invented the telephone?", "options": ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Albert Einstein"], "answer": "Alexander Graham Bell"},
            {"question": "Which language is used for web development?", "options": ["Python", "Java", "HTML", "C++"], "answer": "HTML"},
            {"question": "What is the capital of Japan?", "options": ["Tokyo", "Osaka", "Kyoto", "Nagoya"], "answer": "Tokyo"},
            {"question": "What is the square root of 16?", "options": ["2", "3", "4", "5"], "answer": "4"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Venus", "Jupiter"], "answer": "Mars"},
            {"question": "Who wrote 'Romeo and Juliet'?", "options": ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"], "answer": "William Shakespeare"},
            {"question": "Which programming language is primarily used for Android app development?", "options": ["Java", "Swift", "Python", "C#"], "answer": "Java"},
            {"question": "What is the chemical symbol for water?", "options": ["H2O", "CO2", "O2", "NaCl"], "answer": "H2O"},
            {"question": "Who was the first President of the United States?", "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"], "answer": "George Washington"},
            {"question": "What is the speed of light?", "options": ["300,000 km/s", "150,000 km/s", "400,000 km/s", "250,000 km/s"], "answer": "300,000 km/s"},
            {"question": "Which element has the atomic number 1?", "options": ["Hydrogen", "Oxygen", "Carbon", "Helium"], "answer": "Hydrogen"},
            {"question": "What is the national language of China?", "options": ["Mandarin", "Cantonese", "Japanese", "Korean"], "answer": "Mandarin"},
            {"question": "Which organ in the human body is responsible for pumping blood?", "options": ["Heart", "Liver", "Brain", "Lungs"], "answer": "Heart"},
            {"question": "Who painted the Mona Lisa?", "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"], "answer": "Leonardo da Vinci"},
            {"question": "Which gas do plants use for photosynthesis?", "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
            {"question": "What is the smallest unit of life?", "options": ["Cell", "Atom", "Molecule", "Organ"], "answer": "Cell"},
            {"question": "Which continent is known as the 'Dark Continent'?", "options": ["Africa", "Asia", "South America", "Europe"], "answer": "Africa"},
            {"question": "What is the main ingredient in bread?", "options": ["Flour", "Sugar", "Salt", "Butter"], "answer": "Flour"},
            {"question": "Who discovered gravity?", "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Marie Curie"], "answer": "Isaac Newton"},
            {"question": "What is the largest mammal in the world?", "options": ["Blue Whale", "Elephant", "Giraffe", "Great White Shark"], "answer": "Blue Whale"},
            {"question": "Which country is known as the Land of the Rising Sun?", "options": ["Japan", "China", "Thailand", "India"], "answer": "Japan"},
            {"question": "What is the boiling point of water at sea level?", "options": ["100°C", "90°C", "80°C", "120°C"], "answer": "100°C"}
        ]
        self.available_questions = [q for q in self.all_questions if q["question"] not in Quiz.used_questions]
        self.current_question = None
        self.selected_option = None
        self.correct_answers = 0
        self.game_over = False
        self.show_next_question()

    def show_next_question(self):
        """Select one random question and display it."""
        if len(self.available_questions) > 0:
            self.current_question = random.choice(self.available_questions)
            Quiz.used_questions.add(self.current_question["question"])  # Mark question as used
            self.available_questions.remove(self.current_question)  # Remove from available questions
        else:
            self.game_over = True  # No more questions available

    def handle_event(self, event):
        """Handle user input for answering the quiz."""
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                self.selected_option = self.current_question["options"][0]
            elif event.key == pg.K_2:
                self.selected_option = self.current_question["options"][1]
            elif event.key == pg.K_3:
                self.selected_option = self.current_question["options"][2]
            elif event.key == pg.K_4:
                self.selected_option = self.current_question["options"][3]

            if self.selected_option:
                self.check_answer()

    def check_answer(self):
        """Check if the selected answer is correct."""
        if self.selected_option == self.current_question["answer"]:
            self.correct_answers += 1
            if self.correct_answers >= 2:  # Resume game after 2 correct answers
                self.game.state = 'game'  # Switch back to game state
                self.game.quiz = None
                self.game.quiz_timer = pg.time.get_ticks()  # Reset quiz timer
            else:
                self.show_next_question()  # Show next question if available
        else:
            self.game_over = True  # End game on wrong answer
            self.game_over_screen()

    def draw(self):
        """Draw the quiz question and options on the screen."""
        font = pg.font.Font(None, 36)

        if self.current_question:
            question_text = font.render(self.current_question["question"], True, (255, 255, 255))
            self.game.screen.blit(question_text, (50, 50))

            for i, option in enumerate(self.current_question["options"]):
                option_text = font.render(f"{i + 1}. {option}", True, (255, 255, 255))
                self.game.screen.blit(option_text, (50, 100 + i * 50))

        if self.game_over:
            self.game_over_screen()

    def game_over_screen(self):
        """Display game over message."""
        font = pg.font.Font(None, 48)
        result_text = font.render(f"Game Over! You answered {self.correct_answers} correctly.", True, (255, 255, 255))
        self.game.screen.blit(result_text, (50, self.game.screen.get_height() // 2))
        self.game.sound.game_over.play()
        self.game.object_renderer.game_over_quiz()
        pg.display.flip()
        pg.time.delay(2000)
        pg.quit()
        sys.exit()

    def update(self):
        """Update quiz logic."""
        if self.game_over:
            return
'''


import pygame as pg
import random
import sys

class Quiz:
    used_questions = set()  # A global set to track used questions

    def __init__(self, game):
        self.game = game
        self.all_questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
            {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
            {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Jupiter", "Mars", "Saturn"], "answer": "Jupiter"},
            {"question": "Who invented the telephone?", "options": ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Albert Einstein"], "answer": "Alexander Graham Bell"},
            {"question": "Which language is used for web development?", "options": ["Python", "Java", "HTML", "C++"], "answer": "HTML"},
            {"question": "What is the capital of Japan?", "options": ["Tokyo", "Osaka", "Kyoto", "Nagoya"], "answer": "Tokyo"},
            {"question": "What is the square root of 16?", "options": ["2", "3", "4", "5"], "answer": "4"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Venus", "Jupiter"], "answer": "Mars"},
            {"question": "Who wrote 'Romeo and Juliet'?", "options": ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"], "answer": "William Shakespeare"},
            {"question": "Which programming language is primarily used for Android app development?", "options": ["Java", "Swift", "Python", "C#"], "answer": "Java"},
            {"question": "What is the chemical symbol for water?", "options": ["H2O", "CO2", "O2", "NaCl"], "answer": "H2O"},
            {"question": "Who was the first President of the United States?", "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"], "answer": "George Washington"},
            {"question": "What is the speed of light?", "options": ["300,000 km/s", "150,000 km/s", "400,000 km/s", "250,000 km/s"], "answer": "300,000 km/s"},
            {"question": "Which element has the atomic number 1?", "options": ["Hydrogen", "Oxygen", "Carbon", "Helium"], "answer": "Hydrogen"},
            {"question": "What is the national language of China?", "options": ["Mandarin", "Cantonese", "Japanese", "Korean"], "answer": "Mandarin"},
            {"question": "Which organ in the human body is responsible for pumping blood?", "options": ["Heart", "Liver", "Brain", "Lungs"], "answer": "Heart"},
            {"question": "Who painted the Mona Lisa?", "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"], "answer": "Leonardo da Vinci"},
            {"question": "Which gas do plants use for photosynthesis?", "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
            {"question": "What is the smallest unit of life?", "options": ["Cell", "Atom", "Molecule", "Organ"], "answer": "Cell"},
            {"question": "Which continent is known as the 'Dark Continent'?", "options": ["Africa", "Asia", "South America", "Europe"], "answer": "Africa"},
            {"question": "What is the main ingredient in bread?", "options": ["Flour", "Sugar", "Salt", "Butter"], "answer": "Flour"},
            {"question": "Who discovered gravity?", "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Marie Curie"], "answer": "Isaac Newton"},
            {"question": "What is the largest mammal in the world?", "options": ["Blue Whale", "Elephant", "Giraffe", "Great White Shark"], "answer": "Blue Whale"},
            {"question": "Which country is known as the Land of the Rising Sun?", "options": ["Japan", "China", "Thailand", "India"], "answer": "Japan"},
            {"question": "What is the boiling point of water at sea level?", "options": ["100°C", "90°C", "80°C", "120°C"], "answer": "100°C"}

        ]
        self.available_questions = [q for q in self.all_questions if q["question"] not in Quiz.used_questions]
        self.current_question = None
        self.selected_option = None
        self.correct_answers = 0
        self.game_over = False
        self.show_next_question()

    def show_next_question(self):
        """Select one random question and display it."""
        if len(self.available_questions) > 0:
            self.current_question = random.choice(self.available_questions)
            Quiz.used_questions.add(self.current_question["question"])  # Mark question as used
            self.available_questions.remove(self.current_question)  # Remove from available questions
        else:
            self.game_over = True  # No more questions available

    def handle_event(self, event):
        """Handle user input for answering the quiz."""
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                self.selected_option = self.current_question["options"][0]
            elif event.key == pg.K_2:
                self.selected_option = self.current_question["options"][1]
            elif event.key == pg.K_3:
                self.selected_option = self.current_question["options"][2]
            elif event.key == pg.K_4:
                self.selected_option = self.current_question["options"][3]

            if self.selected_option:
                self.check_answer()

    def check_answer(self):
        """Check if the selected answer is correct."""
        if self.selected_option == self.current_question["answer"]:
            self.correct_answers += 1
            if self.correct_answers >= 2:  # Resume game after 2 correct answers
                self.game.state = 'game'  # Switch back to game state
                self.game.quiz = None
                self.game.quiz_timer = pg.time.get_ticks()  # Reset quiz timer
            else:
                self.show_next_question()  # Show next question if available
        else:
            self.game_over = True  # End game on wrong answer
            self.game_over_screen()

    def draw(self):
        """Draw the quiz question and options on the screen with a background image."""
        font = pg.font.Font(None, 40)

        # Load background image
        background = pg.image.load("resources\game_over\quiz.png")  # Replace with your image path
        background = pg.transform.scale(background, (self.game.screen.get_width(), self.game.screen.get_height()))  # Scale to fit the screen
        self.game.screen.blit(background, (0, 0))  # Blit background image

        if self.current_question:
            # Render the question text
            question_text = font.render(self.current_question["question"], True, (255, 255, 255))
            question_rect = question_text.get_rect(center=(self.game.screen.get_width() // 2, 150))  # Center horizontally and set vertical position
            self.game.screen.blit(question_text, question_rect)

            # Render the options
            for i, option in enumerate(self.current_question["options"]):
                option_text = font.render(f"{i + 1}. {option}", True, (255, 255, 255))
                option_rect = option_text.get_rect(center=(self.game.screen.get_width() // 2, 250 + i * 50))  # Center horizontally, space vertically
                self.game.screen.blit(option_text, option_rect)

        if self.game_over:
            self.game_over_screen()

    def game_over_screen(self):
        """Display game over message."""
        font = pg.font.Font(None, 48)
        result_text = font.render(f"Game Over! You answered {self.correct_answers} correctly.", True, (255, 255, 255))
        result_rect = result_text.get_rect(center=(self.game.screen.get_width() // 2, self.game.screen.get_height() // 2))  # Center result message
        self.game.screen.blit(result_text, result_rect)
        self.game.sound.game_over.play()
        self.game.object_renderer.game_over_quiz()
        pg.display.flip()
        pg.time.delay(2000)
        pg.quit()
        sys.exit()

    def update(self):
        """Update quiz logic."""
        if self.game_over:
            return
