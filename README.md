####  Smart Study Predictor

An AI-powered machine learning model that predicts the ideal study time for a student based on mood, sleep, stress, previous study time, and energy level.



##### &#x20; # Project Overview



Students often struggle to decide how long they should study on a particular day.

Factors like sleep, stress, mood, and energy influence productivity — but students rarely track these patterns.



Smart Study Predictor uses Machine Learning to recommend the optimal number of study hours for better learning efficiency and time management.



This project is part of the BYOP (Bring Your Own Project) requirement.



##### &#x20; # Features



1. Predicts recommended study time (0–8 hours)
2. Uses student daily condition inputs:
3. Mood (1–5)
4. Stress level (1–5)
5. Sleep hours
6. Previous day’s study hrs
7. Energy level (1–5)
8. Generates dataset automatically (no external CSV needed)
9. Fully trained ML model (Linear Regression)
10. Simple and beginner-friendly code
11. Clean and readable Python structure



##### &#x20;  # Tech Stack



* Python
* NumPy
* Pandas
* Scikit-learn
* Random module



##### &#x20;# How to Run This Project



1\. Install Dependencies



Run this in terminal:



&#x20;  pip install numpy pandas scikit-learn

2\. Run the Python File

&#x20;  python main.py

3\. Enter the Required Inputs



The program will ask for:



* Mood (1–5)
* Stress (1–5)
* Sleep hours (3–10)
* Previous day study hours (0–6)
* Energy (1–5)



Then it will output:



Recommended Study Time Today: X hours



##### &#x20;# Model Used



✔ Linear Regression

The model is trained on synthetic (generated) data with 500+ records based on realistic patterns related to student behavior.



✔ Dataset Generation Logic

The dataset includes:



1. mood
2. stress
3. sleep\_hours
4. prev\_study\_hours
5. energy
6. recommended\_study (target)



The target is computed using weighted combinations of these features.



##### &#x20; # Outcome



This project helps students learn about:



1. Data generation
2. Feature engineering
3. Model training
4. Evaluation
5. Real-world application of ML for productivity



##### &#x20;# Contribution



Feel free to:



* Fork
* Improve
* Add features like:
* GUI
* Better ML model
* Saving logs
* Graphs
* Mobile app version



##### &#x20; # License



This project is open-source under the MIT License.



