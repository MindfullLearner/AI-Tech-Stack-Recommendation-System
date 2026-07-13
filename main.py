# Career Database
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
    user_skills = input_skills.split(",")
    user_skills = [skill.strip().lower() for skill in user_skills]

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
    print("=========================")
    if rank == 1:
        title = "🏆 BEST MATCH"

    elif rank == 2:
        title = "🥈 Recommendation #2"

    elif rank == 3:
        title = "🥉 Recommendation #3"

    else:
        title = f"Recommendation #{rank}"
    print(" "+title)
    print("=========================")
    print(f"🏆 Career: {career}")
    
    stars, rating = get_match_rating(details["percentage"])
    print(stars)
    print(rating)
    print(f"\n📊 Match Percentage: {details['percentage']:.2f}%")
    print("\nDescription:\n"+details['description'])
    print("\nSalary:\n"+details['salary'])
    print("\nDifficulty:\n"+details['difficulty'])
    print("\nLearning Time:\n"+details['learning_time'])
    print("\nMatched Skills:")
    if details["matched"]:
        print(", ".join(details["matched"]))
    else:
        print("None")
    print("\nMissing Skills:")
    if details["missing"]:
        print(", ".join(details["missing"]))
    else:
        print("None")
    print("\n🛣️ Learning Roadmap:")

    for step in details["roadmap"]:
        print(f"• {step}")

    
# Main 
print("========================================")
print("   AI Tech Stack Recommendation System")
print("========================================")

while True:
    input_skills = input("Enter your skills (comma separated): ")

    if not input_skills.strip():
        print("❌ Please enter at least one skill.")
    else:
        break

result = recommendations(input_skills)
print("\n===== Career Recommendations =====")

displayed_careers = 0
rank = 1
for career, details in result:

    if details["percentage"] == 0:
        continue
    display_recommendation(career, details, rank)
    rank+=1
    displayed_careers += 1    
if displayed_careers == 0:
    print("\n❌ No matching career found.")
    print("Please enter more technical skills like Python, HTML, SQL, JavaScript, etc.")