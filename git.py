exec(open('util.py').read())
def git(inp):
		
	from github import Github

	# Authentication
	g = Github("github788788", "Viovio2@")

	# Access the repository
	repo = g.get_repo("github788788/code")

	# File to upload
	file_content = "naw"
	file_name = "tes.txt"

	# Upload file
	repo.create_file(file_name, "commit message", file_content)
	
inp = []
git(inp)