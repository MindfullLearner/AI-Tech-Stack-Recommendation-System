import tkinter  as tk    #for dekstop graphical interface

#Career Database
career_database = {
    "Data Scientist": {
        "skills": [
            "SQL",
            "Python",
            "Machine Learning",
            "Data Analysis"
        ],

        "description": "Analyzes data and builds machine learning models to solve real-world problems and help organizations make data-driven decisions.",

        "salary": "PKR 120,000 - 350,000/month",

        "difficulty": "⭐⭐⭐⭐☆",

        "learning_time": "6-12 months",

        "roadmap": [
            "Python",
            "SQL",
            "Pandas",
            "NumPy",
            "Data Visualization",
            "Machine Learning",
            "Deep Learning"
        ]
    },

    "Frontend Developer": {
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React"
        ],

        "description": "Builds websites and user interfaces.",

        "salary": "PKR 80,000 - 180,000/month",

        "difficulty": "⭐⭐☆☆☆",

        "learning_time": "2-4 months",

        "roadmap": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Git",
            "REST APIs"
        ]
    },

    "Backend Developer": {
        "skills": [
            "Java",
            "Python",
            "SQL",
            "APIs"
        ],

        "description": "Develops the server-side logic, databases, and APIs that power web and mobile applications.",

        "salary": "PKR 90,000 - 220,000/month",

        "difficulty": "⭐⭐⭐☆☆",

        "learning_time": "4-8 months",

        "roadmap": [
            "Java or Python",
            "Databases (SQL)",
            "REST APIs",
            "Git",
            "Authentication",
            "Deployment"
        ]
    },

    "DevOps Engineer": {
        "skills": [
            "Docker",
            "AWS",
            "Kubernetes",
            "Git"
        ],

        "description": "Automates software development, deployment, and infrastructure management to improve reliability and scalability.",

        "salary": "PKR 150,000 - 400,000/month",

        "difficulty": "⭐⭐⭐⭐☆",

        "learning_time": "6-12 months",

        "roadmap": [
            "Linux",
            "Git",
            "Networking Basics",
            "Docker",
            "CI/CD",
            "Kubernetes",
            "AWS or Azure",
            "Terraform",
            "Monitoring"
        ]
    },

    "MERN Stack Developer": {
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Node.js",
            "MongoDB"
        ],

        "description": "Develops full-stack web applications using MongoDB, Express.js, React, and Node.js.",

        "salary": "PKR 100,000 - 250,000/month",

        "difficulty": "⭐⭐⭐☆☆",

        "learning_time": "5-8 months",

        "roadmap": [
            "HTML",
            "CSS",
            "JavaScript",
            "Git",
            "React",
            "Node.js",
            "Express.js",
            "MongoDB",
            "REST APIs",
            "Authentication",
            "Deployment"
        ]
    }
}




def recommendations(input_skills):

    # Convert input into a clean list
    user_skills = [
    skill.strip().lower()
    for skill in input_skills.split(",")
    if skill.strip()
]

    results = {}

    # Compare user skills with each career
    for career, details in career_database.items():

        score = 0
        matched_skills = []
        missing_skills = []
        skills = details["skills"]
        for skill in skills:

            if skill.lower() in user_skills:
                score += 1
                matched_skills.append(skill)   # Original name
            else:
                missing_skills.append(skill)

        percentage = (score / len(skills)) * 100

        results[career] = {
            "percentage": percentage,

            "matched": matched_skills,

            "missing": missing_skills,

            "description": details["description"],

            "salary": details["salary"],

            "difficulty": details["difficulty"],

            "learning_time": details["learning_time"],

            "roadmap": details["roadmap"]
        }

    # Sort from highest percentage to lowest
    sorted_results = sorted(
        results.items(),
        key=lambda item: item[1]["percentage"],
        reverse=True
    )

    return sorted_results

def get_match_rating(percentage):
    if percentage >=90:
        return "⭐⭐⭐⭐⭐", "Excellent Match"
    elif percentage >=70:
        return "⭐⭐⭐⭐☆", "Strong Match"
    elif percentage >=50:
        return "⭐⭐⭐☆☆", "Good Match"
    elif percentage >=30:
        return "⭐⭐☆☆☆", "Beginner Match"
    else:
        return "⭐☆☆☆☆", "Weak Match"
    
