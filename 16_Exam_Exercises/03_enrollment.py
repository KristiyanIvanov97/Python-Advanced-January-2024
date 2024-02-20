# def gather_credits(credits_needed, *courses):
#     done_courses = []
#     total_credits = 0
#     for course_name, course_credits in courses:
#         if course_name not in done_courses:
#             done_courses.append(course_name)
#             total_credits += int(course_credits)
#             if total_credits >= credits_needed:
#                 return (f"Enrollment finished! Maximum credits: {total_credits}.\n"
#                         f"Courses: {', '.join(sorted(done_courses))}")
#
#     return (f"You need to enroll in more courses! "
#             f"You have to gather {credits_needed - total_credits} credits more.")

def gather_credits(number_of_credits_needed, *course_info):
    courses_enrolled = {}

    for course_name, credits in course_info:
        if sum(courses_enrolled.values()) >= number_of_credits_needed:
            break

        if course_name not in courses_enrolled:
            courses_enrolled[course_name] = credits

    if sum(courses_enrolled.values()) >= number_of_credits_needed:
        return (f"Enrollment finished! Maximum credits: {sum(courses_enrolled.values())}.\n"
                f"Courses: {', '.join(sorted(courses_enrolled))}")
    return (f"You need to enroll in more courses! "
            f"You have to gather {number_of_credits_needed - sum(courses_enrolled.values())} credits more.")


# print(gather_credits(
#     80,
#     ("Advanced", 30),
#     ("Basics", 27),
#     ("Fundamentals", 27),
# ))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 5),
    ("Advanced", 22),
))
