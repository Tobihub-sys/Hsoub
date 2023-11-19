class ProgrammerRole:
  def __init__(self, lang, projects):
    self.lang = lang
    self. projects = projects

  def assign_project(self, project):
    self.projects.append(project)

  def get_projects(self):
    print("projects:")
    print('=' * 10)
    projects_list = []
    for number, project in enumerate(self.projects):
      projects_list.append(f'{number + 1}. {project}')
    return '\n'.join(projects_list)