import requests
import openai

# Set your GitHub API token and OpenAI API key here
GITHUB_API_TOKEN = "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"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

# Initialize OpenAI
openai.api_key = OPENAI_API_KEY

def get_user_repositories(username):
    url = f"https://api.github.com/users/manas95826/repos"
    response = requests.get(url)
    repositories = response.json()
    return repositories

def fetch_repository_code(repo):
    # Implement code fetching logic here
    pass

def preprocess_code(code):
    # Implement preprocessing techniques here
    return preprocessed_code

def assess_technical_complexity(code):
    prompt = f"Assess the technical complexity of the following code:\n\n{code}"
    response = openai.Completion.create(
        engine="text-davinci-003",  # or other GPT variant
        prompt=prompt,
        max_tokens=50  # Adjust as needed
    )
    complexity_score = response.choices[0].text
    return complexity_score

def find_most_complex_repository(username):
    repositories = get_user_repositories(username)
    most_complex_repository = None
    highest_score = float("-inf")

    for repo in repositories:
        code = fetch_repository_code(repo)
        preprocessed_code = preprocess_code(code)
        complexity_score = assess_technical_complexity(preprocessed_code)

        if complexity_score > highest_score:
            highest_score = complexity_score
            most_complex_repository = repo

    return most_complex_repository, highest_score

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    most_complex_repo, complexity_score = find_most_complex_repository(username)
    
    print(f"The most complex repository is: {most_complex_repo['name']}")
    print(f"Complexity Score: {complexity_score}")
