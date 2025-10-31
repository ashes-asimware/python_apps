import pickle

course_statistics = [
    {
        "course_name": "Python Programming",
        "enrollment": 150,
        "completed": 120
    },
    {
        "course_name": "Data Science",
        "enrollment": 200,
        "completed": 180
    },
    {
        "course_name": "Web Development",
        "enrollment": 250,
        "completed": 230
    }
]

# Pickle the above data to a file
print(f"Pickling course statistics data... {course_statistics}")
with open("course_stats.pkl", "wb") as pkl_file:
    pickle.dump(course_statistics, pkl_file)
print("Course statistics data has been pickled to 'course_stats.pkl'.")
pkl_file.close()

# Unpickle the data from the file
with open("course_stats.pkl", "rb") as pkl_file:
    print("Raw pickled data: ",end=" ")
    print(pkl_file.read())
pkl_file.close()    

with open("course_stats.pkl", "rb") as pkl_file:
    loaded_statistics = pickle.load(pkl_file)
    print(f"Unpickled Course Statistics: {loaded_statistics}")
pkl_file.close()