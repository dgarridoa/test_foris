import numpy as np

def minutes(time):
    # from "HH:MM" to minutes (int)
    h, m = time.split(":")
    return int(h)*60+int(m)

def load_data(path):
    """
    Read the file with student and its presences in classes. Then
    return a dictionary with information grouping by student.

    Example
    -------
        Student Marco
        Student David
        Student Fran
        Presence Marco 1 09:02 10:17 R100
        Presence Marco 3 10:58 12:05 R205
        Presence David 5 14:02 15:46 F505
    
    Parameters
    ----------
    path: str
        path with the input file

    Returns
    -------
    presences: dict
        dictionary with student presences
        {"student1":[[day, minutes], [day, minutes], ...], "student2":[...], ...}    

    """
    with open(path, "r") as f:
        presences = {}
        for line in f:
            tokens = line.split()
            if tokens[0]=="Student":
                presences[tokens[1]] = []
            elif tokens[0]=="Presence":
                if tokens[1] in presences.keys():
                    delta = minutes(tokens[4]) - minutes(tokens[3])
                    if delta>=5:
                        presences[tokens[1]].append([int(tokens[2]), delta])
                else:
                    raise NameError(f"Student {tokens[1]} doesn't exist")
            else:
                raise ValueError("No command given")
    return presences

def build_report(presences):
    """
    Build a report from student presences. The report lists students in descending order by total minutes.

    Example
    -------
        Marco: 142 minutes in 2 days
        David: 104 minutes in 1 day
        Fran: 0 minutes

    Paremeters
    ----------
    presences: dict
        dictionary with student presences
        {"student1":[[day, minutes], [day, minutes], ...], "student2":[...], ...}
    Returns
    -------
    report: str
        report in descending order by total minutes.
    """
    students = list(presences.keys())
    n = len(students)
    results = np.zeros((n,3))
    # get minutes and days per student
    for i in range(n):
        if len(presences[students[i]])>0:
            matrix = np.array(presences[students[i]])
            minutes = matrix[:,1].sum()
            days = len(np.unique(matrix[:,0]))
            results[i] = i, minutes, days
        else:
            results[i] = i, 0, 0
    # sort using quicksort
    results = results[results[:,1].argsort()][::-1]
    # build report
    report  = "\n".join(["{s}: {m:.0f} minutes in {d:.0f} days".format(
        s=students[int(results[i,0])], m=results[i,1], d=results[i,2]) if results[i,1]>0 
        else f"{students[int(results[i,0])]}:  0 minutes" 
        for i in range(n)])
    return report