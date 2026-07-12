
# Career Database
career_database = {
    "Data Scientist": [
        "SQL",
        "Python",
        "Machine Learning",
        "Data Analysis"
    ],
    "Frontend Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React"
    ],
    "Backend Developer": [
        "Java",
        "Python",
        "SQL",
        "APIs"
    ],
    "DevOps Engineer": [
        "Docker",
        "AWS",
        "Kubernetes",
        "Git"
    ],
    "MERN Stack Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js",
        "MongoDB"
    ]
}




def recommendations(input_skills):

    # Convert input into a clean list
    user_skills = input_skills.split(",")
    user_skills = [skill.strip() for skill in user_skills]

    results = {}

    # Compare user skills with each career
    for career, skills in career_database.items():

        score = 0
        matched_skills = []
        missing_skills = []

        for skill in skills:

            if skill in user_skills:
                score += 1
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

        percentage = (score / len(skills)) * 100

        results[career] = {
            "percentage": percentage,
            "matched": matched_skills,
            "missing": missing_skills
        }

    # Sort from highest percentage to lowest
    sorted_results = sorted(
        results.items(),
        key=lambda item: item[1]["percentage"],
        reverse=True
    )

    return sorted_results



# Main 
print("========================================")
print("   AI Tech Stack Recommendation System")
print("========================================")

input_skills = input("Enter your skills (comma separated): ")

result = recommendations(input_skills)

print("\n===== Career Recommendations =====")

displayed_careers = 0

for career, details in result:

    if details["percentage"] == 0:
        continue

    displayed_careers += 1

    print("\n-----------------------------------")
    print(f"🏆 Career: {career}")
    print(f"📊 Match Percentage: {details['percentage']:.2f}%")

    print("✔ Skills You Have:")
    if details["matched"]:
        print(", ".join(details["matched"]))
    else:
        print("None")

    print("❌ Skills You Should Learn:")
    if details["missing"]:
        print(", ".join(details["missing"]))
    else:
        print("None")

if displayed_careers == 0:
    print("No matching career found.")