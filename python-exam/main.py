# server.py
from flask import Flask, jsonify, render_template
import random
import json
from datetime import datetime

app = Flask(__name__)

questions = [
    "1. Write a program to print 'Hello World'.",
    "2. Write a program to print 'Welcome to MRIST'.",
    "3. Write a program to take a name as input and display it.",
    "4. Write a program to take a name as input and display it along with 'MRIST'.",
    "5. Write a program to check whether a given number is even or odd.",
    "6. Write a program to check whether a given number is positive or negative.",
    "7. Write a program to check whether a given character is a vowel or consonant.",
    "8. Write a program to check whether a given year is a leap year.",
    "9. Write a program to calculate the area of a circle.",
    "10. Write a program to calculate the area of a triangle.",
    "11. Write a program to calculate the area of a rectangle.",
    "12. Write a program to calculate the area of a square.",
    "13. Write a program to display numbers from 1 to 100 using a loop.",
    "14. Write a program to display even numbers from 10 to 100.",
    "15. Write a program to display odd numbers from 10 to 100.",
    "16. Write a program to find the sum of the series 1 + 2 + 3 + 4 + … + n.",
    "17. Write a program to find the sum of the series 2 + 4 + 6 + … + n.",
    "18. Write a program to calculate the product of the series 1 × 2 × 3 × 4 × … × n.",
    "19. Write a program to print the following pattern:\n*\n**\n***\n****",
    "20. Write a program to generate the multiplication table of a given number.",
    "21. Write a program using a function to check whether a number is even or odd.",
    "22. Write a program using a function to check whether a year is a leap year."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/spin', methods=['GET'])
def spin():
    selected = random.randint(0, 21)
    return jsonify({
        'question_number': selected + 1,
        'question': questions[selected],
        'total_questions': 22,
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)