import pandas as pd
import xlsxwriter

writer = pd.ExcelWriter("output\\testdata.xlsx", engine="xlsxwriter")
data = {
    "Name": ["Player1", "Player2", None],
    "Team": ["TeamA", None, "TeamC"],
    "Number": [23, None, 45],
    "Position": ["G", "F", None],
    "Age": [25, None, 30],
    "Height": [78, 80, None],
    "Weight": [200, None, 220],
    "College": ["CollegeA", None, "CollegeC"],
    "Salary": [5000000, 0, None],
}
df_test = pd.DataFrame(data)

df_test.to_excel(writer, index=False, sheet_name="Some Data")
writer.close()

dfStudents = pd.read_csv("data\\student_data.csv")
dfCourses = pd.read_csv("data\\course_enrolled.csv")

outer_join = pd.merge(dfStudents, dfCourses, how="outer", on="name")

dfStyling = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

dfStyling.style.set_table_styles(
    [
        {
            "selector": "td",
            "props": [
                ("border", "2px solid blue"),
                ("background-color", "powderblue"),
                ("color", "darkblue"),
                ("padding", "10px"),
            ],
        }
    ]
)