# dispaly of each career details
def display_recommendation(career, details, rank):
    output=""
    output += "=========================\n"
    if rank == 1:
        title = "🏆 BEST MATCH"

    elif rank == 2:
        title = "🥈 Recommendation #2"

    elif rank == 3:
        title = "🥉 Recommendation #3"

    else:
        title = f"Recommendation #{rank}"
    output+= " "+title+"\n"
    output+= "=========================\n"
    output+=f"🏆 Career: {career}"+"\n"
    
    stars, rating = get_match_rating(details["percentage"])
    output+= stars +"\n"
    output+= rating +"\n"
    output+=f"\n📊 Match Percentage: {details['percentage']:.2f}%"
    output+= "\nDescription:\n"+details['description']
    output+="\nSalary:\n"+details['salary']
    output+="\nDifficulty:\n"+details['difficulty']
    output+="\nLearning Time:\n"+details['learning_time']
    output+="\nMatched Skills:"
    if details["matched"]:
        output+=", ".join(details["matched"])+"\n"
    else:
        output+="None"+"\n"
    output+="\nMissing Skills:"
    if details["missing"]:
        output+=", ".join(details["missing"])+"\n"
    else:
        output+="None"+"\n"
    output+="\n🛣️ Learning Roadmap:"+"\n"

    for step in details["roadmap"]:
        output+=f"• {step}\n"
    return output

    
# # Main 
# print("========================================")
# print("   AI Tech Stack Recommendation System")
# print("========================================")

# while True:
#     input_skills = input("Enter your skills (comma separated): ")

#     if not input_skills.strip():
#         print("❌ Please enter at least one skill.")
#     else:
#         break

# result = recommendations(input_skills)
# print("\n===== Career Recommendations =====\n")

# displayed_careers = 0
# rank = 1
# for career, details in result:

#     if details["percentage"] == 0:
#         continue
#     text=display_recommendation(career, details, rank)
#     print(text)
#     rank+=1
#     displayed_careers += 1    
# if displayed_careers == 0:
#     print("\n❌ No matching career found.")
#     print("Please enter more technical skills like Python, HTML, SQL, JavaScript, etc.")
def recommend():
    input_skills = skills_entry.get()

    result = recommendations(input_skills)

    all_output = ""
    rank = 1
    displayed_careers = 0

    for career, details in result:

        if details["percentage"] == 0:
            continue

        text = display_recommendation(career, details, rank)

        all_output += text + "\n"

        rank += 1
        displayed_careers += 1

    if displayed_careers == 0:
        all_output = (
            "❌ No matching career found.\n"
            "Please enter more technical skills."
        )

    results_text.delete("1.0", tk.END)

    results_text.insert(
        tk.END,
        all_output
    )
#Tkinter 
window = tk.Tk()  #creates actual window application


title_label = tk.Label(         #creates a text label
    window,  #first argument tells where to put this label as it says window it means put the following label in main window 
    text="AI Tech Stack Recommendation System",
    font=("Arial", 18, "bold")
)

title_label.pack(pady=20)  # this helps the text  to place it on window 

#creates label for taking skills from user
skills_label = tk.Label(
    window,
    text="Enter your skills (comma separated):",
    font=("Arial", 12)
)

skills_label.pack()
#Widget takes input from user 
#Entry is a single line input box it acts in place of input()
skills_entry = tk.Entry(
    window,
    width=50
)

skills_entry.pack(pady=10)
#Create button for taking input
recommend_button = tk.Button(
    window,
    text="Recommend Careers",
    command=recommend   #call function named recommend  when user clicls on button
)

recommend_button.pack(pady=10)
#create ouput arae where the result will be displayed
results_frame = tk.Frame(window)
results_frame.pack(pady=10)

scrollbar = tk.Scrollbar(results_frame)

results_text = tk.Text(
    results_frame,
    width=80,
    height=25,
    yscrollcommand=scrollbar.set
)

scrollbar.config(command=results_text.yview)

results_text.pack(side=tk.LEFT)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


window.mainloop()