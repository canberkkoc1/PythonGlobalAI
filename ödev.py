name = 'canberk'
surname = "koç"


i = 0

while i < 3:
    ex = input('for exit "q" continue any key : ')
    if ex == 'q' or ex == 'Q':
        break

    else:

        inputName = input('Please Enter Your Name: ')
        inputSurname = input('Please Enter Your Surname: ')

        if inputName == name and inputSurname == surname:
            print('Login Success')

            courses = ['Math', 'Python', 'JavaScript', 'Java', 'R']
            print(','.join(courses))
            chc = []
            while True:

                coiceCourses = input('please select Coourses: ')
                if chc.count(coiceCourses):
                    print('You select this course please select another one')

                else:
                    if courses.count(coiceCourses):
                        chc.append(coiceCourses)
                        print('Success your courses = {}'.format(','.join(chc)))

                    else:
                        print('just select this courses {} : '.format(
                            ','.join(courses)))

                    cont = input(
                        'Do you want contiune select the course(y/n) : ')
                    if cont == 'y' or cont == 'Y':
                        continue

                    elif len(chc) < 3 and (cont == 'n' or cont == 'N'):
                        print('you fail')
                        break

                    elif len(chc) >= 3 and (cont == 'n' or cont == 'N'):
                        exam = input(
                            'choice course for exam = {} :'.format(','.join(chc)))

                        if exam in chc:
                            print('you choice the {}'.format(exam))
                            point = {'midterm': 0.3,
                                     'final': 0.5, 'project': 0.2}
                            mid = int(
                                input('Please Enter The Midterm result: '))
                            finals = int(
                                input('Please Enter The Final result: '))
                            project = int(
                                input('Please Enter The Project result: '))
                            midPoint = mid * point['midterm']
                            finalPoint = finals * point['final']
                            projectPoint = project * point['project']
                            totalPoint = midPoint + finalPoint + projectPoint
                            if totalPoint > 90:
                                print('AA')
                                break
                            elif totalPoint > 70 and totalPoint < 90:
                                print('BB')
                                break
                            elif totalPoint > 50 and totalPoint < 70:
                                print('CC')
                                break
                            elif totalPoint > 30 and totalPoint < 50:
                                print('DD')
                                break
                            else:
                                print('FF and you be failed')
                                break
                        elif exam not in chc:
                            print('Please select one this courses= {}'.format(
                                ','.join(chc)))
                            continue

                    else:
                        print('wrong input')

        else:
            print('Wrog name or surname!!!')
            i += 1

        if i >= 3:
            print("Please try again")
            break
