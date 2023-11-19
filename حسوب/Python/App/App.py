from Roles import *
from Payments import *
from Profile import Profile

if __name__ == '__main__':
    jawad = Programmer('Jawad', 'Kareem', 'Python', 'HR System', 4000)
    maha = FreelancerProgrammer('MAha', 'Ali', 50, 30, 'PHP', ['Website'])
    ahmad = Manager('Ahmad', 'Saeed', 5000, [jawad, maha])

    
    jawadProfile = Profile('Iraq, Baghdad', '394888', 'jawad@example.com', True)

    print(jawadProfile)