class Skill:
    def __init__(self):
        self.skills = ["css", "java", "python"]
    def __str__(self):
        return f"my skills are {self.skills}"
    def __len__(self):
        return len(self.skills)
profile = Skill()
print(profile)
print(len(profile))