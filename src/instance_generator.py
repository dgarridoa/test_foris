import numpy as np


def random_generator(size, path, seed=0):
    """
    Instances generator

    Parameters
    ----------
    size: tuple,
        size = (s, c, n), where "s" represents the number of stundents,
        "c" the number of classrooms and "n" represents the number of presences.
    path: str
        path to save.
    seed: int, default 0
        random seed.
    """
    # set random seed
    np.random.seed(seed)
    s, c, n = size
    letters = [w for w in "abcdefghijklmnopqrstuvwxyz"]
    # student generator
    students = ["".join(np.random.choice(letters, size=np.random.randint(low=4, high=8))) 
    for i in range(s)]
    # classroom generator
    classrooms = ["".join(np.random.choice(letters)+str(np.random.randint(low=100, high=999))) 
    for i in range(c)]
    ### presence generator ###
    p_students = np.random.choice(a=students, size=n)
    p_classrooms = np.random.choice(a=classrooms, size=n)
    # days generator
    days = np.random.randint(low=1, high=7, size=n)
    # star time generator
    ti = np.random.randint(low=0, high=1439, size=n)
    # final time generator, tf>=ti 
    tf = [np.random.randint(low=ti[i], high=1439) for i in range(n)]
    # formating time
    ti = ["{:02d}:{:02d}".format(*divmod(ti[i], 60)) for i in range(n)]
    tf = ["{:02d}:{:02d}".format(*divmod(tf[i], 60)) for i in range(n)]

    ### save instance ###
    with open(path, "w") as f:
        # add students
        f.write("\n".join([f"Student {students[i]}" for i in range(s)]))
        f.write("\n")
        # add presences
        f.write("\n".join(
        [f"Presence {p_students[i]} {days[i]} {ti[i]} {tf[i]} {p_classrooms[i]}"
        for i in range(n)]
        ))