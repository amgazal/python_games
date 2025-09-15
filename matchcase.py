def passing_grades(grade):
    match grade:
        case 55:
            return "We have to work our grades up"
        case 60:
            return "You had a C"
        case 65:
            return "You had a C+"
        case 70:
            return "You had a B-"
        case 75:
            return "You had a B"
        case 80:
            return "You had a B+"
        case 85:
            return "You had an A"
        case 100:
            return "You had an A+"
        case _:
            return 'Kindly come see me'
